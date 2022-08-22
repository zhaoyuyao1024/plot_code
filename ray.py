import matplotlib.pyplot as plt
import numpy as np

y1 = [0,0,-0.2,-0.1,-0.1,-0.4,0,0.1,-0.2,-0.1,-0.4,0.3,-0.3,-0.3,0.6,0.1,-0.1,-0.3,0,0,0.1,0.2,0.1,0,-0.1,0.2,-0.1,-0.1,-0.2,-0.2]

y2 = [0.2,-0.1,-0.2,-0.2,-0.1,-0.4,-0.1,0,0,0.2,-0.2,-0.2,-0.3,-0.3,0.6,-0.1,0,-0.3,-0.1,-0.1,0,0.1,0.1,0,0,0.2,-0.1,-0.3,-0.1,0]

y3 = [0.3,-0.1,-0.1,0,-0.1,0,0,-0.1,0,0.2,-0.1,0.1,-0.1,-0.3,0.5,-0.1,0,-0.2,0.2,0.1,0.1,0.1,0.1,0.1,0.1,0.2,-0.1,-0.1,-0.2,-0.2]


for i in range(30):
    plt.plot([0, 1], [0, y1[i]], color='black', linewidth=0.5)
for i in range(30):
    plt.plot([1, 2], [y1[i], y2[i]], color = 'black', linewidth=0.5)
for i in range(30):
    plt.plot([2, 3], [y2[i], y3[i]], color = 'black', linewidth=0.5)
plt.grid(linewidth=0.3)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
labels = ['术前', '30s', '2min', '5min']
plt.xticks(np.arange(0,4), labels=labels)
plt.ylim(-1,1)
plt.yticks(np.arange(-1, 1.2, 0.2))
plt.show()