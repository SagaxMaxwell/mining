# 数据探索

用 Polars 完成缺失值、异常值、描述统计和相关性分析。

- Notebook：`explore.ipynb`
- 数据：`../../data/scores.csv`、`../../data/turnover.csv`

常用方法：`null_count()`、`all_horizontal()`、`describe()`、`pl.corr()`；异常值使用 IQR 边界判断。
