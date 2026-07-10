# 现代数据探索

## 用途

用 Polars 做缺失值、异常值、描述统计和相关性分析。

## 文件

- Notebook：`explore.ipynb`
- 数据：`../../data/scores.csv`、`../../data/turnover.csv`

## 方法

| 任务 | 推荐方法 |
| --- | --- |
| 缺失值统计 | `Series.null_count()` |
| 全空列/行 | `pl.all_horizontal()` |
| 描述性统计 | `DataFrame.describe()` |
| 相关系数 | `pl.corr()` |
| 异常值 | IQR 边界 |
