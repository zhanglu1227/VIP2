import xlrd,xlwt,os


#获取测试数据的存放目录
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

file = path + '\\' +'Data'+'\\'+'data.xlsx'
print('path',path)
print('file',file)

def readdata(Method,file=file):
    '''
    1、传入类名和方法名
    2、根据方法名获取对应测试数据
    3、测试数据放入list进行返回
    '''
    # print('xxx',file)
    workbook = xlrd.open_workbook(file)
    sheet1 = workbook.sheet_by_index(0)
    #获取方法列表和测试数据列表
    cols1 = sheet1.col_values(1)
    cols2 = sheet1.col_values(2)
    testdata = []
    # print('方法列表',cols1)
    # print('数据列表',cols2)
    #根据传入的方法来获取对应的测试数据
    for i in cols1:
        if Method == i:
            data = cols2[cols1.index(i)]
            # print('Method',Method,'data',data,'index',)
            List = data.split(',')
            # print('List',List)
            testdata = List

    # print('testdata',testdata)

    return testdata



if __name__ == '__main__':

    readdata('get_login_Message')