import tkinter
import requests
from lxml import etree
def get_html(ip='197.25.55.11'):
    url='https://ip.cn/index.php?ip=%s' % ip
    html=requests.get(url)
    page=etree.HTML(html.text)
    data=page.xpath('/html/body/div/div[4]/div/p[2]/code/text()')
    print(data)
tk = tkinter.Tk()
tk.title('IP地址查询')
ip_input=tkinter.Entry(tk,width=50)

display_info = tkinter.Listbox(tk,width=50,height=10)
result_button= tkinter.Button(tk,text='查询',command=get_html )
if __name__ == "__main__":
    
    ip_input.pack()
    display_info.pack()
    result_button.pack()


    tk.mainloop()