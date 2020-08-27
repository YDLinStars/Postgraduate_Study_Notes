from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import xlwt

#配置google驱动
chrome_driver = 'D:\pythonEdit\chromedriver_win32\chromedriver.exe'  # chromedriver的文件位置
browser = webdriver.Chrome(executable_path=chrome_driver)
#等到这个元素可操作的时候才会继续执行下一步，时间为10秒
WAIT = WebDriverWait(browser, 10)
#浏览器的窗口
browser.set_window_size(1400, 900)

#ECCEL格式
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
#EXCEL名称与题目
sheet = book.add_sheet('请回答1988', cell_overwrite_ok=True)
sheet.write(0, 0, '名称')
sheet.write(0, 1, '地址')
sheet.write(0, 2, '描述')
sheet.write(0, 3, '观看次数')
sheet.write(0, 4, '弹幕数')
sheet.write(0, 5, '发布时间')
#全局变量Excel条数
n = 1

#搜索内容
def search():
    try:
        print('开始访问b站....')
        browser.get("https://www.bilibili.com/")

        # 被那个破登录遮住了
        # index = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#primary_menu > ul > li.home > a")))
        # index.click()

        #等到这个元素可操作的时候才会继续执行下一步
        input = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#nav_searchform > input")))
        #获取提交的标签
        submit = WAIT.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div/div[2]/div/form/div/button')))

        input.send_keys('请回答1988')
        submit.click()

        # 跳转到新的窗口
        print('跳转到新窗口')
        #当前窗口第一页的全部数据
        all_h = browser.window_handles
        browser.switch_to.window(all_h[1])
        get_source()

        #获取总页数
        total = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                           "#all-list > div.flow-loader > div.page-wrap > div > ul > li.page-item.last > button")))
        return int(total.text)
    except TimeoutException:
        return search()


def next_page(page_num):
    try:
        print('获取下一页数据')
        #下一页的按钮
        next_btn = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                          '#all-list > div.flow-loader > div.page-wrap > div > ul > li.page-item.next > button')))
        next_btn.click()
        #直到页数被点击
        WAIT.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,
                                                     '#all-list > div.flow-loader > div.page-wrap > div > ul > li.page-item.active > button'),
                                                    str(page_num)))
        get_source()
    except TimeoutException:
        browser.refresh()
        return next_page(page_num)

#将数据存到Excel
def save_to_excel(soup):
    list = soup.find(class_='video-list clearfix').find_all(class_='video-item matrix')

    for item in list:
        item_title = item.find('a').get('title')
        item_link = item.find('a').get('href')
        item_dec = item.find(class_='des hide').text
        item_view = item.find(class_='so-icon watch-num').text
        item_biubiu = item.find(class_='so-icon hide').text
        item_date = item.find(class_='so-icon time').text

        print('爬取：' + item_title)

        global n

        sheet.write(n, 0, item_title)
        sheet.write(n, 1, item_link)
        sheet.write(n, 2, item_dec)
        sheet.write(n, 3, item_view)
        sheet.write(n, 4, item_biubiu)
        sheet.write(n, 5, item_date)

        n = n + 1


def get_source():
    #等到这个元素可操作的时候才会继续执行下一步
    WAIT.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#all-list > div.flow-loader > div.filter-wrap')))
    #上述元素之后获剩余的HTML
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
    print('到这')

    save_to_excel(soup)


def main():
    try:
        total = search()
        print(total)

        for i in range(2, int(total + 1)):
            next_page(i)

    finally:
        browser.close()


if __name__ == '__main__':
    main()
    book.save('请回答1988.xlsx')