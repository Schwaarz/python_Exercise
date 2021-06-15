import tkinter as tk
import os
import tkinter.messagebox as messagebox



def tk_file():
    root = tk.Tk()
    text = tk.Text(root, width=100, height=20)
    text.pack()

    text.insert("insert", "点击插入按钮（读取已经存在的TXT内容，并插入在此处） ")
    text.insert('end', '\n')

    mytxtfile = "D:\\RDAPP.txt"


    # 读取TXT文件，显示在tkinter的Text
    def in_f_txt():
        if os.path.exists(mytxtfile):
            a = open(mytxtfile, 'r', encoding='utf-8')
            for id_names in a:
                text.insert('insert', id_names)
            a.close()

    b3 = tk.Button(text, text="插入", command=in_f_txt)
    text.window_create("insert", window=b3)
    text.insert('end', '\n')
    root.mainloop()
# 输入文本框
# input_txt = tk.Entry(root, width=20)
# input_txt.pack()


# def add():
#     # 通过get()函数获得Text（input_txt）的输入内容
#     var_id = input_txt.get()
#     h = open(mytxtfile, 'a+', encoding='utf-8')
#     h.write(var_id + '\n')  # 添加到文件夹中的txt
#     h.close()
#
#
# b2 = tk.Button(text, text="写入txt", command=add)
# text.window_create("insert", window=b2)
# text.insert('end', '\n')


