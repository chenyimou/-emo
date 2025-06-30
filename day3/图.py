# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 设置随机种子保证结果可重现
np.random.seed(35)

# 生成日期数据
year = np.arange(2000, 2021).astype(str)
month = np.random.randint(1, 13, size=20).astype(str)
day = np.random.randint(1, 31, size=20).astype(str)

# 使用列表推导式高效创建日期字符串
date = [f"{y}/{m}/{d}" for y, m, d in zip(year, month, day)]

# 生成随机销量数据
sales = np.random.randint(500, 2000, size=len(date))

# 创建图形
plt.figure(figsize=(12, 6))

# 绘制折线图
plt.plot(date, sales, marker='o', linestyle='-', color='blue', linewidth=2)

# 设置横坐标标签（每隔2个日期显示一个）
# 使用格式化的日期字符串，添加"日期："前缀
tick_labels = [f"日期: {d}" for d in date[::2]]
plt.xticks(range(0, len(date), 2), tick_labels, rotation=45, color='red')

# 设置纵坐标标签
plt.ylabel('销量', fontsize=12)

# 添加标题
plt.title('2000-2019年销量变化趋势', fontsize=14, pad=20)

# 添加网格线
plt.grid(True, linestyle='--', alpha=0.7)

# 自动调整布局防止标签被裁剪
plt.tight_layout()

# 显示图形
plt.show()