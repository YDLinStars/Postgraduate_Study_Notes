import requests
from lxml import etree
import time
import os
from sendEmail import email
 
while True:
    # 博主名字
    author_name = input("请输入博主的名字: ")
    # 博主博文页数
    page_num = int(input("请输入博客页数: "))
    url = "https://blog.csdn.net/"+author_name+"/article/list/"+str(page_num)  #目标跟踪网页
    content = requests.get(url).content
    html = etree.HTML(content)
    # 博客文章的标题
 
 
    # 博客文章的标题
    title = html.xpath("//div[@class='article-item-box csdn-tracking-statistics']/h4/a/text()") #取0为空 暂时不清粗为什么
    csdn_article_url = html.xpath("//div[@class='article-item-box csdn-tracking-statistics']//h4//a/@href")[0]
    # 处理换行问题
    csdn_article_title = []
    for i in range(0, len(title)):
        csdn_article_title.append(title[i].strip())
    while "" in csdn_article_title:
        csdn_article_title.remove("")
 
    #获取第一篇文章标题
    print("当前的标题为:%s"%csdn_article_title[0]) #取第一个
    print("当前的链接为:%s" %csdn_article_url)
    #屏幕打印获取的第一篇文章标题
 
    #文件打印 转换为字符换类型
    csdn_article_title[0]=str(csdn_article_title[0])
    csdn_article_url=str(csdn_article_url)
 
    if not os.path.isfile("D:\\title_temp.txt"):
    #判断title_temp.txt文件是否存在，不存在则创建，并写入获取的第一篇文章标题
        f = open("D:\\title_temp.txt", "w")
        f.write(csdn_article_title[0])
        f.write(csdn_article_url)
        print("将当前标题、url记录在D:\title_temp.txt中，等待检测")
        f.close()
    else:
    #title_temp.txt文件存在的话，提取里面标题，和获取的标题对比
        with open("D:\\title_temp.txt", "r+") as f:
            old_url = f.read()
            if old_url !=csdn_article_url:
            #如果读取内容和获取的网站第一篇文章标题不一致，则表明网站更新
                #email(csdn_article_title[0],csdn_article_url)#发送qq邮件
                f.seek(0)
                f.truncate()
                print("网站有更新，需通知")
                f.write(csdn_article_title[0])
                f.write(csdn_article_url)
                #写入最新的标题内容，方便下一次比对
                break
                #退出循环
            else:
            #否则的话，表明网站没有更新
                print("网站暂时没有更新\n")
    time.sleep(5)
    #检测网页内容时间间隔，单位为秒（s）
