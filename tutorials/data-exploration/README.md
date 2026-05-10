# 数据探索

## 学习目标

- 统计缺失值、全空列和全空行。
- 使用箱线图识别正态样本中的异常值。
- 对成绩数据计算描述性统计、极差、变异系数和四分位距。
- 对广告投入与销售额进行相关性分析和散点图展示。

## 文件

- Notebook：`data-exploration.ipynb`
- 数据：`../../data/scores.csv`、`../../data/turnover.csv`

## 关键方法

| 任务 | 推荐方法 |
| --- | --- |
| 缺失值统计 | `DataFrame.isna().sum()` |
| 全空列/行 | `DataFrame.isna().all()` |
| 描述性统计 | `DataFrame.describe()` |
| 相关系数矩阵 | `DataFrame.corr(numeric_only=True)` |
| 异常值边界 | `Q1 - 1.5 * IQR` 与 `Q3 + 1.5 * IQR` |
