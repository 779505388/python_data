"""GUI"""
import tkinter as tk
master = tk.Tk()
theLB= tk.Listbox(master,selectmode= 'extended',height =11)
theLB.pack()
for item in range(11):
    theLB.insert('end',item)

theButton = tk.Button(master,text= 'delete',\
    command = lambda x= theLB:x.delete('active'))
theButton.pack()
tk.mainloop()