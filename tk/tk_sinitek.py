import base64
import os
import shutil
from tkinter import messagebox
from tkinter.ttk import *
import zipfile
import time
from tkinter import *
from icon import img


root = Tk()
root.title("一键文件替换")
# 读取base64转码后的数据，并设置压缩图标
picture = open("picture.ico", "wb+")
picture.write(base64.b64decode(img))
picture.close()
root.iconbitmap('picture.ico')
os.remove("picture.ico")
# 获取屏幕高度宽度
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
w = 810
h = 350
x = (screenWidth - w) / 2
y = (screenHeight - h) / 2
root.geometry("%dx%d+%d+%d" % (w, h, x, y))
label = Label(root, text="服务器前端路径:")
label.grid(row=0)
label1 = Label(root, text="前端部署包路径:")
label1.grid(row=1)
label2 = Label(root, text="服务器后端路径:")
label2.grid(row=2)
label3 = Label(root, text="后端部署包路径:")
label3.grid(row=3)
label4 = Label(root, text="进度显示  :", anchor="w", width=12)
label4.grid(row=4)
old_frontendpath = Entry(root, width="100")
new_frontendpath = Entry(root, width="100")
old_backendpath = Entry(root, width="100")
new_backendpath = Entry(root, width="100")
old_frontendpath.grid(column=1, row=0)
old_backendpath.grid(column=1, row=2)
new_frontendpath.grid(column=1, row=1)
new_backendpath.grid(column=1, row=3)
text = "操作说明：\n" \
       "1、本工具一旦点击执行，将不可逆，请仔细检查各项参数填写是否正确\n" \
       r"2、部署包文件路径实例：C:\Users\yinguohao\Downloads\国信应用包\broker.war" \
       "\n3、可以使用broker.war，工具会自动重命名并解压\n" \
       r"4、服务器文件路径实例：D:\\apache-tomcat-8.5.61\webapps\ROOT" \
       "\n5、所有参数不能为空，为空则执行不了，后续版本迭代"
msg = Message(root, text=text, width="400", bg="yellow")
msg.grid(column=1, row=7)
def iv():
    int1 = iv_default.get()
    return int1
iv_default = IntVar()
rb_default1 = Radiobutton(root, text='前端增量更新', value=1, variable=iv_default, command=iv)
rb_default2 = Radiobutton(root, text='后端增量更新', value=2, variable=iv_default, command=iv)
rb_default1.grid(column=1, row=5)
rb_default2.grid(column=1, row=6)

def del_file(filepath):
    """
    删除某一目录下的所有文件或文件夹
    :param filepath: 路径
    :return:
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


def re_filename(src, dst):
    """
    重命名文件
    :param src: 要重命名目录或文件
    :param dst: 重命名后目录或文件
    :return:
    """
    os.rename(src, dst)


def copy_file(src_dir, dst_dir):
    """
    复制src_dir目录下的所有内容到dst_dir目录
    :param src_dir: 源文件目录
    :param dst_dir: 目标目录
    :return:
    """
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    if os.path.exists(src_dir):
        for file in os.listdir(src_dir):
            file_path = os.path.join(src_dir, file)
            dst_path = os.path.join(dst_dir, file)
            if os.path.isfile(os.path.join(src_dir, file)):
                shutil.copyfile(file_path, dst_path)
            else:
                copy_file(file_path, dst_path)


def unzip(unsrc_dir, undst_dir):
    """
    传入压缩包路径，解压到指定路径中
    :param unsrc_dir:压缩包路径
    :param undst_dir:解压后路径
    :return:
    """
    file = zipfile.ZipFile(unsrc_dir, "r")
    for f in file.namelist():
        file.extract(f, undst_dir)
    file.close()


def progressnbar_show():
    """
    进度条函数
    :return:
    """
    num = 0
    list5 = 5
    progressbarF = Progressbar(root)
    progressbarF.place(relx=0.10, width=180, height=10, rely=0.29)
    progressbarF['maximum'] = list5  # 进度条最大值
    progressbarF['value'] = 0  # 进度条初始值
    while num < 6:
        progressbarF['value'] += 1  # 进度+1
        time.sleep(1)  # 延迟1秒
        root.update()  # 更新页面
    num += 1


# 帮助-关于
def menutips():
    messagebox.showinfo("关于", "作者：gh.yin\n"
                              "版本：1.0.0.0"
                        )


# 帮助-联系作者
def menutips_two():
    messagebox.showinfo("微信号", "QQ2071419073")

# 前端增量更新
def frontend_updating():
    rb = iv()
    print(rb)
    frontend_filepath = old_frontendpath.get()
    frontend_src_dir = new_frontendpath.get()
    frontend_dst_dir = old_frontendpath.get()
    if rb == 1 and frontend_filepath != '' and frontend_src_dir != '':
        try:
            del_file(frontend_filepath)  # 删除服务器前端文件
            copy_file(frontend_src_dir, frontend_dst_dir)  # 复制部署包文件到服务器-前端 C:\Users\yinguohao\Downloads\国信应用包\dist
        except BaseException:
            messagebox.showerror("错误", "系统找不到指定的路径")
    elif rb == 1 and frontend_filepath == '' and frontend_src_dir == '':
        messagebox.showwarning("警告", "前端增量更新，请检查路径是否填写")
    elif rb == 1 and frontend_filepath != '' and frontend_src_dir == '':
        messagebox.showwarning("警告", "前端增量更新，请检查路径是否填写")
    elif rb == 1 and frontend_filepath == '' and frontend_src_dir != '':
        messagebox.showwarning("警告", "前端增量更新，请检查路径是否填写")
    elif rb == 2 and frontend_filepath != '' and frontend_src_dir != '':
        messagebox.showwarning("警告", "请选择前端增量更新，请检查路径是否填写")

def backend_updating():
    rb = iv()
    print(rb)
    backend_filepath = old_backendpath.get()
    backend_dst_dir = old_backendpath.get()
    rename = new_backendpath.get()

    print(rename[-8:])
    if rb == 2 and backend_filepath != '' and rename != '':
        try:
            del_file(backend_filepath)  # 删除服务器后端文件
            if rename[-8:] == "broker.war":
                rename2 = rename.replace("broker.war", "ROOT.zip")  # 替换名称，获取同一路径，提供给重命名函数的传参
                rename3 = rename2.replace("ROOT.zip", "ROOT")  # 替换名称，获取同一路径，提供给解压、复制的函数的传参
                re_filename(rename, rename2)  # 部署包后端文件重命名 C:\Users\yinguohao\Downloads\国信应用包\broker.war
                unzip(rename2, rename3)  # 解压后端部署包
                copy_file(rename3, backend_dst_dir)  # 复制部署包文件到服务器-后端
            elif rename[-8:] == "ROOT.war":
                rename2 = rename.replace("ROOT.war", "ROOT.zip")
                rename3 = rename2.replace("ROOT.zip", "ROOT")  # 替换名称，获取同一路径，提供给解压、复制的函数的传参
                re_filename(rename, rename2)  # 部署包后端文件重命名 C:\Users\yinguohao\Downloads\国信应用包\broker.war
                unzip(rename2, rename3)  # 解压后端部署包
                copy_file(rename3, backend_dst_dir)  # 复制部署包文件到服务器-后端
        except Exception:
            messagebox.showerror("错误", "系统找不到指定的路径")
    elif rb == 2 and backend_filepath == '' and rename != '':
        messagebox.showwarning("警告", "后端增量更新，请检查路径是否填写")
    elif rb == 2 and backend_filepath != '' and rename == '':
        messagebox.showwarning("警告", "后端增量更新，请检查路径是否填写")
    elif rb == 2 and backend_filepath == '' and rename == '':
        messagebox.showwarning("警告", "后端增量更新，请检查路径是否填写")
    elif rb == 1 and backend_filepath != '' and rename != '':
        messagebox.showwarning("警告", "请选择后端增量更新，请检查路径是否填写")


def dy_list():
    rb = iv()
    print(rb)
    if rb == 0:
        frontend_filepath = old_frontendpath.get()
        backend_filepath = old_backendpath.get()
        frontend_src_dir = new_frontendpath.get()
        frontend_dst_dir = old_frontendpath.get()
        backend_dst_dir = old_backendpath.get()
        rename = new_backendpath.get()
        rename2 = rename.replace("broker.war", "ROOT.zip")  # 替换名称，获取同一路径，提供给重命名函数的传参
        rename3 = rename2.replace("ROOT.zip", "ROOT")  # 替换名称，获取同一路径，提供给解压、复制的函数的传参
        del_file(frontend_filepath)  # 删除服务器前端文件
        del_file(backend_filepath)  # 删除服务器后端文件
        re_filename(rename, rename2)  # 部署包后端文件重命名 C:\Users\yinguohao\Downloads\国信应用包\broker.war
        unzip(rename2, rename3)  # 解压后端部署包
        copy_file(frontend_src_dir, frontend_dst_dir)  # 复制部署包文件到服务器-前端 C:\Users\yinguohao\Downloads\国信应用包\dist
        copy_file(rename3, backend_dst_dir)  # 复制部署包文件到服务器-后端
        progressnbar_show()
    elif rb == 1:
        frontend_updating()
    elif rb == 2:
        backend_updating()
    else:
        messagebox.showwarning("提示", "不进行部署更新请关闭本软件，节约内存")

menubar = Menu(root)  # 菜单
filemenubar = Menu(menubar, tearoff=False)  # 下拉菜单
menubar.add_cascade(label='帮助', menu=filemenubar)  # 一级
filemenubar.add_command(label='联系作者', command=menutips_two)  # 二级
filemenubar.add_command(label='关于', command=menutips)  # 二级
root.config(menu=menubar)  # 菜单回显

btn = Button(root, text="点击即可替换文件（服务需手动启停）", command=dy_list)
btn.grid(column=1, row=4)
root.mainloop()
