#CSV目录下，读取信息并绘制折线图
import matplotlib.pyplot as plt
import csv
from datetime import datetime
plt.rcParams['font.sans-serif']=['SimHei']#统一指定
plt.rcParams['axes.unicode_minus']=False #显示负号
fliename ='sitka_weather_07-2014.csv'

with open(fliename,'r') as f:
    reader = csv.reader(f)#CSV的阅读器，generater(生成器)
    header_row =next(reader)
    # print(header_row)Excel的表头 为列表
    max_temps =list()
    min_temps = list()
    dates = list()
    for row in reader:
        dates.append(datetime.strptime(row[0],"%Y-%m-%d"))
        max_temp =int(row[1])
        max_temps.append(max_temp)
        min_temps.append(int(row[3]))

fig = plt.figure(dpi=128,figsize=(10,6))
plt.fill_between(dates,max_temps,min_temps,facecolor='green',alpha=0.2)
plt.plot(dates,max_temps,c='red')
plt.plot(dates,min_temps,c='yellow')
plt.title('最高气温',fontsize=50)
plt.xlabel('日期',fontsize=50)
plt.ylabel('气温F',fontsize=50)
plt.tick_params(axis='both',which='major',labelsize=12)
#x轴是日期的话，可以使用画布tuofmt_date()函数
fig.autofmt_xdate()
plt.show()


# print(max_temps)