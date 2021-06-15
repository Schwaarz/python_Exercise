import os
import sys
import win32con
import win32api
from tkinter import *

root = Tk()
root.resizable(width=False, height=False)
text = Text(root)
text.pack(fill=X, side=BOTTOM)
text.grid(row=0, padx=2, pady=2)


def hello():
    #    print('hello')
    text.insert(END, 'hello' + '\n')
    text.insert(END, "我是命令行")


def about():
    #    print('ok')
    text.insert(END, 'ok' + '\n')


def change():
    root.update()


def delete():
    text.delete(1.0, END)


def Exit():
    os._exit(0)


def show():
    try:
        # 你要的在这里
        # f = sys.stdout
        f = os.popen('08.py')
        for l in iter(f.readline, ''):
            print(l,end='')
            text.insert(END, l)
            text.see(END)
            text.update()

    except:
        win32api.MessageBox(0, "文件读写错误！",
                            "警告！", win32con.MB_OK)


menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="开始", command=show)
filemenu.add_command(label="清除", command=delete)
filemenu.add_command(label="退出", command=Exit)
menubar.add_cascade(label="文件", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="关于", command=about)
helpmenu.add_command(label="帮助", command=hello)
menubar.add_cascade(label="帮助", menu=helpmenu)

root.config(menu=menubar)

mainloop()
