import os
import configparser  # 读取配置文件模块

# 获取文件路径
fileDir = os.path.split(os.path.realpath(__file__))[0]
print(fileDir)

#获取上层目录
parDir = os.path.dirname(fileDir)
print(parDir)

# 获取配置文件路径
configPath = os.path.join(parDir,'config.ini')
print(configPath)

class ReadConfig(object):
    def __init__(self):
        # 第一步：实例化configparser对象
        self.cf = configparser.ConfigParser()
        # 第二步：调用read方法读取该文件（传参：文件路径和编码格式）
        self.cf.read(configPath, encoding="utf-8-sig")

    # 获取配置文件中的分组（eg:EMAIL）中的对应选项(eg:name)的值
    def get_email(self, name):
        # 第三步：获取某某section下的配置，name相当于key
        value = self.cf.get("EMAIL", name)
        return value
    
if __name__ == '__main__':
    c = ReadConfig()
    print(c.get_email('mail_user'))




