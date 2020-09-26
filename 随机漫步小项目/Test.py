import random
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']#统一指定
plt.rcParams['axes.unicode_minus']=False #显示负号
class randomWalk(object):
    def __init__(self,step_list=5000):
        #随机漫步的步数限制
        self.step_limit = step_list
        #用两个列表记录每步所在的位置x，y
        #原点开始
        self.x= [0]
        self.y= [0]
    def walk(self):
        while len(self.x)<self.step_limit:
            #决定x，y的方向
            x_dir = random.choice([-1,1])
            x_dist = random.choice(range(5))
            y_dir = random.choice([-1,1])
            y_dist = random.choice(range(5))
            #新的位置对于原位置的移动
            x_step =x_dir*x_dist
            y_step =y_dir*y_dist
            #0 全为原地踏步 not
            if (not x_step)and (not y_step):
                continue
            self.x.append(self.x[-1]+x_step)
            self.y.append(self.y[-1]+y_step)
if __name__ == '__main__':
    rw = randomWalk()
    rw.walk()
    plt.title('随机漫步图',fontsize=50)
    plt.scatter(rw.x,rw.y,s=12,c=rw.x,cmap=plt.cm.Greens,edgecolors='none')
    #起始位置
    plt.scatter(rw.x[0],rw.y[0],s=100,c='Red',edgecolors='none')
    #结束位置
    plt.scatter(rw.x[-1], rw.y[-1], s=100, c='Yellow', edgecolors='none')
    plt.xlabel('X',fontsize=12)
    plt.ylabel('Y',fontsize=12)
    plt.show()
    # print(rw.x)
    # print(rw.y)
