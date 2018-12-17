"""__new__()方法学习"""


class CapStr(str):
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls, string)


a = CapStr('i love you')
print(a)
