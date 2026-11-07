"""Compares the JSON Schema the model gives with the schema.json MCP publishes.

tests/test_parity.py runs three tiers over these helpers:

1. Addresses. The generated file compiles, every reference in it resolves, and every
   definition MCP publishes is there, but those parity/probes.yaml lists as gaps.
2. Verdicts. Each of MCP's examples, each example under tests/data/problem/, a smallest
   valid instance of each definition, and each mutation of all of these get the same
   verdict from both files, or the difference parity/probes.yaml expects.
3. Structure. The definitions that differ in shape once both sides are normalised are the
   ones parity/structural.yaml lists, each with its reason.
"""

from __future__ import annotations

import copy
import json
from functools import lru_cache
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
VERSION = "2026-07-28"
PUBLISHED = (
    ROOT / "upstream" / "modelcontextprotocol" / "schema" / VERSION / "schema.json"
)
EXAMPLES = PUBLISHED.parent / "examples"
GENERATED = ROOT / "meta" / "schema.json"
PARITY = ROOT / "parity"
PROBLEM = ROOT / "tests" / "data" / "problem"
DEFS = "#/$defs/"
ANNOTATIONS = ("description", "title", "examples", "$comment", "format")

# A value of each JSON kind, for the mutations that change a value's kind.
OTHER_KINDS = ("text", 7, 2.5, True, None, [], {})


@lru_cache(maxsize=None)
def load(which: str) -> dict:
    """MCP's file ("published"), the file the model gives ("generated"), or MCP's file with
    the rules MCP's words state and its file does not, which probes.yaml lists as
    narrower ("stated"). Tier 2 compares "stated" with "generated"."""
    if which == "stated":
        doc = copy.deepcopy(load("published"))
        for rule in probes()["narrower"]:
            target = doc["$defs"][rule["definition"]]
            target["anyOf"] = target.get("anyOf", []) + rule["anyOf"]
        return doc
    path = PUBLISHED if which == "published" else GENERATED
    return json.loads(path.read_text(encoding="utf-8"))


@lru_cache(maxsize=None)
def validator(which: str, name: str) -> Draft202012Validator:
    """A validator for one definition of one file, with the file's definitions beside it."""
    doc = load(which)
    return Draft202012Validator(
        {"$schema": doc["$schema"], "$defs": doc["$defs"], "$ref": DEFS + name}
    )


def verdict(which: str, name: str, instance) -> bool:
    return validator(which, name).is_valid(instance)


@lru_cache(maxsize=None)
def probes() -> dict:
    return yaml.safe_load((PARITY / "probes.yaml").read_text(encoding="utf-8"))


@lru_cache(maxsize=None)
def structural() -> dict:
    return yaml.safe_load((PARITY / "structural.yaml").read_text(encoding="utf-8"))


def definition_of(path: Path) -> str:
    """The definition an example under tests/data/problem/ is an instance of: its class's
    name, McpTool for Tool, without the prefix every class carries."""
    cls = path.stem.split("-")[0]
    if not cls.startswith("Mcp"):
        raise ValueError(f"{path.name} does not start with a class name")
    return cls[len("Mcp") :]


def _yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


# Tier 1 --------------------------------------------------------------------------------


def refs(node):
    """Every $ref anywhere in a JSON tree."""
    if isinstance(node, dict):
        if isinstance(node.get("$ref"), str):
            yield node["$ref"]
        for value in node.values():
            yield from refs(value)
    elif isinstance(node, list):
        for item in node:
            yield from refs(item)


def missing_definitions() -> set[str]:
    return set(load("published")["$defs"]) - set(load("generated")["$defs"])


# Tier 2 --------------------------------------------------------------------------------


def smallest(name: str, depth: int = 0):
    """The smallest instance of a definition, with the stated rules: its required keys
    only, and those of the first branch of a rule, each with its const, its first enum
    value, or the least value of its type."""
    defs = load("stated")["$defs"]
    return _smallest(defs[name], defs, depth)


def _smallest(node: dict, defs: dict, depth: int):
    if depth > 12:
        raise ValueError("the definitions nest too deep to build an instance")
    if "$ref" in node:
        return _smallest(defs[node["$ref"][len(DEFS) :]], defs, depth + 1)
    if "const" in node:
        return node["const"]
    if "enum" in node:
        return node["enum"][0]
    if "allOf" in node:
        merged: dict = {}
        for part in node["allOf"]:
            value = _smallest(part, defs, depth + 1)
            merged = merged | value if isinstance(value, dict) else value
        return merged
    if "anyOf" in node and "properties" not in node:
        return _smallest(node["anyOf"][0], defs, depth + 1)
    kind = node.get("type")
    if isinstance(kind, list):
        kind = kind[0]
    if kind == "object" or "properties" in node:
        keys = list(node.get("required", []))
        if node.get("anyOf"):
            keys += node["anyOf"][0].get("required", [])
        return {
            key: _smallest(node["properties"][key], defs, depth + 1) for key in keys
        }
    if kind == "array":
        return [
            _smallest(node["items"], defs, depth + 1)
            for _ in range(node.get("minItems", 0))
        ]
    if kind == "string":
        return {
            "uri": "https://example.com/a",
            "byte": "AA==",
            "uri-template": "file:///{path}",
        }.get(node.get("format"), "a")
    if kind in ("integer", "number"):
        return node.get("minimum", 0)
    if kind == "boolean":
        return False
    return {}


def mutations(instance):
    """Each instance one change away: a key removed, a value of another kind, or a string
    no list allows. Each comes with the JSON pointer of what changed."""

    def walk(node, path):
        if isinstance(node, dict):
            for key in node:
                where = f"{path}/{key}"
                removed = {k: v for k, v in node.items() if k != key}
                yield where + " removed", removed, path
                for other in OTHER_KINDS:
                    if type(other) is not type(node[key]):
                        yield (
                            where + f" as {json.dumps(other)}",
                            node | {key: other},
                            path,
                        )
                if isinstance(node[key], str):
                    yield where + " misspelt", node | {key: node[key] + "-x"}, path
                if type(node[key]) in (int, float):
                    for other in (node[key] - 100, node[key] + 100):
                        yield where + f" as {other}", node | {key: other}, path
                for label, child, child_path in walk(node[key], where):
                    yield label, node | {key: child}, child_path
        elif isinstance(node, list):
            for i, item in enumerate(node):
                for label, child, child_path in walk(item, f"{path}/{i}"):
                    yield label, node[:i] + [child] + node[i + 1 :], child_path

    yield from ((label, value) for label, value, _ in walk(instance, ""))


def corpus():
    """Every positive document with the definition it is an instance of: MCP's examples,
    the examples under tests/data/problem/valid/ (named <Class>-<anything>.yaml), and the
    smallest instance of each published definition."""
    for path in sorted(EXAMPLES.rglob("*.json")):
        yield (
            f"examples/{path.parent.name}/{path.name}",
            path.parent.name,
            json.loads(path.read_text()),
        )
    for path in sorted((PROBLEM / "valid").glob("*.yaml")):
        yield f"problem/valid/{path.name}", definition_of(path), _yaml(path)
    for name, node in load("published")["$defs"].items():
        if name not in missing_definitions():
            yield f"smallest/{name}", name, smallest(name)


def counter_examples():
    """The examples under tests/data/problem/invalid/, which both files must reject.
    Each is named <Class>-<anything>.yaml."""
    for path in sorted((PROBLEM / "invalid").glob("*.yaml")):
        yield f"problem/invalid/{path.name}", definition_of(path), _yaml(path)


def differences():
    """Each document and mutation the two files judge differently, as (label, definition,
    verdict of MCP's file with the stated rules, generated verdict)."""
    found = []
    for label, name, doc in corpus():
        cases = [(label, doc)] + [
            (f"{label} {change}", value) for change, value in mutations(doc)
        ]
        for case, value in cases:
            published = verdict("stated", name, value)
            generated = verdict("generated", name, value)
            if published != generated:
                found.append((case, name, published, generated))
    return found


# Tier 3 --------------------------------------------------------------------------------


def _scalar(body: dict) -> bool:
    """A definition of a value that is no object: a string, a string or an integer."""
    return (
        "properties" not in body
        and "anyOf" not in body
        and body.get("type") != "object"
    )


def normalise(node, defs: dict, inline: bool = False):
    """A schema in a form both files share: annotations out, a reference to a scalar
    definition replaced by its body and any other kept by name, allOf merged with its base
    inlined, a type list read as an anyOf of types, an open object's additionalProperties
    dropped, required as a sorted list. With ``inline``, a reference at the top is followed
    once, as for a definition that only names another."""
    if isinstance(node, list):
        return [normalise(item, defs) for item in node]
    if not isinstance(node, dict):
        return node
    node = {k: v for k, v in node.items() if k not in ANNOTATIONS}
    if "$ref" in node:
        target = node["$ref"][len(DEFS) :]
        if inline or _scalar(defs[target]):
            rest = {k: v for k, v in node.items() if k != "$ref"}
            body = normalise(defs[target], defs)
            return normalise({"allOf": [body, rest]}, defs) if rest else body
        return {"$ref": DEFS + target}
    if "allOf" in node:
        merged: dict = {}
        for part in node.pop("allOf"):
            part = normalise(part, defs, inline=True)
            for key, value in part.items():
                if key == "properties":
                    merged.setdefault("properties", {})
                    for prop, schema in value.items():
                        merged["properties"][prop] = (
                            _merge(merged["properties"][prop], schema)
                            if prop in merged["properties"]
                            else schema
                        )
                elif key == "required":
                    merged["required"] = sorted(
                        set(merged.get("required", [])) | set(value)
                    )
                else:
                    merged[key] = value
        return normalise(merged | node, defs)
    if isinstance(node.get("type"), list):
        kinds = node.pop("type")
        node["anyOf"] = [{"type": k} for k in kinds] + node.get("anyOf", [])
    if node.get("additionalProperties") in ({}, True):
        node.pop("additionalProperties")
    if node.get("properties") == {}:
        node.pop("properties")
    if "required" in node:
        node["required"] = sorted(node["required"])
    out = {}
    for key, value in node.items():
        if key == "properties":
            out[key] = {prop: normalise(schema, defs) for prop, schema in value.items()}
        elif key in ("items", "additionalProperties", "not"):
            out[key] = normalise(value, defs)
        elif key in ("anyOf", "oneOf"):
            branches = []
            for branch in normalise(value, defs):
                branches += branch["anyOf"] if set(branch) == {"anyOf"} else [branch]
            out[key] = sorted(branches, key=lambda b: json.dumps(b, sort_keys=True))
        else:
            out[key] = value
    if set(out) == {"anyOf"} and len(out["anyOf"]) == 1:
        return out["anyOf"][0]
    return out


def _merge(left: dict, right: dict) -> dict:
    """Two schemas for one property, merged as allOf merges them where they do not clash."""
    merged = copy.deepcopy(left)
    for key, value in right.items():
        merged[key] = value
    return merged


def shape_differences() -> dict[str, str]:
    """Each definition whose normalised shape differs, with the first pointer that differs."""
    published, generated = load("published")["$defs"], load("generated")["$defs"]
    found = {}
    for name in sorted(set(published) & set(generated)):
        left = normalise(published[name], published, inline=True)
        right = normalise(generated[name], generated, inline=True)
        if left != right:
            found[name] = _first_difference(left, right, "")
    return found


def _first_difference(left, right, path: str) -> str:
    if isinstance(left, dict) and isinstance(right, dict):
        for key in sorted(set(left) | set(right)):
            if left.get(key) != right.get(key):
                return _first_difference(left.get(key), right.get(key), f"{path}/{key}")
    if isinstance(left, list) and isinstance(right, list) and len(left) == len(right):
        for i, (a, b) in enumerate(zip(left, right)):
            if a != b:
                return _first_difference(a, b, f"{path}/{i}")
    return path or "/"
