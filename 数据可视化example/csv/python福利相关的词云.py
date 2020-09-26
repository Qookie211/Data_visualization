import  matplotlib.pyplot as plt
import pandas as pd
import jieba
from wordcloud import WordCloud
plt.rcParams['font.sans-serif']=['SimHei']#统一指定
plt.rcParams['axes.unicode_minus']=False #显示负号
data = pd.read_csv('51job%25E7%2588%25AC%25E8%2599%25AB+20200924-195051.csv',encoding='gbk')
text =''
for line in data['公司待遇'].value_counts():
    print(type(line))
    if len(eval(line)) == 0:
        continue
    else:
        for word in eval(line):
            # print(word)
            text += word
cut_word = ','.join(jieba.cut(text))
cloud = WordCloud(
    font_path=r'C:\Windows\Fonts\simfang.ttf',
    background_color='black',
    max_words=500,
    max_font_size=100,
    width=400,
    height=800

)
word_cloud = cloud.generate(cut_word)
word_cloud.to_file('公司待遇.png')
plt.imshow(word_cloud)
plt.axis('off')
plt.show()