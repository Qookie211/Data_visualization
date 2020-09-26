import  matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif']=['SimHei']#统一指定
plt.rcParams['axes.unicode_minus']=False #显示负号
data = pd.read_csv('51job%25E7%2588%25AC%25E8%2599%25AB+20200924-195051.csv',encoding='gbk')
city = data['公司地点'].value_counts()
print(type(city))
# print(len(city))
label = city.keys()
print(label)
city_list = []
count = 0
n = 1
distance = []
for i in city:
    city_list.append(i)
    print('列表长度', len(city_list))
    count += 1
    if count > 5:
        n += 0.1
        distance.append(n)
    else:
        distance.append(0)
plt.pie(city_list, labels=label, labeldistance=1.2, autopct='%2.1f%%', pctdistance=0.6, shadow=True, explode=distance)
plt.axis('equal')  # 使饼图为正圆形
plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1))
plt.savefig('python地理位置分布图.jpg')
plt.show()