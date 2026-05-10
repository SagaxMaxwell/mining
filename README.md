# 数据挖掘教程项目

本项目将原始实验材料整理为可复用的数据挖掘教程。活跃教程统一放在 `tutorials/`，数据集统一放在 `data/`，原始 Word 与 Notebook 材料保存在 `archive/original/` 以便追溯。

## 目录结构

| 路径 | 说明 |
| --- | --- |
| `data/` | 教程使用的数据集，文件名统一使用小写和下划线 |
| `tutorials/environment-setup/` | Python、Conda 与 Jupyter 环境准备 |
| `tutorials/data-exploration/` | 数据探索、缺失值、异常值和描述性统计 |
| `tutorials/customer-segmentation/` | 商场客户聚类与人群画像 |
| `tutorials/association-rules/` | 从零实现 Apriori 关联规则 |
| `tutorials/market-basket-analysis/` | 商品购物篮分析与 mlxtend 实践 |
| `tutorials/time-series-arima/` | 牛奶产量 ARIMA 时间序列预测 |
| `tutorials/temperature-autoregression/` | 日温度 AutoReg 自回归预测 |
| `archive/original/` | 原始实验报告和旧 Notebook |
| `scripts/` | 项目维护脚本 |

## 快速开始

建议使用 Python 3.10 或更高版本。

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
jupyter lab
```

Windows PowerShell 可使用：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .
jupyter lab
```

## 教程风格约定

- 每个模块都包含 `README.md` 和一个可运行的 Notebook。
- Notebook 按「目标、数据、方法、代码、结果解释」组织。
- Python 代码统一使用清晰变量名、固定随机种子、稳定数据路径和函数封装。
- 图表代码统一使用 `matplotlib`，中文字体配置集中在 Notebook 开头。
- 回归任务使用 MAE、RMSE、MAPE 等指标；聚类任务使用轮廓系数、Calinski-Harabasz 等指标。

## 维护

教程内容应逐个文件维护，避免用批处理脚本覆盖人工调整。提交前可运行静态检查：

```bash
python scripts/validate_tutorials.py
```
