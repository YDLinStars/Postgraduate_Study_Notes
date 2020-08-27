from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait

chrome_driver = 'D:\pythonEdit\chromedriver_win32\chromedriver.exe'  # chromedriver的文件位置
browser = webdriver.Chrome(executable_path=chrome_driver)
WAIT = WebDriverWait(browser, 10)
browser.set_window_size(1400, 900)

def search():
    try:
        browser.get('https://www.bilibili.com/')
        #等到这个元素可操作的时候才会继续执行下一步
        input = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#nav_searchform > input")))
        submit = WAIT.until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div/div[2]/div/form/div/button')))

        input.send_keys('蔡徐坤 篮球')
        submit.click()

        # 跳转到新的窗口
        print('跳转到新窗口')
        all_h = browser.window_handles
        browser.switch_to.window(all_h[1])
        get_source()

        total = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                       "#all-list > div.flow-loader > div.page-wrap > div > ul > li.page-item.last > button")))
        return int(total.text)
    except TimeoutException:
        return search()
    # time.sleep(5)
    # b.quit()
def next_page(page_num):
    try:
        print('获取下一页数据')
        next_btn = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                          '#all-list > div.flow-loader > div.page-wrap > div > ul > li.page-item.next > button')))
        next_btn.click()
        WAIT.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,
                                                     '#all-list > div.flow-loader > div.page-wrap > div > ul > li.page-item.active > button'),
                                                    str(page_num)))
        get_source()
    except TimeoutException:
        browser.refresh()
        return next_page(page_num)

def get_source():
    WAIT.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#all-list > div.flow-loader > div.filter-wrap')))

    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
    print('到这')



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