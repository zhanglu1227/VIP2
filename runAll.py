
import unittest
import HTMLTestRunner
import time
import sys

def run_case():
    # 定义报告存放路径
    path = 'result' + time.strftime('%Y-%m-%d_%H-%M-%S') + '.html'
    reportpath = 'report/' + path

    # 定义一个文件名，以写的方式打开
    fp = open(reportpath, 'wb')

    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'UI测试报告',
        description=u'用例执行情况：')

    # 运行测试用例
    casedir = sys.path[0] + '/testCase'
    discover = unittest.defaultTestLoader.discover(start_dir=casedir, pattern="HomeTest.py", top_level_dir=None)
    runner.run(discover)

    # 关闭报告文件
    fp.close()

if __name__ == '__main__':
    run_case()



