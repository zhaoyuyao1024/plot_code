import matplotlib.pyplot as plt
import numpy as np
xx1 = ['点眼前', '30s后', '2min后', '5min后']

# 基准坐标
x = np.arange(-0.1,3.9,1)
xx2 = np.arange(0,4,1)
xx3 = np.arange(0.1,4.1,1)
xx4 = np.arange(0.2,4.2,1)


# 各组均值和方差
mean1 = [537.5, 542.6, 541.2, 542]
var1 = [34.4, 35.6, 34.7, 35.5]

mean2 = [548, 554, 549.3, 548.1]
var2 = [28.3, 27.5, 27.9, 27.2]

mean3 = [551, 553.6, 554, 553.6]
var3 = [23.1, 22.3, 23.2, 23.5]

mean4 = [544.7, 547.6, 546.4, 545.6]
var4 =[27.5, 29.2, 28.4, 28.9]


d1=[]
d2=[]
d3=[]
d4=[]

p1=[]
p2=[]
p3=[]
p4=[]

m1=[]
m2=[]
m3=[]
m4=[]

n1=[]
n2=[]
n3=[]
n4=[]

# 第一组纵坐标
d1.append(mean1[0]+var1[0])
d1.append(mean1[0])
d1.append(mean1[0]-var1[0])

d2.append(mean1[1]+var1[1])
d2.append(mean1[1])
d2.append(mean1[1]-var1[1])

d3.append(mean1[2]+var1[2])
d3.append(mean1[2])
d3.append(mean1[2]-var1[2])

d4.append(mean1[3]+var1[3])
d4.append(mean1[3])
d4.append(mean1[3]-var1[3])

# 第二组纵坐标
p1.append(mean2[0]+var2[0])
p1.append(mean2[0])
p1.append(mean2[0]-var2[0])

p2.append(mean2[1]+var2[1])
p2.append(mean2[1])
p2.append(mean2[1]-var2[1])

p3.append(mean2[2]+var2[2])
p3.append(mean2[2])
p3.append(mean2[2]-var2[2])

p4.append(mean2[3]+var2[3])
p4.append(mean2[3])
p4.append(mean2[3]-var2[3])

# 第三组纵坐标
m1.append(mean3[0]+var3[0])
m1.append(mean3[0])
m1.append(mean3[0]-var3[0])

m2.append(mean3[1]+var3[1])
m2.append(mean3[1])
m2.append(mean3[1]-var3[1])

m3.append(mean3[2]+var3[2])
m3.append(mean3[2])
m3.append(mean3[2]-var3[2])

m4.append(mean3[3]+var3[3])
m4.append(mean3[3])
m4.append(mean3[3]-var3[3])

# 第四组纵坐标
n1.append(mean4[0]+var4[0])
n1.append(mean4[0])
n1.append(mean4[0]-var4[0])

n2.append(mean4[1]+var4[1])
n2.append(mean4[1])
n2.append(mean4[1]-var4[1])

n3.append(mean4[2]+var4[2])
n3.append(mean4[2])
n3.append(mean4[2]-var4[2])

n4.append(mean4[3]+var4[3])
n4.append(mean4[3])
n4.append(mean4[3]-var4[3])


# 第一组横坐标
x1 = [-0.1,-0.1,-0.1]
q1 = [0,0,0]
j1 = [0.1,0.1,0.1]
k1 = [0.2,0.2,0.2]

x2 = [0.9,0.9,0.9]
q2 = [1,1,1]
j2 = [1.1,1.1,1.1]
k2 = [1.2,1.2,1.2]

x3 = [1.9,1.9,1.9]
q3 = [2,2,2]
j3 = [2.1,2.1,2.1]
k3 = [2.2,2.2,2.2]

x4 = [2.9,2.9,2.9]
q4 = [3,3,3]
j4 = [3.1,3.1,3.1]
k4 = [3.2,3.2,3.2]


# plt.axis([0, 5, 0, 25])
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title('各分组中不同时间点的CCT值')
plt.xlabel('时间')
plt.ylabel('CCT(μm)')
labels = ['点眼前', '30s后', '2min后', '5min后']


# 第一组
plt.plot(x1, d1, color = '#054E9F', marker ='o')
plt.plot(x2, d2, color = '#054E9F',marker ='o')
plt.plot(x3, d3, color = '#054E9F',marker ='o')
plt.plot(x4, d4, color = '#054E9F',marker ='o')
plt.plot(x, mean1, color = '#054E9F',marker ='o', label='N1', linestyle = 'dashed')

# 第二组
plt.plot(q1, p1, color = '#FFA500', marker ='*',linewidth=2)
plt.plot(q2, p2, color = '#FFA500',marker ='*', linewidth=2)
plt.plot(q3, p3, color = '#FFA500',marker ='*', linewidth=2)
plt.plot(q4, p4, color = '#FFA500',marker ='*', linewidth=2)
plt.plot(xx2, mean2, color = '#FFA500',marker ='*', label='N2',linestyle = 'dashed', linewidth=2)

# 第三组
plt.plot(j1, m1, color = 'g', marker ='+')
plt.plot(j2, m2, color = 'g',marker ='+')
plt.plot(j3, m3, color = 'g',marker ='+')
plt.plot(j4, m4, color = 'g',marker ='+')
plt.plot(xx3, mean3, color = 'g',marker ='+', label='D1', linestyle = ':')

# 第四组
plt.plot(k1, n1, color = 'm', marker ='d',linewidth=2)
plt.plot(k2, n2, color = 'm',marker ='d', linewidth=2)
plt.plot(k3, n3, color = 'm',marker ='d', linewidth=2)
plt.plot(k4, n4, color = 'm',marker ='d', linewidth=2)
plt.plot(xx4, mean4, color = 'm',marker ='d', label='D2',linestyle = '-.', linewidth=2)


plt.xticks(np.arange(0,4), labels=labels)
# plt.yticks(np.arange(10, 25, 5))
plt.legend(loc='lower center')
plt.show()
