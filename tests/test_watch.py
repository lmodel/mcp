"""Checks the upstream watch's decisions against stubbed answers.

scripts/check_upstream_release.py lists the repository through GitHub's API. These tests
replace its one network call, `_get`, with a table of answers, so they run offline. They
show what the report says in each case the watch knows.
"""

import http.client
import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "check_upstream_release.py"


@pytest.fixture
def watch():
    """A fresh copy of the script, so no test sees another's stub."""
    spec = importlib.util.spec_from_file_location("watch_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _files(watch, ref):
    """The pinned version's folder at a ref, by path inside the folder."""
    prefix = f"{watch.SPEC}/{watch.FOLDER}/"
    files = {
        path.removeprefix(prefix): sha
        for path, sha in watch.pins().items()
        if path.startswith(prefix)
    }
    if ref == watch.BRANCH:
        folder = f"{watch.FOLDER}/"
        files |= {p.removeprefix(folder): s for p, s in watch.EDITED_ON_BRANCH.items()}
    return {"tree": [{"path": p, "type": "blob", "sha": s} for p, s in files.items()]}


def _answers(watch):
    """The answers of an unchanged upstream, at the tag's commit and on the branch."""
    spec, licence = watch.SPEC, watch.pins()[f"{watch.SPEC}/LICENSE"]
    answers = {
        f"/{spec}/tags?per_page=100&page=1": [{"name": t} for t in watch.KNOWN_TAGS],
        f"/{spec}/git/ref/tags/{watch.TAG}": {
            "object": {"type": "commit", "sha": watch.COMMIT}
        },
    }
    for ref in (watch.COMMIT, watch.BRANCH):
        answers[f"/{spec}/git/trees/{ref}"] = {
            "tree": [
                {"path": "LICENSE", "type": "blob", "sha": licence},
                {"path": "schema", "type": "tree", "sha": f"schema-{ref}"},
            ]
        }
        answers[f"/{spec}/git/trees/schema-{ref}"] = {
            "tree": [
                {"path": f, "type": "tree", "sha": f"{f}-{ref}"}
                for f in (*watch.KNOWN_FOLDERS, "draft")
            ]
        }
        answers[f"/{spec}/git/trees/{watch.VERSION}-{ref}?recursive=1"] = _files(
            watch, ref
        )
    return answers


def _run(watch, answers, capsys, argv=()):
    def fake_get(path):
        answer = answers[path]
        if isinstance(answer, Exception):
            raise answer
        return answer

    watch._get = fake_get
    code = watch.main(list(argv))
    return code, capsys.readouterr().out


def test_an_unchanged_upstream_reports_nothing(watch, capsys):
    code, report = _run(watch, _answers(watch), capsys)
    assert code == 0, report
    assert "**" not in report
    assert "only the 3 known edits" in report


def test_a_new_tag_is_reported_and_quoted(watch, capsys):
    answers = _answers(watch)
    answers[f"/{watch.SPEC}/tags?per_page=100&page=1"].append({"name": "2027-01-15-RC"})
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert "`2027-01-15-RC`" in report


def test_a_new_version_folder_is_reported(watch, capsys):
    answers = _answers(watch)
    answers[f"/{watch.SPEC}/git/trees/schema-{watch.BRANCH}"]["tree"].append(
        {"path": "2027-01-15", "type": "tree", "sha": "x"}
    )
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert "`2027-01-15`" in report


def test_a_folder_that_names_no_version_stays_quiet(watch, capsys):
    answers = _answers(watch)
    answers[f"/{watch.SPEC}/git/trees/schema-{watch.BRANCH}"]["tree"].append(
        {"path": "tools", "type": "tree", "sha": "x"}
    )
    code, report = _run(watch, answers, capsys)
    assert code == 0, report


def test_a_moved_tag_is_reported(watch, capsys):
    answers = _answers(watch)
    moved = "2" * 40
    answers[f"/{watch.SPEC}/git/ref/tags/{watch.TAG}"] = {
        "object": {"type": "commit", "sha": moved}
    }
    for key in [k for k in answers if watch.COMMIT in k]:
        answers[key.replace(watch.COMMIT, moved)] = answers[key]
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert f"moved to `{moved}`" in report


def test_an_annotated_tag_is_followed(watch, capsys):
    """MCP's tags name commits directly today; an annotated one is read through its
    object."""
    answers = _answers(watch)
    annotated = "1" * 40
    answers[f"/{watch.SPEC}/git/ref/tags/{watch.TAG}"] = {
        "object": {"type": "tag", "sha": annotated}
    }
    answers[f"/{watch.SPEC}/git/tags/{annotated}"] = {
        "object": {"type": "commit", "sha": watch.COMMIT}
    }
    code, report = _run(watch, answers, capsys)
    assert code == 0, report


def test_a_further_edit_on_the_branch_is_reported_by_path(watch, capsys):
    answers = _answers(watch)
    listing = answers[
        f"/{watch.SPEC}/git/trees/{watch.VERSION}-{watch.BRANCH}?recursive=1"
    ]
    for entry in listing["tree"]:
        if entry["path"] == "schema.json":
            entry["sha"] = "0" * 40
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert f"1 pinned files changed on {watch.BRANCH}" in report
    assert f"`{watch.FOLDER}/schema.json`" in report


def test_a_file_gone_at_the_tag_is_reported_by_path(watch, capsys):
    answers = _answers(watch)
    key = f"/{watch.SPEC}/git/trees/{watch.VERSION}-{watch.COMMIT}?recursive=1"
    answers[key]["tree"] = [e for e in answers[key]["tree"] if e["path"] != "schema.ts"]
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert f"1 pinned files gone at {watch.TAG}" in report


def test_a_changed_licence_is_reported(watch, capsys):
    answers = _answers(watch)
    root = answers[f"/{watch.SPEC}/git/trees/{watch.BRANCH}"]
    root["tree"] = [dict(entry) for entry in root["tree"]]
    root["tree"][0]["sha"] = "3" * 40
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert "The LICENSE changed" in report


def test_a_truncated_listing_cannot_finish(watch, capsys):
    answers = _answers(watch)
    answers[f"/{watch.SPEC}/git/trees/{watch.VERSION}-{watch.BRANCH}?recursive=1"][
        "truncated"
    ] = True
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert "could not finish" in report


def test_a_missing_folder_cannot_finish(watch, capsys):
    answers = _answers(watch)
    answers[f"/{watch.SPEC}/git/trees/schema-{watch.BRANCH}"]["tree"] = []
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert f"The MCP {watch.VERSION} check could not finish" in report


@pytest.mark.parametrize(
    "failure",
    [
        OSError("refused"),
        http.client.RemoteDisconnected("cut"),
        KeyError("tree"),
        ValueError("too large"),
    ],
    ids=lambda e: type(e).__name__,
)
def test_a_failed_request_cannot_finish_and_is_quoted(watch, capsys, failure):
    answers = _answers(watch)
    answers[f"/{watch.SPEC}/tags?per_page=100&page=1"] = failure
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert "The new versions check could not finish" in report


def test_an_answer_of_another_shape_cannot_finish(watch, capsys):
    """A mapping where the watch expects a list stops one check, and the others still run."""
    answers = _answers(watch)
    answers[f"/{watch.SPEC}/tags?per_page=100&page=1"] = {"message": "Moved"}
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert "The new versions check could not finish" in report
    assert "The licence on the default branch is the pinned file." in report


def test_server_text_cannot_mention_or_link(watch, capsys):
    """A tag's name reaches an issue only as code on one line."""
    answers = _answers(watch)
    answers[f"/{watch.SPEC}/tags?per_page=100&page=1"].append(
        {"name": "@someone\n\n`x`"}
    )
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert "`@someone 'x'`" in report


def test_a_second_page_of_tags_is_read(watch, capsys):
    answers = _answers(watch)
    answers[f"/{watch.SPEC}/tags?per_page=100&page=1"] = [
        {"name": f"2020-01-{n:02d}"} for n in range(100)
    ]
    answers[f"/{watch.SPEC}/tags?per_page=100&page=2"] = [
        {"name": tag} for tag in watch.KNOWN_TAGS
    ]
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert "`2020-01-00`" in report


def test_a_redirect_off_the_api_is_refused(watch):
    handler = watch._ApiRedirect()
    with pytest.raises(ValueError, match="leads off"):
        handler.redirect_request(None, None, 302, "Found", {}, "https://example.org/x")
    with pytest.raises(ValueError, match="leads off"):
        handler.redirect_request(
            None, None, 302, "Found", {}, "http://api.github.com/x"
        )


def test_the_report_goes_to_a_file_when_asked(watch, capsys, tmp_path):
    target = tmp_path / "report.md"
    code, report = _run(watch, _answers(watch), capsys, ["--report", str(target)])
    assert code == 0
    assert target.read_text(encoding="utf-8") == report


def test_the_watch_reads_only_github():
    """The watch has no address but GitHub's API."""
    text = SCRIPT.read_text(encoding="utf-8")
    addresses = [part.split('"')[0] for part in text.split("https://")[1:]]
    assert addresses
    assert all(address.startswith("api.github.com") for address in addresses), addresses
