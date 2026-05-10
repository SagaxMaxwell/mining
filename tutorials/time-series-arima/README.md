# 牛奶产量 ARIMA 预测

## 学习目标

- 将月度数据转换为稳定的时间序列索引。
- 使用 ADF 检验判断平稳性，使用 Ljung-Box 检验判断白噪声。
- 通过差分阶数和 BIC 网格搜索选择 ARIMA 参数。
- 预测最后 6 个月产量并计算误差指标。

## 文件

- Notebook：`milk-production-arima.ipynb`
- 数据：`../../data/milk_production.csv`

## 代码优化点

- 不再硬编码 `ARIMA(4, 2, 7)`，改为根据 BIC 自动选择。
- 使用 `forecast()` 预测测试集长度，避免日期字符串兼容问题。
- 误差指标统一输出 MAE、RMSE、MAPE。
