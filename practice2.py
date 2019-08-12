import unittest
from common.Driver import Driver

class practice2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('当前测试类所有test开头的用例执行一次')
        driver = Driver()
        cls.driver = driver.startup()

    def setUp(self):
        print('当前测试类每个test开头的用例前执行一次')
        # driver = Driver()
        # self.driver = driver.startup()


    def testHome(self):

        # self.driver.find_elements_by_id()
        print('测试步骤')


    def tearDown(self):
        print('xxx')
        # self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        print('xxx')
        cls.driver.quit()

if __name__ == 'main__':
    unittest.main()