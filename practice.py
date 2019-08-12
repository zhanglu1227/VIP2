

# 引入appium包

from appium import webdriver

def startup():

    desired_capabilities={

        "deviceName": "emulator-5554",
        "platformName": "Android",
        "platformVersion": "6.0.1",
        "app": "/Users/cola/Desktop/kaishujianggushiv5.4.1_downcc.com.apk",
        "appPackage": "com.ks.kaishustory",
        "appActivity": "com.ks.kaishustory.pages.firstenter.FirstActivity",
        "noReset": True,
        "unicodeKeyboard": True,
        "resetKeyboard": True

    }

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=desired_capabilities)

    # 清除搜索输入框
    driver.find_element_by_id('com.ss.android.article.lite:id/adg').clear()
    print('clear')
    # 输入要搜索的内容
    driver.find_element_by_id('com.ss.android.article.lite:id/qp').send_keys('哪吒')
    print('send_keys')
    # 点击搜索
    driver.find_element_by_id('com.ss.android.article.lite:id/qq').click()
    print('click')

    # 如果获取多个元素，则需要用find_elements
    driver.find_elements_by_id('')
    idList[0].click()

    driver.find_elements_by_id()[0]


startup()