from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

browser = webdriver.ChromeOptions()
browser.binary_location = r"D:\Users\picc\AppData\Roaming\360se6\Application\360se.exe"  #这里是360安全浏览器的路径
browser.add_argument(r'--lang=zh-CN') # 这里添加一些启动的参数
browser = webdriver.Chrome(options=browser)
try:
    browser.get("https://www.baidu.com")
    input = browser.find_element_by_id("kw")
    input.send_keys("尤克里里跟吉他的区别")
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, "content_left")))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
    time.sleep(10)
finally:
    pass
    # browser.close()
    