
import numpy as np
#产生一个数组，元素取值范围【1,10】
arr = np.arange(1,10)
print(type(arr))#<class 'numpy.ndarray'>
print(arr)

r= range(1,10)
arr1 = np.array(r)#工厂函数aarray产生不同对象
arr2 = np.asarray(r) #asarry同一个对象

list = [
    [1,2,3,4],
    [5,6,7,8]
]
#产生二维数组
arr3 = np.array(list)
print(arr3)
print(type(arr3))

arr4 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])
for ele in arr4:
    print(ele)#[1 2 3 4]
              #[5 6 7 8]
for ele1 in arr4.tolist():
    print(ele1)
    # [1, 2, 3, 4]
    # [5, 6, 7, 8]
list1 = [range(10),range(10)]
arr=np.array(list1)


#产生随机数组
r_number = np.random.rand()#产生一个随机数0-1
print(r_number)

r_arr = np.random.rand(3,3)#产生3*3的数组
print(r_arr)

r_arr1 = np.random.randn(2,2)#产生2*2的正态分布
print(r_arr1)

r_int = np.random.randint(1,5)#产生一个随机整数
print(r_int)

arr_int = np.random.randint(1,4,5)#一维随机整数
print(arr_int)

arr_int2=np.random.randint(1,5,size=(2,2))
print(arr_int2)#产生二维随机整数组

arr_float = np.random.random_sample(((5,5)))#元组表示
print(arr_float)

#随机取数：np.random.choice(5,2) 0-5  取2个数replace=false 不同值
#np.random.choice(数组，取数，p=[数组里每个值被取得的概率])
#np.random.shuffile(数组) 打乱数据 数组本身已经乱了


#等差数列
print(np.linspace(1,100,20))#99/19
# 特殊数组：
# 	全0数组 np.zeors np.zeors_like
# 	全1数组 np.ones np.ones_like
# 	空  np.empty np.empty_like
# 	对角线全1 np.eye,np.identity
# 		区别：np.eye 可以不是方正，可以指定对角线方向，np.idenity只能是方阵
#数组 属性  ndim（维度数） shape（几乘几的数组 返回的是元组 dtype属性）





