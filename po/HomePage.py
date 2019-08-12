
from common.Driver import Driver
from selenium.webdriver.common.by import By
import time

class HomePage(Driver):

    def __init__(self, driver):
        self.driver = driver

    # 封装页面元素属性
    first_page = (By.ID, 'com.ss.android.article.lite:id/axy') # 首页

    # 封装页面元素的操作方法
    def clickFirst(self):
        time.sleep(5)
        self.driver.find_element(*self.first_page).click()
        print('点击完成')
        time.sleep(10)
        return self.driver


if __name__ == '__main__':
    h = HomePage()
    h.clickFirst()




