

class Public():

    def __init__(self, driver):
        self.driver = driver



    def getSize(self):

        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']

        return (x,y)

    # 向上滑动
    def swipeUp(self,t=1000):

        l = self.getSize()
        x1 = int(l[0]*0.5)
        y1 = int(l[1]*0.25)
        y2 = int(l[1]*0.75)
        self.driver.swipe(x1,y1,x1,y2,t)



if __name__ == 'main__':
    p = Public()
    p.swipeUp()






