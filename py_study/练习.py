'''回文数判断'''
mun =''
while type(mun) != type(123):

    try:
        mun=eval(input('请随机输入一个数：'))
    except:

        print('请输入一个数！！！')

    
mun = str(mun)
sj = ''
a=99999
a=len(mun)
while a >=1:
    a -=1
    sj = sj +mun[a]
    
if mun == sj:
    print('输入的数为回文数')
else:
    print('输入的不是回文数')