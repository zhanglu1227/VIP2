

from appium import webdriver
import time,os

class Driver(object):

    def startup(self):
        print('启动app')

        desired_caps = {

            "deviceName": "emulator-5554",
            "platformName": "Android",
            "platformVersion": "6.0.1",
            # "app": "/Users/cola/Desktop/news_article_lite_tt_lite_hb_lite-dsp-xz-and11_v7.0.7_3a56adb.apk",
            "appPackage": "com.ss.android.article.lite",
            "appActivity": "com.ss.android.article.lite.activity.SplashActivity",
            "noReset": True,
            "unicodeKeyboard": True,
            "resetKeyboard": True

        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        print('已经启动，等待6s中。。。')

        time.sleep(6)
        print('等待6s完成')
        return self.driver


if __name__ == '__main__':
    d = Driver()
    d.startup()

