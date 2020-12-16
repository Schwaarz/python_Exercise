#1
# for i in range(1,101):
#     print("第",i,"遍写：好好学习，天天向上！")
#
#2
# for i in range(1,10001):
#     print("第",i,"遍写：好好学习，天天向上！")
#3
# print("上午阅读教材！")
# print("下午上机编程！")
# string1=input('合格了吗？y/n：')
# while string1 == 'n':
#         print("上午阅读教材！")
#         print("下午上机编程！")
#         string1 = input('合格了吗？y/n：')
# else:
#         print("完成学习任务！")
#4
# xueyuan=80000
# n=2006
# while xueyuan < 200000:
#     xueyuan=int(xueyuan*(1+0.25))
#     n = n + 1
#     print(n,"年，培训人数达到20万人")
#5
# num=1
# sum=0
# while num <= 100:
#     sum= sum + num
#     num += 1
#     print(sum)
# num=1
# sum=2
# while sum <=10:
#     num = sum * num
#     sum += 1
#     print(num)
#6
# print("请选择购买的商品编号：")
# print("1.T恤  2.网球鞋  3.网球拍")
# str1=input("请输入商品编号：")
# str2=int(input("请输入购买数量："))
#不会做
# if str1 == '1':
#     print("T恤￥245.0      数量%d   合计￥%d"%(str2,str2))
#7
# sum=105
# while sum >= 1:
#     sum=sum-5
#     print(sum)
#8
# sum=0
# num=1
# while num<=50:
#     num=num+1
#     if num%7==0:
#         sum+=num
#         print(sum)
#9不会
#10
# answer=input("请问你合格了么？")
# while answer == '不合格':
#     print("上午阅读教材，下午上机编程")
#     answer = input("请问你合格了么？")

# year=2006
# people=8
# while 1==1:
#     if people >= 20:
#         break
#     else:
#         people=people*1.25
#         year=year+1
# print("在%d年将达到20万以上"%year)
#缩进很重要
# sum=0
# for i in range(1,101):
#     sum=sum+i
# print(sum)
#6
# sum=0
# while True:
#     num=int(input("请选择购买的商品编号:1.T恤  2.网球鞋  3.网球拍:"))
#     count=int(input("请输入购买数量:"))
#     if num==1:
#         print("T恤￥245.0   数量%d  合计%d"%(count,count*245))
#         sum=sum+count*245
#     if num==2:
#         print("网球鞋￥570.0   数量%d  合计%d"%(count,count*570))
#         sum = sum + count * 570
#     if num==3:
#         print("网球拍￥700.0   数量%d  合计%d"%(count,count*700))
#         sum = sum + count * 700
#     anser=input("是否继续？")
#     if anser=='n':
#         break
# print("本次购物的总金额是：%d"%sum)
#反转结果reversed
# for s in reversed(range(5,100,5)):
#     print(s)
# sum=0
# for s in reversed(range(0,50,7)):
#      sum+=s
# print(sum)
# max=min=num=int(input("请输入:"))
# while True:
#     if num == 0:
#         break
#     num=int(input("请输入:"))
#     #如果假设的最大值小于输入的值则把输入的值赋予假设的最大值
#     if max<num:
#         max=num
#     if num<min and num!=0:
#         min=num
# print("最大值是：%d"%max)
# print("最小值是：%d"%min)

# num=int(input('请输入一个数：'))
# i=1
# count=0
# while i<=num:
#     if num%i==0:
#         count+=1
#         i+=1
# if count > 2:
#     print('这个数不是素数')
# else:
#     print('这个数是素数')
import random
count=0
randNum=random.randint(1,101)
while True:
    cai = int(input("请输入你要猜的数"))
    if(cai<randNum):
        print("这个数在%d到100之间"%cai)
    elif(cai>randNum):
        print("这个数在1到%d"%cai)
    elif(cai<randNum):
        pass

    elif(cai==randNum):
        print("恭喜你猜对了...")
        break
    count+=1
print("总共用了%d次"%count)










