# coding=utf-8
import re
import urllib.request
import urllib

account = "qq_37457202"  # 输入你的账号

url = "https://blog.csdn.net/" + account + "/article/list/"
t = 0
read_num = 0
mark_num = 0
while 1:
    t += 1
    url_s = url + str(t)
    content = urllib.request.urlopen(url_s).read()
    content = content.decode('utf-8')
    print(content)
    num = re.findall(r'<span class="read-num">(阅读数.*?)</span>', content)  #获取阅读数
    if len(num) <= 0:
        break
    for i in num:
        read_num += int(re.findall('(\d+)', i)[0])
    mark = re.findall(r'<span class="read-num">(评论数.*?)</span>', content)  #获取评论数
    for i in mark:
        mark_num += int(re.findall('(\d+)', i)[0])
print("阅读数: " + str(read_num))
print("评论数: " + str(mark_num))
