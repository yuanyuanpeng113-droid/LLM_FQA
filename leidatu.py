import numpy as np
import matplotlib.pyplot as plt
from math import pi

# 设置字体为 Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 20

# 定义数据
labels = np.array(['C++', 'JavaScript', 'Java', 'Bash', 'C#', 'PHP'])
values1 = np.array([16.77, 24.22, 17.53, 11.90, 17.96, 27.33])
values2 = np.array([13.04, 26.08, 11.90, 8.70, 14.27, 22.36])
values3 = np.array([17.39, 26.98, 18.27, 16.43, 18.80, 29.12])

# 计算角度
num_vars = len(labels)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # 闭合图形
values1 = np.concatenate((values1, [values1[0]]))
values2 = np.concatenate((values2, [values2[0]]))
values3 = np.concatenate((values3, [values3[0]]))

# 创建图形
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# 绘制第一个数据集
ax.fill(angles, values1, color='blue', alpha=0.20, label='Normal(blue)')
ax.plot(angles, values1, color='blue', linewidth=2)

# 绘制第二个数据集
ax.fill(angles, values2, color='red', alpha=0.20, label='Analogical(red)')
ax.plot(angles, values2, color='red', linewidth=2)

# 绘制第三个数据集
ax.fill(angles, values3, color='green', alpha=0.20, label='test')
ax.plot(angles, values3, color='green', linewidth=2)

# 添加值标签
for i in range(num_vars):
    angle = angles[i]
    ax.text(angle + 0.2, values1[i] + 0.1, str(values1[i]), color='blue', ha='center', va='center')
    ax.text(angle, values2[i] + 0.1, str(values2[i]), color='red', ha='center', va='center')
    ax.text(angle - 0.2, values3[i] - 0.1, str(values3[i]), color='green', ha='center', va='center')

# 设置标签
ax.set_yticklabels([])

# 根据角度调整标签旋转角度
for i, label in enumerate(labels):
    angle_deg = np.degrees(angles[i])  # 将弧度转换为角度
    if angle_deg > 90 and angle_deg < 270:
        ax.text(angles[i], 1.05, label, ha='right', va='center', rotation=angle_deg + 180, color='black')
    else:
        ax.text(angles[i], 1.05, label, ha='left', va='center', rotation=angle_deg, color='black')

# 添加图例
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=3, fontsize=20)

plt.show()
