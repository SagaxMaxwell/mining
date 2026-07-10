# 数据挖掘教程项目

现代数据挖掘教程。只保留可运行、可维护的活跃内容。

## 内容

| 路径 | 说明 |
| --- | --- |
| `tutorials/explore/` | Polars 数据探索 |
| `tutorials/customers/` | 客户聚类画像 |
| `tutorials/basket/` | FP-Growth 购物篮分析 |
| `tutorials/forecast/` | 监督学习式时间序列预测 |
| `tutorials/common.py` | Notebook 公共函数 |
| `data/` | 教程数据 |
| `scripts/` | 校验脚本 |

## 运行

推荐 Python 3.11+ 和 `uv`：

```bash
uv sync
uv run jupyter lab
```

校验：

```bash
uv run ruff check scripts tutorials
uv run python scripts/validate.py
```

## 约定

- 每个教程含 `README.md` 和一个 notebook。
- 公共路径、绘图和指标放在 `tutorials/common.py`。
- 保留现代主线：Polars、HDBSCAN、FP-Growth、梯度提升。
- 不维护旧手写算法和经典统计时间序列教程。
