#encoding:utf-8
#max:假设的最大值
#min:假设的最小值
#num:刚输入的值
max=min=num=int(raw_input("请输入"))
while True:
    if num==0:
        break
    num=int(raw_input("请输入"))
    #如果假设的最大值小于输入的值则把输入的值赋给假设的最大值
    if max<num:
        max=num
    # 如果假设的最小值小于输入的值则把输入的值赋给假设的最小值
    if num<min and num!=0:
        min=num
print("最大值是:%d"%max)
print("最小值是:%d"%min)
