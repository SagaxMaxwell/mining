---
date created: 2026-07-10T11:11
date updated: 2026-10-26T13:06
---

# 客户聚类

比较 K-Means、HDBSCAN 与层次聚类，生成客户画像。

- Notebook：[[mining/tutorials/customers/customers.ipynb|运行示例]]
- 数据：`../../data/customers.csv`

流程：IQR 截尾 → `StandardScaler` → 肘部法/轮廓系数选型 → 输出聚类指标与画像。
