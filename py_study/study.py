"""GUI"""
import tkinter as tk
root = tk.Tk()
tk.Label(root,text = '账号：').grid(row=0,column=0)
tk.Label(root ,text = '密码：').grid(row=1,column=0)
v1=tk.StringVar()
v2=tk.StringVar()
e1=tk.Entry(root,textvariable=v1)
e1.grid(row=0,column=1,padx=10,pady=5)
e2=tk.Entry(root,textvariable=v2,show='*')
e2.grid(row=1,column=1,padx=10,pady=5)
def show():
    print("作品：《%s》" % e1.get())
    print("作者：%s" % e2.get())
tk.Button(root,text='登录',width=10,command=show).grid(row=2,column=0,\
    padx=10,sticky='W')
tk.Button(root,text='退出',width=10,command=root.quit).grid(row=2,column=1,\
    padx = 10,sticky='E')
tk.mainloop()