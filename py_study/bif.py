class New_int(int):
    """继承并更改int()"""
    def __add__(self,value):
        return int(self)-int(value)
    def __sub__(self,value):
        return int.__add__(self,value)

a=New_int(7)
b=New_int(5)
print(a+b)