import os

import requests
from lxml import etree

# 获取页面的信息
def page_data(url):
    urls=[]
    headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
    }
    # 根据这个url，获取一列url
    for urlI in url:
        response = requests.get(urlI, headers=headers)
        response.encoding = 'gbk'
        response = response.text
        text = etree.HTML(response)
        ppturl = text.xpath('//ul[@class="arclist"]/li[@class="arclistbg1"]/a/@href')
        print(ppturl)
        if len(ppturl) >0:
            urls = [] #清空数组
            for i in ppturl[:3]:
                urls.append("http://www.1ppt.com/" + i)
            print('可访问的url:' + str(urls))
            for new_url in urls:
                new_page = requests.get(new_url, headers=headers)
                new_page.encoding = 'gbk'
                new_page = new_page.text
                detail = etree.HTML(new_page)
                if len(detail.xpath('//ul[@class="downurllist"]/li/a/@href')[0]):
                    down = detail.xpath('//ul[@class="downurllist"]/li/a/@href')[0]
                    title = detail.xpath("//div[@class='ppt_info clearfix']/h1/text()")[0]
                    # 文件名以书名号进行划分
                    file_name = str(title).split('《')[1].split('》')[0]
                    print(file_name)
                    # 解决乱码
                    print(title)
                    down_doc = requests.get(down, headers=headers).content
                    if not os.path.isdir(r'D:\PPTDetail\\' + file_name):  # 判断有无此目录，两个\\，第一个\转义了第二个\
                        os.mkdir(r'D:\PPTDetail\\' + file_name)  # 若无，创建此目录。
                    with open("D:\PPTDetail\\" + file_name + '\\' + title, "ab")as f:
                        f.write(down_doc)
                        print(title + "爬取成功！！！")
                    down_doc = requests.get(down, headers=headers).content
                else:
                    print("有一个网页。。没有下载链接")
                    print(detail)

        else:
            print("当前列表为空，爬取不到下一个网址")
def get_urls():
    # 第一模板网下需要的爬取的起始目录
    page_url = 'http://www.1ppt.com/kejian/14324.html'
    content = requests.get(page_url).content
    page_html = etree.HTML(content)
    # 获得目录网页需要的所有网址
    url = page_html.xpath("//div[@class='content']/dl[@class='kjmulu']/dd/span/a/@href")
    print(url)
    page_data(url)
    print("所有的ppt模板爬取成功了")


if __name__ == '__main__':
    get_urls()
