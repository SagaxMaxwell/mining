"""Notebook helpers."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

try:
    from IPython.display import display
except ImportError:
    display = print


RANDOM_STATE = 42


def find_project_root(start: Path | str | None = None) -> Path:
    current = Path.cwd() if start is None else Path(start).resolve()
    for path in [current, *current.parents]:
        if (path / "data").is_dir() and (path / "pyproject.toml").is_file():
            return path
    raise FileNotFoundError("未找到包含 data/ 和 pyproject.toml 的项目根目录")


PROJECT_ROOT = find_project_root()
DATA_DIR = PROJECT_ROOT / "data"


def configure_matplotlib() -> None:
    plt.rcParams["font.sans-serif"] = ["SimHei", "Arial Unicode MS", "DejaVu Sans"]
    plt.rcParams["axes.unicode_minus"] = False


def regression_metrics(actual: pd.Series, forecast: pd.Series) -> pd.DataFrame:
    from sklearn.metrics import mean_absolute_error, root_mean_squared_error

    aligned = pd.concat(
        {"actual": pd.Series(actual), "forecast": pd.Series(forecast)}, axis=1
    ).dropna()
    error = aligned["actual"] - aligned["forecast"]
    denominator = aligned["actual"].abs().replace(0, np.nan)
    return pd.DataFrame(
        {
            "MAE": [mean_absolute_error(aligned["actual"], aligned["forecast"])],
            "RMSE": [root_mean_squared_error(aligned["actual"], aligned["forecast"])],
            "MAPE": [(error.abs() / denominator).mean()],
        }
    )


configure_matplotlib()
