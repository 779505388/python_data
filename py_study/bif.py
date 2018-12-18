"""__del__()方法"""


class C():
    '''创建一个类'''
    def __init__(self):
        print('调用__init__()方法中……')

    def __del__(self):
        """del方法在删除所有标签指向后才启动"""
        print('调用__del__()方法中……')

a1=C()