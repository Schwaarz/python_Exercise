from tkinter import *
from airtest.core.api import *
import sys

sys.path.append("D:/airtest work/games/tianmingzhizi.air")
# ST.PROJECT_ROOT = "D:/airtest work/games"
using("tianmingzhizi.air")
# from tianmingzhizi import Let_tai, CS_migong, HD_dixia, DX_migong, Tan_suo, MOJIE_wenquan, GS_dixa, SJ_boos2, devices

# 创建窗口并给窗口设置标题
window = Tk()
window.geometry("500x350")
window.title("天命之子每日清扫脚本")
col_count, row_count = window.grid_size()
for col in range(col_count):
    window.grid_columnconfigure(col, minsize=20)
for row in range(row_count):
    window.grid_rowconfigure(row, minsize=20)
# 创建标签组件，设置其在窗口的位置
lbl = Label(window, text="请勾选需要的功能，可勾选多个同时进行")
lbl.grid(column=0, row=0)
# 创建单选按钮
def rad_btn():
    num = var.get()
    if num == 1:
        print("模拟器已连接")

    elif num == 2:
        print("真机已连接")

    elif num == 3:
        print("远程真机已连接")


var = IntVar()
rb_1 = Radiobutton(window, text="模拟器", variable=var, value=1, command=rad_btn)
rb_1.grid(column=0, row=2, sticky="w")
rb_2 = Radiobutton(window, text="真机", variable=var, value=2, command=rad_btn)
rb_2.grid(column=0, row=3, sticky="w")
rb_3 = Radiobutton(window, text="远程真机", variable=var, value=3, command=rad_btn)
rb_3.grid(column=0, row=4, sticky="w")
# 根据列表创建复选框，并把值放到dic1中，且dic1[i]=True,默认全选
Optionslist = {0: "恶魔擂台", 1: "活动地下城", 2: "重生迷宫", 3: "地下迷宫", 4: "探索", 5: "魔界温泉", 6: "故事地下城", 7: "无尽对决"}
dic1 = {}
for i in range(len(Optionslist)):
    dic1[i] = BooleanVar(window,True)
    chk = Checkbutton(window, text="" + Optionslist[i] + "", variable=dic1[i], anchor="w")
    chk.grid(column=3, row=i, sticky="w")
# 反选按钮
def selectall():
    for i in range(len(Optionslist)):
        dic1[i] = BooleanVar()
qx = Button(window, text='反选', bg='#fff', fg='blue', command=selectall)
qx.grid(column=3, row=8, sticky="w")
# 循环遍历dic1中键值并带出相应的文字
def sele():
    list2 = ["恶魔擂台", "活动地下城", "重生迷宫", "地下迷宫", "探索", "魔界温泉", "故事地下城", "无尽对决"]
    for key, value in dic1.items():
        if value.get() == True:
            list1 = Optionslist[key]  # 将键值的文字赋值到list1
            if list1 == list2[0]:  # 判断list1的值是不是与list2的值相等，相等执行对应分支函数
                print("执行恶魔擂台函数")

            elif list1 == list2[1]:
                print("执行活动地下城函数")

            elif list1 == list2[2]:
                print("执行重生迷宫函数")

            elif list1 == list2[3]:
                print("执行地下迷宫函数")

            elif list1 == list2[4]:
                print("执行探索函数")

            elif list1 == list2[5]:
                print("执行魔界温泉函数")

            elif list1 == list2[6]:
                print("执行活动地下城函数")

            elif list1 == list2[7]:
                print("执行无尽对决函数")

# 创建按钮组件，给按钮增加文本和颜色，设置显示在第一行的第二个位置并绑定上面的函数
btn = Button(window, text="点击运行", bg="#f391a9", fg="#3e4145", command=sele)
btn.grid(column=0, row=5, sticky="w")

btn2 = Button(window, text='退出程序', bg='blue', fg='#fff', command=quit)
btn2.grid(column=1, row=5, sticky="w")
# 放入消息中进行渲染
window.mainloop()
