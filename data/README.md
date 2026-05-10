# 数据集说明

| 文件 | 编码 | 主要用途 |
| --- | --- | --- |
| `mall_customers.csv` | UTF-8 | 客户聚类与消费画像 |
| `menu_orders.xls` | GBK/Excel | 小型菜单订单，用于手写 Apriori |
| `goods_order.csv` | GBK | 商品订单明细，用于购物篮分析 |
| `goods_types.csv` | GBK | 商品与类别映射 |
| `milk_production.csv` | UTF-8 | 月度牛奶产量时间序列 |
| `daily_temperature.csv` | UTF-8 | 日温度时间序列 |
| `scores.csv` | UTF-8 | 成绩描述性统计 |
| `turnover.csv` | UTF-8 | 广告投入与销售额相关分析 |
| `watermelon.csv` | UTF-8 | 分类算法示例数据 |
| `air_data.csv` | GBK | 航空客户价值分析示例数据 |
| `java_scores.csv` | UTF-8 | Java 成绩练习数据 |

读取中文或 GBK 编码数据时，请显式传入 `encoding="gbk"`，避免不同系统默认编码导致报错。
