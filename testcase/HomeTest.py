
from common.MyTest import MyTest
from po.HomePage import HomePage
from common.Public import Public


class HomeTest(MyTest):

    def testhome(self):
        h = HomePage(self.driver)
        print('点击首页')
        h.clickFirst()
        p = Public(self.driver)
        p.swipeUp()
        self.assertEqual(1, 1)


if __name__ == 'main__':
    test = HomeTest()
    test.testhome()

