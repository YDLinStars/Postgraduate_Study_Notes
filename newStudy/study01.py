#导入词云的包
from wordcloud import WordCloud
#导入matplotlib作图的包
import matplotlib.pyplot as plt

#读取文件,返回一个字符串，使用utf-8编码方式读取，该txt文本文件位于此python同以及目录下
#注意：该txt文本文件必须是utf-8编码
f = open(u'NINETEEN EIGHTY-FOUR.txt','r',encoding='utf-8').read()
#生成一个词云对象
wordcloud = WordCloud(
        background_color="white", #设置背景为白色，默认为黑色
        font_path='C:/Windows/Fonts/simkai.ttf',  #中文处理，用系统自带的字体
        width=1500,              #设置图片的宽度
        height=960,              #设置图片的高度
        margin=10               #设置图片的边缘
        ).generate(f)
# 绘制图片
plt.imshow(wordcloud)
# 消除坐标轴
plt.axis("off")
# 展示图片
plt.show()
# 保存图片
wordcloud.to_file('english_ciyun.png')
