
# coding: utf-8

# In[6]:


import os, sys
import requests
import re
import time

from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
from tkinter.messagebox import *
#import tkinter.filedialog as tkFileDialog
#import tkinter.simpledialog as tkSimpleDialog    #askstring()

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Form1')
        self.master.geometry('709x356+400+300')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('TLabel1.TLabel', anchor='w', font=('宋体',12))
        self.Label1 = Label(self.top, text='要翻译的内容：', style='TLabel1.TLabel')
        self.Label1.place(relx=0.023, rely=0.022, relwidth=0.159, relheight=0.07)

        self.style.configure('TLabel2.TLabel', anchor='w', font=('宋体',12))
        self.Label2 = Label(self.top, text='翻译的结果：', style='TLabel2.TLabel')
        self.Label2.place(relx=0.553, rely=0.022, relwidth=0.159, relheight=0.07)

        self.style.configure('TCommand1.TButton', font=('宋体',12))
        self.Command1 = Button(self.top, text='翻译', command=self.Command1_Cmd, style='TCommand1.TButton')
        self.Command1.place(relx=0.214, rely=0.876, relwidth=0.114, relheight=0.093)

        self.style.configure('TCommand2.TButton', font=('宋体',12))
        self.Command2 = Button(self.top, text='退出', command=self.Command2_Cmd, style='TCommand2.TButton')
        self.Command2.place(relx=0.677, rely=0.876, relwidth=0.114, relheight=0.093)

        self.Text1Var = StringVar(value='')
        self.Text1 = Text(self.top, width=100,height=10, font=('宋体',12))
        self.Text1.place(relx=0.011, rely=0.112, relwidth=0.475, relheight=0.744)

        self.Text2Var = StringVar(value='')
        self.Text2 = Text(self.top, width=100,height=10, font=('宋体',12))
        self.Text2.place(relx=0.519, rely=0.112, relwidth=0.453, relheight=0.744)
class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Command1_Cmd(self, event=None):
        #TODO, Please finish the function here!
        #TODO, Please finish the function here!
        content = self.Text1.get("0.0","end")
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        header = {'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
        data={
            'i': content,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            #时间戳
            'salt': '1527599872479',
            #签名
            'sign': 'a801ff94378f249420ae79e19ad57139',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_CLICKBUTTION',
            'typoResult': 'false'
        } 
        response = requests.post(url,data=data)
        translation = response.json()
#         print(translation)
        translate = translation['translateResult'][0][0]['tgt']
#         print(translate)
        self.Text2.delete(1.0,END)
        self.Text2.insert(1.0,translate)

    def Command2_Cmd(self, event=None):
        #TODO, Please finish the function here!
        top.destroy()
        
if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()

