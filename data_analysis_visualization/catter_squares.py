import matplotlib.pyplot as plt

x_values = range(1, 1001) # (range-范围）
y_values = [x**2 for x in x_values] # 使用了列表解析（它遍历x的值for x in x_values计算其平方值（x**2）并将结果储存到列表y_values中
plt.style.use('seaborn')
plt.rcParams['font.sans-serif']=['Microsoft YaHei']#设置中文字体
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c= y_values, cmap= plt.cm.Blues, s=10)

# 设置图表标题并给坐标轴加上标签。
ax.set_title("平方数", fontsize=20)
ax.set_xlabel("值", fontsize=10)
ax.set_ylabel("值得平方", fontsize=10)

# 设置刻度标记的大小。
ax.tick_params(axis='both', which='major',  labelsize=8)

# 设置每个坐标的取值范围。
ax.axis([0, 1100, 0, 1100000])

# 打开Matplotlib 查看器并（show-显示）绘制的图表。
plt.show()
# [savefig('squares_plot.png', bbox_inches='tight ')]--(savefig-保存图表)