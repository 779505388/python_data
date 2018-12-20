<<<<<<< HEAD
class New_int(int):
    """继承并更改int()"""
    def __add__(self,value):
        return int(self)-int(value)
    def __sub__(self,value):
        return int.__add__(self,value)

a=New_int(7)
b=New_int(5)
print(a+b)
=======
"""__del__()方法"""


class C():
    '''创建一个类'''
    def __init__(self):
        print('调用__init__()方法中……')

    def __del__(self):
        """del方法在删除所有标签指向后才启动"""
        print('调用__del__()方法中……')

a1=C()
>>>>>>> a3d55760aa0d34882a246442616190544cf6b2ea
