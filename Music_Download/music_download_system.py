
# coding: utf-8

# In[2]:


import os, sys
import requests
import re

if sys.version_info[0] == 2:
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    from tkinter import *
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('音乐下载')
        self.master.geometry('626x391')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('TLabel1.TLabel', anchor='w', font=('楷体',14))
        self.Label1 = Label(self.top, text='歌手：', style='TLabel1.TLabel')
        self.Label1.place(relx=0.038, rely=0.041, relwidth=0.104, relheight=0.084)

        self.Text1Var = StringVar(value='')
        self.Text1 = Entry(self.top, textvariable=self.Text1Var, font=('楷体',14))
        self.Text1.place(relx=0.166, rely=0.02, relwidth=0.181, relheight=0.105)

        self.style.configure('TLabel2.TLabel', anchor='w', font=('楷体',14))
        self.Label2 = Label(self.top, text='歌曲：', style='TLabel2.TLabel')
        self.Label2.place(relx=0.038, rely=0.164, relwidth=0.104, relheight=0.084)

        self.List1Var = StringVar(value='')
        self.List1Font = Font(font=('楷体',14))
        self.List1 = Listbox(self.top, listvariable=self.List1Var, font=self.List1Font)
        self.List1.place(relx=0.166, rely=0.164, relwidth=0.564, relheight=0.777)
        self.List1.bind('<Double-Button-1>', self.download)
        self.List1.curIndex = None


        self.style.configure('TCommand1.TButton', font=('楷体',14))
        self.Command1 = Button(self.top, text='开始搜索', command=self.Command1_Cmd, style='TCommand1.TButton')
        self.Command1.place(relx=0.371, rely=0.02, relwidth=0.181, relheight=0.105)

        self.style.configure('TCommand2.TButton', font=('楷体',14))
        self.Command2 = Button(self.top, text='选择路径', command=self.Command2_Cmd, style='TCommand2.TButton')
        self.Command2.place(relx=0.767, rely=0.205, relwidth=0.181, relheight=0.105)

        self.style.configure('TCommand3.TButton', font=('楷体',14))
        self.Command3 = Button(self.top, text='开始下载', command=self.Command3_Cmd, style='TCommand3.TButton')
        self.Command3.place(relx=0.767, rely=0.471, relwidth=0.181, relheight=0.105)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    
    def __init__(self, master=None):
        Application_ui.__init__(self, master)
        
    def Command1_Cmd(self, event=None):
        #TODO, Please finish the function here!
        self.geshou = self.Text1Var.get()
        self.list_information=[]
        self.List1Var.set('')
       
        #搜索歌曲
        self.music = {
            'key':self.geshou
        }
        #百度音乐搜索api
        search_url = 'http://music.baidu.com/search'
        #发送http请求
        search_response = requests.get(search_url,params=self.music)
        #设置编码
        search_response.encoding = 'utf-8'
        search_html = search_response.text
        #获取歌曲id，用正则表达式
        song_ids = re.findall(r'sid&quot;:(\d+),',search_html)
        #print(song_ids)

        #根据id去获取歌曲的信息
        song_api='http://play.baidu.com/data/music/songlink'
        data = {
            'songIds':','.join(song_ids),
            'hq':0,
            'type':'mp3',
            'pt':0,
            'flag':1,
            's2p':650,
            'prerate':128,
            'bwt':266,
            'dur':231000,
            'bat':266,
            'bp':100,
            'pos':65833,
            'auto':0  
        }
        #发送请求
        song_response = requests.post(song_api,data=data)
        #print(song_response.text)
        #将返回回来的歌曲数据转换成字典
        self.song_info = song_response.json()
        self.song_info = self.song_info['data']['songList']
#         print(self.song_info)
        #遍历song_info
        for song in self.song_info:
            self.song_name = song['songName']
#             self.song_author = song['artistName']
            music_information = self.song_name
#             print(song_author + ':' + song_name)
#             print(song['songLink'])
            self.list_information.append(music_information)
            self.list_information.append(song['songLink'])
            self.List1.insert(END, music_information)

        
        
    def Command2_Cmd(self, event=None):
        #TODO, Please finish the function here!
        self.path = tkFileDialog.askdirectory()
        print(self.path)
    def Command3_Cmd(self, event=None):
        #TODO, Please finish the function here!
        with open(self.path + '/'+ '%s.mp3' % self.contend,'wb') as f:
        #下载mp3
            for i in self.song_info:
                if i['songName'] == self.contend:
                    response = requests.get(i['songLink'])
                    print(response.content)
                    f.write(response.content)                 
    
    def download(self, event=None):
        self.contend = self.List1.get(self.List1.curselection())
        print(self.contend)

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()


