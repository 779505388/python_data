"""python内置函数的学习"""
class Rectangle:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def get_peri(self):
        '''计算周长'''
        return 2*(self.x+self.y)
    def get_area(self):
        '''计算面积'''
        return self.x*self.y

exa=Rectangle(3,4)
print(exa.get_area())