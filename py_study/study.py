'''python递归的学习'''
def hanoi(n=4,x='x',y='y',z='z'):
    if n == 1 :
        print(x,'移动到',z)
    else:
        hanoi(n-1,x,z,y)
        print(x,'移动到',z)
        hanoi(n-1,y,x,z)
hanoi(n=3)