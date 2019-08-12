from common.MyTest import MyTest
from po.MyPage import MyPage

class Mtest(MyTest):

    def testmine(self):
        h = MyPage(self.driver)
        print('点击个人中心')
        h.clickMypage()
        self.assertEqual(1, 1)


if __name__ == 'main__':
    test = Mtest()
    test.testmine()