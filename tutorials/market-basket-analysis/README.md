# 商品购物篮分析

## 学习目标

- 对商品订单明细进行独热编码。
- 分析热销商品和热销品类。
- 使用 Apriori 与 FP-Growth 挖掘频繁项集。
- 生成并筛选关联规则。

## 文件

- Notebook：`market-basket-analysis.ipynb`
- 数据：`../../data/goods_order.csv`、`../../data/goods_types.csv`

## 代码优化点

- 使用 `pd.crosstab()` 构建布尔购物篮矩阵，比手工 `get_dummies()` 后求和更直观。
- 将关联规则生成封装为兼容函数，降低 `mlxtend` 版本差异影响。
- 商品级和品类级分析使用同一套函数和输出格式。
