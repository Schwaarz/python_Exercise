from tkinter import *

from airtest.core.api import *
ST.PROJECT_ROOT = "D:/airtest work/games"
using("tianmingzhizi.air")
from tianmingzhizi import Let_tai,CS_migong,HD_dixia,DX_migong,Tan_suo,MOJIE_wenquan,GS_dixa,SJ_boos2,devices
# 日志类
class Logger(object):
    def __init__(self, filename='default.txt', stream=sys.stdout):
        self.terminal = stream
        self.log = open(filename, 'w')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

sys.stdout = Logger('default.txt', sys.stdout)
sys.stderr = Logger('default.txt', sys.stderr)
# 实例化日志类对象并初始化
# log = Logger()
# log.__init__()
# 创建窗口并给窗口设置标题
window = Tk()
window.geometry("350x200")
window.title("天命之子每日清扫脚本")
col_count, row_count = window.grid_size()
for col in range(col_count):
    window.grid_columnconfigure(col, minsize=20)
for row in range(row_count):
    window.grid_rowconfigure(row, minsize=20)
# 创建标签组件，设置其在窗口的位置
lbl = Label(window, text="请勾选需要的功能，可勾选多个同时进行")
lbl.grid(column=1, row=0)
# 根据列表创建复选框，并把值放到dic1中，且dic1[i]=True
Optionslist = {0: "恶魔擂台", 1: "活动地下城", 2: "重生迷宫", 3: "地下迷宫", 4: "探索", 5: "魔界温泉",6: "故事地下城"}
dic1 = {}
for i in range(len(Optionslist)):
    dic1[i] = BooleanVar()
    chk = Checkbutton(window, text="" + Optionslist[i] + "", variable=dic1[i], anchor="w")
    chk.grid(column=3,row=i,sticky="w")
# 循环遍历dic1中键值并带出相应的文字
def sele():
    list2 = ["恶魔擂台", "活动地下城", "重生迷宫", "地下迷宫", "探索", "魔界温泉", "故事地下城"]
    for key, value in dic1.items():
        if value.get() == True:
            list1 = Optionslist[key]   # 将键值的文字赋值到list1
            if list1 == list2[0]: # 判断list1的值是不是与list2的值相等，相等执行对应分支函数
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

# 创建按钮组件，给按钮增加文本和颜色，设置显示在第一行的第二个位置并绑定上面的函数
btn = Button(window, text="点击运行", bg="#f391a9", fg="#3e4145", command=sele)
btn.grid(column=1, row=5)

# 放入消息中进行渲染
window.mainloop()
