import json
import multiprocessing

import multiprocess as multiprocess
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import re
import time
import xlwt

def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
            }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

book = xlwt.Workbook(encoding='utf-8', style_compression=0)

sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
sheet.write(0, 0, '名称')
sheet.write(0, 1, '图片')
sheet.write(0, 2, '排名')
sheet.write(0, 3, '评分')
sheet.write(0, 4, '作者')
sheet.write(0, 5, '简介')

n = 1
def save_to_excel(soup):
    list = soup.find(class_='grid_view').find_all('li')

    for item in list:
        item_name = item.find(class_='title').string
        item_img = item.find('a').find('img').get('src')
        item_index = item.find(class_='').string
        item_score = item.find(class_='rating_num').string
        item_author = item.find('p').text
        if (item.find(class_='inq') != None):
            item_intr = item.find(class_='inq').string
        # print('爬取电影：' + item_index + ' | ' + item_name +' | ' + item_img +' | ' + item_score +' | ' + item_author +' | ' + item_intr )
        print('爬取电影：' + item_index + ' | ' + item_name + ' | ' + item_score + ' | ' + item_intr)
        global n
        sheet.write(n, 0, item_name)
        sheet.write(n, 1, item_img)
        sheet.write(n, 2, item_index)
        sheet.write(n, 3, item_score)
        sheet.write(n, 4, item_author)
        sheet.write(n, 5, item_intr)
        n = n + 1

def parse_one_page(html):
    pattern = re.compile(
        '<li>.*?<em class="">(.*?)</em>.*?title.*?>(.*?)</span>.*? <span class="rating_num" property="v:average">(.*?)</span>.*?<span class="inq">(.*?)</span>',
        re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {'index': item[0],
               'title': item[1],
               'score': item[2],
               'comment': item[3]
               }


def write_to_file(content):
    with open('douban250.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(url):
    html = get_one_page(url)
    soup = BeautifulSoup(html, 'lxml')
    save_to_excel(soup)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    start =time.time()
    urls = []
    pool = multiprocessing.Pool(multiprocessing.cpu_count())#我们根据电脑 CPU 的内核数量创建相应的进程池
    for i in range(0, 10):
        url = 'https://movie.douban.com/top250?start=' + str(i * 25) + '&filter='
        urls.append(url)
    pool.map(main, urls)#通过 map 方法去执行我们的主函数将我们获得的 url 传过去
    pool.close()
    pool.join()#为的是让进程池的进程执行完毕再结束

book.save(u'豆瓣最受欢迎的250部电影.xlsx')
