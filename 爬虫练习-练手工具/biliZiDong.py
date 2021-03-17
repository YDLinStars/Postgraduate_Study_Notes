from selenium import webdriver
#配置google驱动
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_driver = 'D:\pythonEdit\chromedriver_win32\chromedriver.exe'  # chromedriver的文件位置
browser = webdriver.Chrome(executable_path=chrome_driver)
#等到这个元素可操作的时候才会继续执行下一步，时间为10秒
WAIT = WebDriverWait(browser, 10)
#浏览器的窗口
browser.set_window_size(1400, 900)
print('开始访问b站....')
browser.get("https://www.bilibili.com/")
username = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, "帐号的selector")))
password = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, "密码的selector")))
submit = WAIT.until(EC.element_to_be_clickable((By.XPATH, '按钮的xpath')))

username.send_keys('你的帐号')
password.send_keys('你的密码')
submit.click()