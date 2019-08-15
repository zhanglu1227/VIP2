import smtplib,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common.readConfig import ReadConfig


class SendMail():

    re = ReadConfig()
    #配置SMTP属性
    host = re.get_email('mail_host')
    username = re.get_email('mail_user')
    pwd = re.get_email('mail_pass')

    #配置邮件发送属性
    sender = re.get_email('sender')
    receiver = re.get_email('receiver')
    subject = re.get_email('subject')
    content = re.get_email('content')

    # 发送html格式邮件
    msg = MIMEMultipart()


    # 配置附件的属性
    def config_file(self):

        # 调用获取最新文件的方法
        file = self.find_new_file()
        # 添加附件,并打开文件
        f = open(file, 'rb')
        mail_body = f.read()

        # 创建消息对象
        filemsg = MIMEText(mail_body, 'plain', 'utf-8')
        # print(filemsg)

        filemsg["Content-Type"] = 'application/octet-stream'
        filemsg["Content-Disposition"] = 'attachment; filename=report.html'

        self.msg.attach(filemsg)

        self.msg['From'] = self.sender
        self.msg['To'] = self.receiver
        self.msg['subject'] = 'UI自动化测试报告'
        self.msg.attach(MIMEText('附件为UI自动化测试报告，请查收', 'plain', 'utf-8'))


    def send_email(self):

        self.config_file()

        try:
            # 创建一个 SMTP() 对象
            r = smtplib.SMTP()
            # 通过 connect 方法连接 smtp 主机
            r.connect(host=self.host)
            # 邮箱账号登录校验
            r.login(user=self.username, password=self.pwd)
            # 发送邮件
            r.sendmail(self.sender, self.receiver, self.msg.as_string())
            print('邮件发送成功')

        except Exception as msg:
            print('邮件发送失败', msg)
        finally:
            r.close()

    # 查找最新的文件
    def find_new_file(self):
        # 获取当前路径
        current_path = os.path.dirname(os.path.abspath(__file__))
        print('---current', current_path)

        # 获取报告的存放路径
        filePath = os.path.dirname(current_path) + '/' + 'report'
        fileList = os.listdir(filePath)
        #print(fileList)

        fileList = os.listdir(filePath)

        # 定义一个字典来接收文件的路径及文件名
        fileDict={}
        # 定义一个列表来接收文件的时间
        fileTime=[]

        #查找这个文件列表中每个文件的路径及文件名
        for iName in fileList:
            # 拼接文件路径和文件名
            filename = filePath + "/" + iName

            # 获取该文件的修改时间
            iTime = os.path.getmtime(filename)
            print(iTime)
            # 将文件的修改时间追加到时间列表中
            fileTime.append(iTime)
            # 将文件名iName作为字典的value,文件的修改时间iTime作为字典的key存入
            fileDict[iTime] = iName
            # fileD现在是空字典，把文件名和时间以键值对形式填充
        # print(fileDict, fileTime)

        # 查找时间列表中最新的文件
        sendfilekey = max(fileTime)

        #  把这个时间对应的文件名找出来，通过key查找value
        sendfile = fileDict[sendfilekey]
        # print(sendfile)
        sendfile = filePath + "/" + sendfile
        return sendfile