import matplotlib.pyplot as plt
#在图中有中文2:统一指定字体
plt.rcParams['font.sans-serif']=['SimHei']#统一指定
plt.rcParams['axes.unicode_minus']=False #显示负号
#散点图scatter
plt.scatter(5,5)
plt.show()
#指定点大小 s=
plt.scatter(5,5,s=300)
plt.show()
#x轴 plt.xlabel y轴plt.ylabel
plt.xlabel('x')
plt.ylabel('y')
plt.show()
#设置坐标上的刻度
plt.scatter(6,6)
plt.tick_params(axis='both',which='major',labelsize=12)
plt.show()
#颜色设置：设置在scatter里面
#边颜色：
# edgecolor='none',c='red'
#颜色变化：c=y(c接近y变化),cmap=plt.cm.Reds
#指定x，y轴的范围设置:
plt.axis([0,1000,0,11000])


#example：
x= range(1,21)
y = [val**2 for val in x]
plt.scatter(x,y,s=50)
plt.title('平方数',fontsize=50)
plt.xlabel('x',fontsize=12)
plt.ylabel('y',fontsize=12)
plt.tick_params(axis='both',which='major',labelsize=12)
plt.show()
