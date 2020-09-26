import  matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif']=['SimHei']#统一指定
plt.rcParams['axes.unicode_minus']=False #显示负号
data = pd.read_csv('51job%25E7%2588%25AC%25E8%2599%25AB+20200924-195051.csv',encoding='gbk')
data['工作薪资'].value_counts()
plt.hist(str(data['工作薪资']),bins=8,facecolor='Red',edgecolor='blue')
plt.xlabel('工作薪资（单位/元）')
plt.ylabel('频数')
plt.title('python职位薪资直方图')
plt.savefig('python薪资.jpg')
plt.show()
