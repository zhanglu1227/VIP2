from common.Driver import Driver
from selenium.webdriver.common.by import By
import time

class MyPage(Driver):

    def __init__(self, driver):
        self.driver = driver

    # 封装页面元素属性
    my_page = (By.ID, 'com.ss.android.article.lite:id/axy')  # 个人中心
    

    # 封装页面元素的操作方法
    def clickMypage(self):
        time.sleep(5)
        self.driver.find_element(*self.my_page).click()
        print('点击完成')
        time.sleep(10)
        return self.driver


if __name__ == '__main__':
    h = MyPage()
    h.clickMypage()