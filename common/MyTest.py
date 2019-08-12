
import unittest
from common.Driver import Driver

class MyTest(unittest.TestCase):

     @classmethod
     def setUpClass(cls):
         print('执行初始化类方法')
         driver = Driver()
         cls.driver = driver.startup()

     def setUp(self):
         print('执行初始化类方法')
         self.driver.launch_app()

     def tearDown(self):
         print('执行清理方法')
         self.driver.close_app()

     # def testcase(self):
     #     print('测试')

     @classmethod
     def tearDownClass(cls):
         print('执行清理方法')
         cls.driver.quit()

if __name__ == 'main__':
    unittest.main()

