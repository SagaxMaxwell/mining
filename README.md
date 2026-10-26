---
date created: 2026-07-10T11:11
date updated: 2026-10-26T11:44
---
# 数据挖掘教程

使用 Python 与 Notebook 完成数据探索、聚类、关联规则和预测。

## 教程

- [[tutorials/explore/explore.ipynb|Polars 数据探索]]
- [[tutorials/customers/customers.ipynb|客户聚类画像]]
- [[tutorials/basket/basket.ipynb|购物篮分析]]
- [[tutorials/forecast/forecast.ipynb|时间序列预测]]

## 运行

在 `mining` 根目录执行，打开教程后从上到下运行单元。

```bash
uv sync
uv run jupyter lab
```

每篇教程包含所需的初始化与函数，可独立运行，无需加载其他 Notebook。数据编码见 [[mining/data/README|数据说明]]。
