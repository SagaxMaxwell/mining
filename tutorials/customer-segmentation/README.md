# 商场客户聚类

## 学习目标

- 完成缺失值处理、异常值截尾和标准化。
- 使用肘部法和轮廓系数辅助选择 K-Means 的 `k` 值。
- 比较 K-Means、DBSCAN 和层次聚类结果。
- 基于聚类结果形成可解释的客户画像。

## 文件

- Notebook：`customer-segmentation.ipynb`
- 数据：`../../data/mall_customers.csv`

## 代码优化点

- 使用 `Path` 自动定位项目根目录，避免相对路径失效。
- 将异常值处理封装为 `cap_outliers_iqr()`，避免把整行错误赋值为均值。
- K-Means 固定 `random_state` 和 `n_init`，保证结果可复现。
- 聚类评估统一输出为表格，避免散落的 `print()`。
