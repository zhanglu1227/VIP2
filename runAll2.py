'''
程序运行入口：
1、查找testcase
2、运行testsuite
'''


import unittest,os,time
import HTMLTestRunner
import sys
from common.SendMail import SendMail


# 获取当前路径
now_dir = os.path.dirname(os.path.abspath(__file__))

test_dir = now_dir + '\\' + 'testcase'
test_report = now_dir + '\\'+'Report'
print('************now_dir:', now_dir)
print('************test_dir:', test_dir)

def create_suite():
    '''获取用例脚本，组装测试套件'''
    #1---创建测试套件
    testunit = unittest.TestSuite()
    #2---获取符合的测试用例脚本，放入list
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*Test.py')
    print('this is discover', discover)
    #3---返回测试套件
    return discover

def clean_dir(goal_path):
    '''运行前清理以前生成的日志和报告'''
    #1---获取目标目录下的文件
    ls = os.listdir(goal_path)
    #2---遍历列表进行删除
    for i in ls:
        #3---连接目录和文件名，然后用方法进行删除
        file = os.path.join(goal_path,i)
        if os.path.isdir(file):
            clean_dir(file)
        else:
            os.remove(file)

if __name__ == '__main__':
    clean_dir(test_report)

    suite = create_suite()
    #获取当前时间
    now = time.strftime("%Y-%m-%d-%H_%M_%S")
    #定义测试报告的名字
    filename = test_report + '\\' + now + 'result.html'
    print('***********filename',filename)
    #1---以写入的方式打开文件
    fp = open(filename,'wb')
    #2---实例化运行类，制定运行的参数
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title='测试报告',
                            description=u"运行环境Android")
    runner.run(suite)

    print('已经运行完discover')
    fp.close()

    #发送邮件
    e = SendMail()
    e.send_email()