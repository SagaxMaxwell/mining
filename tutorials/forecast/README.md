# 时间序列预测

把日温度序列转换为监督学习数据，用梯度提升预测未来 30 天。

- Notebook：`forecast.ipynb`
- 数据：`../../data/temperature.csv`

流程：生成滞后、滚动和周期特征 → `TimeSeriesSplit` → `HistGradientBoostingRegressor` → 置换重要性分析。
