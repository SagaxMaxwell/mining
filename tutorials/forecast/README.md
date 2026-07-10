# 现代时间序列预测

## 用途

把日温度序列转成监督学习数据，用梯度提升预测未来 30 天。

## 文件

- Notebook：`forecast.ipynb`
- 数据：`../../data/temperature.csv`

## 方法

- Polars 滞后、滚动、周期特征
- `TimeSeriesSplit`
- `HistGradientBoostingRegressor`
- 置换重要性
