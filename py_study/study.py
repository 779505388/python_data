"""GUI"""
import tkinter as tk
root = tk.Tk()
sb =tk.Scrollbar()
sb.pack(side ='right',fill='y')
lb = tk.Listbox(root,yscrollcommand=sb.set)
lb.pack()
for i in range(100):
    lb.insert('end',i)

lb.pack(side = 'left',fill='both')
sb.config(command = lb.yview)
tk.mainloop()