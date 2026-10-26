---
date created: 2026-07-10T11:11
date updated: 2026-10-26T13:06
---

# 购物篮分析

用 Polars 整理订单，用 FP-Growth 挖掘关联规则。

- Notebook：[[mining/tutorials/basket/basket.ipynb|运行示例]]
- 数据：`../../data/orders.csv`、`../../data/items.csv`

关键步骤：`read_csv(…, encoding="gbk")` → `pivot()` 构建购物篮矩阵 → `fpgrowth()` → `association_rules()`。
