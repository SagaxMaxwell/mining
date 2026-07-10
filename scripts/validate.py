"""Validate active tutorials."""

from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SKIPPED_PARTS = {".git", ".venv", "archive"}
TEXT_SUFFIXES = {".md", ".py", ".ipynb", ".toml"}
DEPRECATED_TOKENS = {
    "customer-segmentation",
    "data-exploration",
    "temperature-autoregression",
    "market-basket-analysis",
    "time-series-arima",
    "association-rules",
    "environment-setup",
    "validate_tutorials",
    "mall_customers",
    "goods_order",
    "goods_types",
    "milk_production",
    "daily_temperature",
    "menu_orders",
    "milk.csv",
    "statsmodels",
    "xlrd",
    "AutoReg",
    "ARIMA",
    "old_names=False",
}


def iter_files(pattern: str) -> list[Path]:
    return sorted(PROJECT_ROOT.glob(pattern))


def should_skip(path: Path) -> bool:
    return bool(SKIPPED_PARTS.intersection(path.relative_to(PROJECT_ROOT).parts))


def relative(path: Path) -> str:
    return str(path.relative_to(PROJECT_ROOT))


def validate_markdown_files() -> list[str]:
    issues: list[str] = []
    for path in iter_files("**/*.md"):
        if should_skip(path):
            continue
        text = path.read_text(encoding="utf-8")
        if "<b>" in text or "</b>" in text:
            issues.append(f"{relative(path)}: avoid HTML bold tags")
        if "> - #" in text:
            issues.append(f"{relative(path)}: avoid quoted bullet headings")
    return issues


def validate_python_files() -> list[str]:
    issues: list[str] = []
    for pattern in ("scripts/**/*.py", "tutorials/*.py"):
        for path in iter_files(pattern):
            if should_skip(path):
                continue
            try:
                ast.parse(path.read_text(encoding="utf-8"), filename=relative(path))
            except SyntaxError as exc:
                issues.append(
                    f"{relative(path)}: {exc.msg} at line {exc.lineno}, column {exc.offset}"
                )
    return issues


def validate_notebook_files() -> list[str]:
    issues: list[str] = []
    for path in iter_files("tutorials/**/*.ipynb"):
        relative_path = relative(path)
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


def validate_references() -> list[str]:
    issues: list[str] = []
    for readme in iter_files("tutorials/*/README.md"):
        if should_skip(readme):
            continue
        text = readme.read_text(encoding="utf-8")
        for ref in re.findall(r"`([^`]+)`", text):
            if not ref.endswith((".csv", ".xls", ".ipynb")):
                continue
            target = (readme.parent / ref).resolve()
            if not target.exists():
                issues.append(f"{relative(readme)}: missing referenced file {ref}")

    data_readme = PROJECT_ROOT / "data" / "README.md"
    for ref in re.findall(r"`([^`]+)`", data_readme.read_text(encoding="utf-8")):
        if ref.endswith((".csv", ".xls")) and not (data_readme.parent / ref).exists():
            issues.append(f"{relative(data_readme)}: missing listed data file {ref}")

    for notebook_path in iter_files("tutorials/**/*.ipynb"):
        if should_skip(notebook_path):
            continue
        notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
        for cell in notebook.get("cells", []):
            source = "".join(cell.get("source", []))
            for ref in re.findall(r'DATA_DIR / "([^"]+)"', source):
                if not (PROJECT_ROOT / "data" / ref).exists():
                    issues.append(
                        f"{relative(notebook_path)}: missing referenced data file {ref}"
                    )
    return issues


def validate_stale_references() -> list[str]:
    issues: list[str] = []
    validator_path = Path(__file__).resolve()
    for path in iter_files("**/*"):
        if (
            path.resolve() == validator_path
            or should_skip(path)
            or not path.is_file()
            or path.suffix not in TEXT_SUFFIXES
        ):
            continue
        text = path.read_text(encoding="utf-8")
        for token in sorted(DEPRECATED_TOKENS):
            if token in text:
                issues.append(f"{relative(path)}: stale reference {token!r}")
    return issues


def validate_data_usage() -> list[str]:
    referenced = set()
    for readme in iter_files("tutorials/*/README.md"):
        if should_skip(readme):
            continue
        text = readme.read_text(encoding="utf-8")
        referenced.update(re.findall(r"`../../data/([^`]+)`", text))

    for notebook_path in iter_files("tutorials/**/*.ipynb"):
        if should_skip(notebook_path):
            continue
        notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
        for cell in notebook.get("cells", []):
            source = "".join(cell.get("source", []))
            referenced.update(re.findall(r'DATA_DIR / "([^"]+)"', source))

    issues: list[str] = []
    for path in iter_files("data/*"):
        if not path.is_file() or path.name == "README.md":
            continue
        if path.name not in referenced:
            issues.append(f"{relative(path)}: active data file is not referenced")
    return issues


def main() -> int:
    issues = (
        validate_markdown_files()
        + validate_python_files()
        + validate_notebook_files()
        + validate_references()
        + validate_stale_references()
        + validate_data_usage()
    )
    if issues:
        for issue in issues:
            print(issue)
        return 1

    print("Tutorial validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
