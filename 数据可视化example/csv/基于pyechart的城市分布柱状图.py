import  matplotlib as plt
import pandas as pd
from pyecharts.charts import Bar
plt.rcParams['font.sans-serif']=['SimHei']#统一指定
plt.rcParams['axes.unicode_minus']=False #显示负号
data = pd.read_csv('51job%25E7%2588%25AC%25E8%2599%25AB+20200924-195051.csv',encoding='gbk')
city = data['公司地点'].value_counts()
# keys = city.index  # 等价于keys = city.keys()
keys = city.keys()
values = city.values
bar = Bar()
bar.add_yaxis("工作地点", keys)
bar.render(path='a.html')