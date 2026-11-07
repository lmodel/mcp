#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Check the Model Context Protocol's repository against the version the schema models.

The schema models MCP 2026-07-28, the schema folder of that name at the tag 2026-07-28.
upstream/ holds that folder's schema.json, schema.ts and examples, and the repository's
LICENSE, unchanged. These things can change without any change in this repository:

- a new tag appears, or a new version folder under schema/;
- the pinned tag moves, or a pinned file changes or is deleted, or a file is added to the
  version folder, at the tag or on the default branch, beyond the edits the default branch
  already held when the pins were read;
- the licence file on the default branch changes.

The script lists the repository's trees through GitHub's API and compares git object hashes,
so it downloads no file. scripts/upstream_pins.tsv holds each file's hash. The script prints
a Markdown report and exits 1 on any of the above, or when a check could not finish.

Text a server chose is quoted as code on one line in the report, so the issue the workflow
opens from it cannot mention anyone. A redirect is followed only to an https address on
api.github.com. Set ``GITHUB_TOKEN`` to raise the API's rate limit. Usage::

    python scripts/check_upstream_release.py [--report FILE]
"""

from __future__ import annotations

import argparse
import http.client
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PINS = ROOT / "scripts" / "upstream_pins.tsv"
USER_AGENT = "lmodel-mcp-upstream-check"
API = "https://api.github.com/repos/modelcontextprotocol"
HOST = "api.github.com"

# The most the script reads of one answer. A recursive listing of the repository is a few MB.
MAX_BYTES = 20_000_000

SPEC = "modelcontextprotocol"
BRANCH = "main"

# What the schema models. tests/test_upstream.py checks that the schema header and these
# pins agree. Move them together, with upstream/ and scripts/upstream_pins.tsv, for another version.
VERSION = "2026-07-28"
TAG = "2026-07-28"
COMMIT = "5f5440bb26a62e2cf3440b92da5a667efa03b267"
FOLDER = f"schema/{VERSION}"

# Pinned files the default branch had already edited when the pins were read, with the hash
# each has there, so only a further edit stands out. Commit 38353251 (#3185) reworded the
# Tool's inputSchema description, changed one example and named two examples in schema.ts.
EDITED_ON_BRANCH = {
    f"{FOLDER}/examples/Tool/tool-with-composition-input-schema.json": (
        "aaaf501f4ed3febbd3ec904c70d4a300b5d05624"
    ),
    f"{FOLDER}/schema.json": "0b9ba317f95c3bc4b44724d65790f7aaaf557dbb",
    f"{FOLDER}/schema.ts": "0abde3c55dd07ee038c8614ce74f116150ff1c8c",
}

# The one file of the version folder that upstream/ leaves out, with its hash at the tag
# and on the default branch: schema.mdx, the outline of MCP's schema reference page, a
# heading per @category and no definition. A change to it is reported as for a pinned file.
NOT_COPIED = {
    f"{FOLDER}/schema.mdx": "023e8b9e758e9db4cd0f876e2ead8540b6652449",
}

# Everything the repository held when the pins were read, so anything new stands out. The
# folder pattern finds a version folder by its date.
KNOWN_TAGS = (
    "2024-10-07",
    "2024-11-05",
    "2024-11-05-final",
    "2025-03-26",
    "2025-06-18",
    "2025-11-25",
    "2025-11-25-RC",
    "2026-07-28",
    "2026-07-28-RC",
)
KNOWN_FOLDERS = (
    "2024-11-05",
    "2025-03-26",
    "2025-06-18",
    "2025-11-25",
    "2026-07-28",
)
VERSION_FOLDER = re.compile(r"^\d{4}-\d{2}-\d{2}")


class _ApiRedirect(urllib.request.HTTPRedirectHandler):
    """Follow a redirect only to an https address on the API's host."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        parts = urllib.parse.urlsplit(newurl)
        if parts.scheme != "https" or parts.hostname != HOST:
            raise ValueError(f"a redirect leads off {HOST}, to {newurl}")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


# An opener in place of urlopen's, whose redirect handler follows any address.
_open = urllib.request.build_opener(_ApiRedirect).open


def _get(path: str):
    """The JSON answer to one API path, read up to the cap."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(f"{API}{path}", headers=headers)
    with _open(req, timeout=60) as resp:
        body = resp.read(MAX_BYTES + 1)
    if len(body) > MAX_BYTES:
        raise ValueError(f"the answer to {path} is larger than {MAX_BYTES} bytes")
    return json.loads(body)


def _code(text: object) -> str:
    """Text a server chose, as a code span on one line, so it cannot mention a person or add a
    link in the issue. A blank line would end the span, so every run of spaces and line breaks
    is one space."""
    return "`" + " ".join(str(text).replace("`", "'").split()) + "`"


def pins() -> dict[str, str]:
    """Each pinned path, under its repository's name, and its git object hash."""
    rows = (line.split("\t") for line in PINS.read_text(encoding="utf-8").splitlines())
    return {path: sha for path, sha in rows}


def _pins_of(repository: str) -> dict[str, str]:
    """The pins of one repository, by the path inside it."""
    prefix = f"{repository}/"
    return {
        path.removeprefix(prefix): sha
        for path, sha in pins().items()
        if path.startswith(prefix)
    }


def _subtree(repository: str, ref: str, folder: str) -> str:
    """The git object hash of a folder at a ref, found one level at a time, so the listing
    stays small however large the repository grows."""
    sha = ref
    for part in folder.split("/"):
        entries = _get(f"/{repository}/git/trees/{sha}")["tree"]
        sha = next(
            e["sha"] for e in entries if e["path"] == part and e["type"] == "tree"
        )
    return sha


def _blobs(repository: str, ref: str, folder: str) -> dict[str, str]:
    """Each file of one folder of a repository at a ref, by its path from the root. A
    listing GitHub cuts short cannot be compared."""
    answer = _get(
        f"/{repository}/git/trees/{_subtree(repository, ref, folder)}?recursive=1"
    )
    if answer.get("truncated"):
        raise ValueError(f"GitHub cut short the listing of {folder} at {ref}")
    return {
        f"{folder}/{e['path']}": e["sha"] for e in answer["tree"] if e["type"] == "blob"
    }


def _tag_commit(repository: str, tag: str) -> str:
    """The commit a tag names, through its tag object when it has one."""
    target = _get(f"/{repository}/git/ref/tags/{tag}")["object"]
    if target["type"] == "tag":
        target = _get(f"/{repository}/git/tags/{target['sha']}")["object"]
    return target["sha"]


def _compare(found: dict[str, str], expected: dict[str, str], place: str) -> list[str]:
    """One line for each kind of difference between the pins and a listing."""
    lines = []
    gone = sorted(path for path in expected if path not in found)
    changed = sorted(
        path for path, sha in expected.items() if path in found and found[path] != sha
    )
    added = sorted(path for path in found if path not in expected)
    for label, paths in (
        ("pinned files gone", gone),
        ("pinned files changed", changed),
        ("files added", added),
    ):
        if paths:
            shown = ", ".join(_code(path) for path in paths)
            lines.append(f"- **{len(paths)} {label} {place}:** {shown}.")
    return lines


def _tags(repository: str) -> set[str]:
    """Every tag of a repository, page by page, so none past the first hundred is missed."""
    tags: set[str] = set()
    for page in range(1, 11):
        found = _get(f"/{repository}/tags?per_page=100&page={page}")
        tags |= {entry["name"] for entry in found}
        if len(found) < 100:
            return tags
    raise ValueError(f"{repository} has over 1000 tags, more than the watch reads")


def check_versions() -> tuple[list[str], bool]:
    """Report any tag or version folder the pins did not know."""
    tags = _tags(SPEC)
    folders = {
        entry["path"]
        for entry in _get(f"/{SPEC}/git/trees/{_subtree(SPEC, BRANCH, 'schema')}")[
            "tree"
        ]
        if entry["type"] == "tree" and VERSION_FOLDER.match(entry["path"])
    }
    lines = []
    new_tags = sorted(tags - set(KNOWN_TAGS))
    new_folders = sorted(folders - set(KNOWN_FOLDERS))
    if new_tags:
        shown = ", ".join(_code(tag) for tag in new_tags)
        lines.append(f"- **New tags in MCP's repository:** {shown}.")
    if new_folders:
        shown = ", ".join(_code(folder) for folder in new_folders)
        lines.append(f"- **New version folders under schema/:** {shown}.")
    if lines:
        lines.append(
            "- Read what changed, decide whether the schema moves to it, and move upstream/, "
            "the pins, the converter's input and the schema header together."
        )
        return lines, True
    return ["- No new tag or version folder in MCP's repository."], False


def check_version() -> tuple[list[str], bool]:
    """Report whether the version's tag still names the pinned commit and files, and whether
    the default branch edited a pinned file beyond the edits already known."""
    commit = _tag_commit(SPEC, TAG)
    lines = []
    if commit != COMMIT:
        lines.append(
            f"- **The tag {TAG} moved to {_code(commit)}.** Find out why a published "
            "version moved before trusting the copy in upstream/."
        )
    expected = {
        path: sha
        for path, sha in _pins_of(SPEC).items()
        if path.startswith(f"{FOLDER}/")
    }
    at_tag = expected | NOT_COPIED
    lines += _compare(_blobs(SPEC, commit, FOLDER), at_tag, f"at {TAG}")
    on_branch = at_tag | EDITED_ON_BRANCH
    lines += _compare(_blobs(SPEC, BRANCH, FOLDER), on_branch, f"on {BRANCH}")
    if lines:
        return lines, True
    return [
        f"- MCP {VERSION}'s {len(expected)} pinned files are unchanged, and {BRANCH} holds "
        f"only the {len(EDITED_ON_BRANCH)} known edits."
    ], False


def check_licence() -> tuple[list[str], bool]:
    """Report whether the licence on the default branch is the pinned file."""
    root = {e["path"]: e["sha"] for e in _get(f"/{SPEC}/git/trees/{BRANCH}")["tree"]}
    if root.get("LICENSE") != pins()[f"{SPEC}/LICENSE"]:
        return [
            "- **The LICENSE changed on the default branch.** Read what changed, and update "
            "NOTICE if the licence moved."
        ], True
    return ["- The licence on the default branch is the pinned file."], False


# Each check, by the name the report gives it when it cannot finish.
CHECKS = (
    ("new versions", check_versions),
    (f"MCP {VERSION}", check_version),
    ("licence", check_licence),
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--report", type=Path, help="Also write the Markdown report to this file"
    )
    args = parser.parse_args(argv)
    lines = [f"- Pinned version: MCP {VERSION} at the tag {TAG}."]
    attention = False
    for label, check in CHECKS:
        try:
            found, needs = check()
        # OSError covers a refused or failed request and a timeout, HTTPException and EOFError
        # a connection cut off mid-answer, and LookupError, TypeError, AttributeError,
        # StopIteration and ValueError an answer of another shape or too large.
        except (
            OSError,
            http.client.HTTPException,
            EOFError,
            LookupError,
            TypeError,
            AttributeError,
            StopIteration,
            ValueError,
        ) as err:
            found = [f"- **The {label} check could not finish: {_code(err)}.**"]
            needs = True
        lines += found
        attention = attention or needs
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.report:
        args.report.write_text(text, encoding="utf-8")
    return 1 if attention else 0


if __name__ == "__main__":
    sys.exit(main())
