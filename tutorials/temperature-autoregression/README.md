# 日温度 AutoReg 预测

## 学习目标

- 使用日温度数据构建自回归模型。
- 通过 BIC 自动选择滞后阶数。
- 预测最后 30 天温度并评估误差。
- 区分回归任务和分类任务的评价指标。

## 文件

- Notebook：`temperature-autoregression.ipynb`
- 数据：`../../data/daily_temperature.csv`

## 代码优化点

- 移除旧代码中不适用于回归的 `accuracy`、`precision`、`recall`、`f1`。
- 使用 `AutoReg(..., old_names=False)` 并封装滞后阶数搜索。
- 输出预测表和误差指标，便于报告复用。
