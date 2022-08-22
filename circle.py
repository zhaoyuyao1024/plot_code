import matplotlib.pyplot as plt
import numpy as np
# x = 0  # 圆心的x轴坐标
# y = 0  # 圆心的y轴坐标
# r1 = 2  # 圆的半径
# r2 = 1
fig = plt.figure(figsize=(6, 6))
# circle1 = plt.Circle((x, y), r1, color='black', fill=False)
# circle2 = plt.Circle((x, y), r2, color='black', fill=False)
# plt.gcf().gca().add_artist(circle1)
# plt.gcf().gca().add_artist(circle2)
plt.axis('equal')

angle = np.linspace(0, 2 * np.pi, 200)
x1 = np.cos(angle)
y1 = np.sin(angle)
x2 = 2 * np.cos(angle)
y2 = 2 * np.sin(angle)

plt.xlim(-4,4)
plt.ylim(-4,4)
plt.xticks(np.arange(-4, 4.5, 0.5))
plt.yticks(np.arange(-4, 4.5, 0.5))

plt.axvline(x=0, c='black', linewidth=0.5)
plt.axhline(y=0, c='black', linewidth=0.5)


area = 20
a = [-0.112889055,-0.523868339,-0.67711487,0.602508475,1.16231376,0.163185635,-1.217981447,-0.865060993,0.066878218,1.862647909,0.593561151,-0.032108201,0,-1.736379649,1.262313815,0.116545857,-0.378583543,-0.360322822,-0.659080514,-0.26937279,-0.551779304,-0.884980027,-0.247466357,-1.112588174,-1.562086318,0.568821342,-1.775446004,0.979071621,-0.350267067,-1.108704452]
b = [-0.221162889,-0.80772764,3.622204221,4.598525693,-1.41380696,3.395580101,0.376253143,-0.805194838,0.271415399,0.929075219,-0.810815573,1.150204559,0,-2.55372031,0.181989347,-0.027733144,-0.066354195,1.657954221,-3.484724436,3.280700761,-0.81775067,1.73208869,-0.657477009,-1.309409333,1.254617077,0.070911967,2.409057559,0.562236979,1.449003612,-0.052826205]
plt.plot(x1, y1, c='black', linewidth=0.5)
plt.plot(x2, y2, c='black', linewidth=0.5)
plt.scatter(a, b, s=area, c='none', marker='o', edgecolors='lightseagreen')
plt.show()

