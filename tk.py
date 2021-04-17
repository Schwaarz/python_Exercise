from tkinter import *

# 创建窗口并给窗口设置标题
window = Tk()
window.geometry("500x200")
window.title("天命之子每日清扫脚本")
# 创建标签组件，设置其在窗口的位置
lbl = Label(window, text="请勾选需要的功能，可勾选多个同时进行")
lbl.grid(column=1, row=0)
# 根据列表创建复选框，并把值放到dic1中，且dic1[i]=True
Optionslist = {0:"恶魔擂台", 1:"活动地下城", 2:"重生迷宫", 3:"地下迷宫", 4:"探索", 5:"魔界温泉"}
dic1 ={}
for i in range(len(Optionslist)):
    dic1[i] = BooleanVar()
    chk = Checkbutton(window, text=""+Optionslist[i]+"", variable=dic1[i])
    chk.grid(column=3, row=i)
# 循环遍历dic1中键值并带出相应的文字
def sele():
    for key,value in dic1.items():
        if value.get() == True:
            print(Optionslist[key])
# 设置按钮触发函数
# def clicked():
#     # 获取复选框状态
#     d = chk_state.get()
#     print(chk_state.get())
#     if d == 1:
#         lbl.configure(text="我被点击了", fg="black")
#     else:
#         lbl.configure(text="请选择选项1", fg="red")
# 创建按钮组件，给按钮增加文本和颜色，设置显示在第二行的第二个位置并绑定上面的函数
btn = Button(window, text="点击运行", bg="#f391a9", fg="#3e4145", command=sele)
btn.grid(column=1, row=2)

window.mainloop()

