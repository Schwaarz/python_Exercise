#encoding:utf-8
num=int(raw_input("请输入一个数:"))
i=1
count=0 #count代表被整除的次数
while i<=num:
    if num%i==0:
        count+=1
    i+=1
if count>2:
    print("这个数不是素数")
else:
    print("这个数是素数")