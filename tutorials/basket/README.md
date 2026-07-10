# 现代购物篮分析

## 用途

用 Polars 整理订单，用 FP-Growth 挖掘关联规则。

## 文件

- Notebook：`basket.ipynb`
- 数据：`../../data/orders.csv`、`../../data/items.csv`

## 方法

- `pl.read_csv(..., encoding="gbk")`
- `pivot()` 构建购物篮矩阵
- `fpgrowth()` 挖掘频繁项集
- `association_rules()` 生成规则
