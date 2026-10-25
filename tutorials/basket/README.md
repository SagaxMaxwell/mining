# 购物篮分析

用 Polars 整理订单，用 FP-Growth 挖掘关联规则。

- Notebook：`basket.ipynb`
- 数据：`../../data/orders.csv`、`../../data/items.csv`

关键步骤：`read_csv(..., encoding="gbk")` → `pivot()` 构建购物篮矩阵 → `fpgrowth()` → `association_rules()`。
