import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#生成范例数据
r = 2 * np.random.rand(100) #生成100个服从“0~1”均匀分布的随机样本值
theta = 2 * np.pi * np.random.rand(100) #生成角度
area = 10
ax = plt.subplot(111, projection='polar') # 定义极坐标
#projection为画图样式，除'polar'外还有'aitoff', 'hammer', 'lambert'等
ax.scatter(theta, r, c='black', s=area, cmap='warm', alpha=1)
#ax.scatter为绘制散点图函数
plt.show()


