# 环境准备

## 学习目标

- 安装并理解 Anaconda、Conda、Jupyter Lab 与 Notebook 的关系。
- 掌握创建、激活、导出和删除虚拟环境的常用命令。
- 能在 Jupyter 中使用 Markdown 组织实验记录。
- 能为教程项目安装统一依赖。

## 推荐环境

本项目建议使用 Python 3.10 到 3.12。Python 3.13+ 在部分科学计算库上可能遇到二进制包兼容问题。

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
jupyter lab
```

Windows PowerShell：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .
jupyter lab
```

## Conda 常用命令

```bash
conda create -n mining python=3.10
conda activate mining
pip install -e .
python -m ipykernel install --user --name mining --display-name "Python (mining)"
conda deactivate
conda remove -n mining --all
```

## Markdown 记录规范

- 使用 `#`、`##`、`###` 建立层级，不用加粗模拟标题。
- 代码块统一标注语言，例如 ```` ```python ```` 或 ```` ```bash ````。
- 实验结果用表格、短段落和图表说明，不堆叠截图。
- 每个 Notebook 保留可复现的数据路径、随机种子和关键参数。
