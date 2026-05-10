"""Validate tutorial Markdown and notebook source code."""

from __future__ import annotations

import ast
import json
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def iter_files(pattern: str) -> list[Path]:
    """Return project files matching a glob pattern.

    Args:
        pattern: Glob pattern relative to the project root.

    Returns:
        Sorted matching files.
    """
    return sorted(PROJECT_ROOT.glob(pattern))


def validate_markdown_files() -> list[str]:
    """Validate tutorial Markdown style rules.

    Returns:
        Human-readable issue messages. An empty list means no issues were found.
    """
    issues: list[str] = []
    for path in iter_files("**/*.md"):
        if ".git" in path.parts or ".venv" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        if "<b>" in text or "</b>" in text:
            issues.append(f"{path.relative_to(PROJECT_ROOT)}: avoid HTML bold tags")
        if "> - #" in text:
            issues.append(f"{path.relative_to(PROJECT_ROOT)}: avoid quoted bullet headings")
    return issues


def validate_notebook_files() -> list[str]:
    """Validate notebook JSON and Python code cell syntax.

    Returns:
        Human-readable issue messages. An empty list means no issues were found.
    """
    issues: list[str] = []
    for path in iter_files("tutorials/**/*.ipynb"):
        relative_path = path.relative_to(PROJECT_ROOT)
        try:
            notebook = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            issues.append(f"{relative_path}: invalid JSON: {exc}")
            continue

        for index, cell in enumerate(notebook.get("cells", []), start=1):
            if cell.get("cell_type") != "code":
                continue
            source = "".join(cell.get("source", []))
            try:
                ast.parse(source, filename=f"{relative_path}:cell-{index}")
            except SyntaxError as exc:
                issues.append(
                    f"{relative_path}: code cell {index}: {exc.msg} "
                    f"at line {exc.lineno}, column {exc.offset}"
                )
    return issues


def main() -> int:
    """Run all static tutorial validations.

    Returns:
        Process exit code. Returns 0 when all checks pass.
    """
    issues = validate_markdown_files() + validate_notebook_files()
    if issues:
        for issue in issues:
            print(issue)
        return 1

    print("Tutorial validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
