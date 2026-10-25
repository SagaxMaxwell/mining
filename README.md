# 数据挖掘教程

可运行的现代数据挖掘示例，统一使用 Python + uv。

## 教程

- `tutorials/explore/`：Polars 数据探索
- `tutorials/customers/`：客户聚类画像
- `tutorials/basket/`：FP-Growth 购物篮分析
- `tutorials/forecast/`：梯度提升时间序列预测

公共函数在 `tutorials/common.py`，数据在 `data/`。

```bash
uv sync
uv run jupyter lab
uv run ruff check scripts tutorials
uv run python scripts/validate.py
```

每个教程包含 `README.md` 和 notebook。数据文件的编码以 `data/README.md` 为准。
