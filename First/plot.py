import matplotlib

#绘制一个plot折线图,取别名plt
import  matplotlib.pyplot as plt
# %matplotlib inline
#绘制y = x^2 (x,1,2,3,4...)/列表自身具有索引【0....】/数据为列表
squares = [x**2 for x in range(1,10)]
#绘图/
# plt.plot(squares)
# plt.show()
#改变线条的样式，线条的粗细linewidth
plt.plot(squares,linewidth=2)
plt.show()
#给图标题标题大小 fontsize，图中写中文：方法属性 fontproperties="Sim_"
plt.title('我',fontproperties="SimHei")
plt.show()
#在图中有中文2:统一指定字体
plt.rcParams['font.sans-serif']=['SimHei']#统一指定
plt.rcParams['axes.unicode_minus']=False #显示负号

#x轴，y轴 写法：
plt.xlabel('数字',fontsize=12)
plt.ylabel('平方',fontsize=12)
plt.show()

