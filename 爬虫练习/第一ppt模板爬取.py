import requests
from lxml import etree
def page_data(url):
    urls=[]
    headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
    }
    response=requests.get(url,headers=headers).text
    text=etree.HTML(response)
    url=text.xpath('//ul[@class="tplist"]/li/a/@href')
    for i in url:
        urls.append("http://www.1ppt.com/"+i)

    for new_url in urls:
        new_page=requests.get(new_url,headers=headers).text
        detail=etree.HTML(new_page)
        down=detail.xpath('//ul[@class="downurllist"]/li/a/@href')[0]
        title=down.split("/")[-1]
        down_doc=requests.get(down,headers=headers).content
        with open("模板存放/"+title,"ab")as f:
            f.write(down_doc)
            print(title+"爬取成功！！！")
def get_urls():
    for i in range(1,4):
        url="http://www.1ppt.com/moban/guoqingjie/ppt_guoqingjie_{}.html".format(i)
        page_data(url)
    print("所以的ppt模板爬取成功了")


if __name__ == '__main__':
    get_urls()
