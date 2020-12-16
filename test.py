
# name=15360059852
# name='深圳';
# name='21岁';
# name='殷国豪';

#print(name,end="");
#print('欢迎学习python3.0',end="");
#变量不能以数字开头，但是可以包括数字，区分大小写，尽量见名知义，不要包含特殊符号

# name=input("请输入你的姓名:")
# age=int(input("请输入你的年龄:"))
# age=age+5
# print("姓名是："+name)
# #格式化输出
# print("五年后年龄是：%s"%age)
# input("\n\n按下enter键退出");
# a=b=c=d=f=g=h=1
# a,b,c,d=1,2,3,4
# print(a+b+c+d)
# b1='工作'
# b2='思考'
# print("爸爸要么在"+b1+','+"要么在"+b2)
# print("爸爸要么在%s要么在%s"%(b1,b2))
# a1=18
# a2='铁柱'
# a3=10
# print("这个楼层大概在%d楼层，而%s住在%d楼"%(a1,a2,a3))
# num=50
# print("这个大西瓜一共100块钱，分成两半后，一半%d块钱，一半%d块钱"%(num,num))
# age=12
# print('小明今年%d，3年后，小明%d岁'%(age,age+3))
#%s用字符串来代替，%d用整型值来代替，%f用浮点型来代替，%r用任意类型值来替代

# a=11
# b=12
# c=13
# d=14
# if a < b and d > c:
#     print('true')
# elif b < c or d < a:
#     print('不成立')
# else:
#     print('......')
# password=input("请输入密码：")
# print("您刚刚输入的密码是：%s"%password)

# longxia=int(input("这是龙虾，您要几斤,单价110元一斤："))
# dazhaxie=int(input("这是大闸蟹，您要几斤，单价91.5元一斤："))
# print('总共',longxia*110+dazhaxie*91.5,'元')
# chushou=91.5*2-50
# print(chushou)

# jiejie=int(input('你尽管输'))
# w=jiejie-11
# print('%d'%w)

# xiaoming=50
# xiaoxiaoming=50/2
#
# zhoushu=365/7
# day=365%52
# print(zhoushu)
# print(day)
# shengao=int(input('请输入你的身高：'))
# money=int(input('请输入你的存款：'))
# if money >= 500 and shengao >= 140:
#     print("土豪")
# else:
#     print("矮穷挫")


#12
# num1=float(input('请输入第一个数：'))
# num2=float(input('请输入第二个数：'))
# num3=float(input('请输入第三个数：'))
# jieguo=num1/(num2+num3)
# print(jieguo)

#13
# string=input('请输入一段文字：')
# num=int(input('请输入一个整数：'))
# fu=float(input('请输入一个小数：'))
# print('%s%d%f)'%(string,num,fu))

#14
# name=input('请输入您的名字：')
# age=int(input('请输入您的年龄：'))
# sex=input('请输入您的性别：')
# money=float(input('请输入您的收入：'))
# like=input('请输入您的爱好：')
# print("您输入的信息是：")
# print("姓名：%s"%name)
# print("年龄：%d"%age)
# print("性别：%s"%sex)
# print("收入：%f"%money)
# print("爱好：%s"%like)

#15
# commodity=input('请输入您购买的物品名称：')
# price=float(input('请输入您购买物品的价格：'))
# number1=int(input('请输入您购买的物品的个数：'))
# number2=int(input('请输入您付的钱数：'))
# Totalprice=price*number1
# money=number2-Totalprice
# print('您购买的商品：%s'%commodity)
# print('价格：%f'%price)
# print('个数：%d'%number1)
# print('您应该付的钱：%d'%Totalprice)
# print('找给您的钱：%d'%money)

#16
# name=input('请输入您的名称：')
# yuexin=int(input('请输入您月薪：'))
# canyinbutie=int(input('请输入您的餐饮补贴：'))
# lufeibutie=int(input('请输入您的路费补贴：'))
# zhufangbutie=int(input('请输入您的住房补贴：'))
# jibenyearxin=yuexin*12
# yearbutie=(canyinbutie+lufeibutie+zhufangbutie)*12
# yearshuiqian=jibenyearxin+yearbutie
# suodeshui=float(yearshuiqian*0.012)
# nianshuigz=yearshuiqian-suodeshui
# print(name,'的年基本工资：%d'%jibenyearxin)
# print(name,'的年补贴总金额：%d'%yearbutie)
# print(name,'的年补贴总工资：%d'%yearshuiqian)
# print(name,'应该缴纳1.2%的年个人所得税：',suodeshui)
# print(name,'的年税后总工资为：%f'%nianshuigz)

# money=int(input('输入你的资产：'))
# if money >100 and money <= 200:
#     print('小土豪')
# elif money > 80 and money < 100:
#     print('小康')
# else:
#     print('穷屌丝')

# money=int(input('输入你的成绩：'))
# if money > 90 :
#     print('优秀')
# elif money >= 80 and money < 90:
#     print('良好')
# elif money >= 70 and money < 80:
#     print('中等')
# else:
#     print('该努力了')

# socre=int(input('输入百米赛跑多少秒:'))
# sex=input('输入性别进行分组:')
# if socre <=10 and sex == '男':
#     print('进入男子决赛')
# elif socre <=10 and sex == '女':
#     print('进行女子决赛')
# else:
#     print('很遗憾，您被淘汰了')

# socre=int(input('请输入你跑步的成绩：'))
# if socre < 10:
#     print('恭喜进入决赛')
#     sex=input('请输入你的性别:')
#     if sex == '男':
#         print('进入男子决赛')
#     else:
#         print('进入女子决赛')
# else:
#     print('很遗憾，您被淘汰了')

# import random
# # num=int(random.random()*10)
# num=random.randint(0,3)
# while num<=100:
#     print('蔡徐坤出来打篮球')
#     num=num+1

# import random
# computer = random.randint(0,2)
# user = input('来玩剪刀，石头，布吧:')
# if user!='剪刀' and user!='石头' and user!='布':
#     print('输入错误')
# if user == '剪刀' and computer == 2:
#    print('赢了....可以去买奶粉了....')
# elif user == '石头' and computer == 0:
#    print('赢了....可以去买奶粉了....')
# elif user == '布' and computer == 1:
#    print('赢了....可以去买奶粉了....')
# elif user == computer:
#    print('平局了...洗洗手决战到天亮')
# else:
#    print('输了...回家拿钱再来...')

# user='admin'
# pwd=888888
# user1=input('请输入用户名:')
# pwd1=int(input('请输入密码：'))
# if user == user1 and pwd == pwd1:
#     print('登录成功')
# elif user1 != user or pwd1 != pwd:
#     print('账户名或密码错误，请重新输入')


# a = 10
# m = 1
# while m < 34:
#     if m <=6:
#         a=a*2
#     elif m<=15:
#         a=a+50
#     else:
#         a=a+20
#     m = m + 1
#     if(m>12):
#         print(a)

# pig=10
# pig=pig*(2**6)
# pig=pig+(50*9)
# print("%d"%pig)

# for i in range(1,11):
#     print(i)

# count=0
# string=input('输入字符串帮你计算A或a包含的个数:')
# for i in string:
# if i=='A' or i=='a':
#     count=count+1
#     print(count)

# sum=0
# for i in range(1,101):
#     if i%2==0:
#         sum+=1
#         print(sum)
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
#求字符串长度len（）
#去掉两端空格strip（）
#去掉左边的空格是用istrip（）
#去掉右边的空格用rstrip（）
#index：查找某个字符或者字符串在该字符或者字符串中的位置
#replace 替换字符串中的字符
# user=input("请输入用户名：")
# if user.__len__() < 6:
#     print("用户名长度必须大于六位")
# elif user.find("@")==-1:
#     print("用户名必须包含@符号")
# elif user.find("s",-1)==-1:
#     print("用户名必须要以s结尾")
# else:
#     pwd = input("请输入密码：")
#     if len(pwd)!=len(pwd.istrip()):
#      print("密码左边不能有空格")
#     elif len(pwd)!=7:
#         print("密码必须是7位数字")
#     elif pwd[3]!="m":
#         print("中间不是m")
#     else:
#         user=user[0].upper()+user[1:]
#         print("注册成功，用户名是%s密码是%s"%(user,pwd))
# name="JavaScript"
# print(name[2:-1:2])
# print(name.replace("J","j"))
#2：代表开始位置
#-1代表最后位置
#2代表步长
#2，-1，2表示从第二个开始到最后一个，每隔两个位置取一个数
# print("我的梦中情人{}".format(name))
#
#
# a='jay'
# b='python'
# print("my name is {}".format(a)+",i love "+b)
# str='good good study'
# if str==str.strip():
#     print("输入正确")
# else:
#     print("输入错误")
# print(str[10:-1])

# sum=0
# sum2=0
# scores=[10,20,30,40,50]
# for s in scores:
#     sum=sum+s
# print(max(scores))
# print(min(scores))
# print(sum/scores.__len__())
# scores.append(60)
# scores.append(70)
# scores.append(80)
# for a in scores:
#     sum2=sum2+a
# print(sum2)
# print(sum2/scores.__len__())
#有一个班级的列表clslist 在整个班级列表中有4个班级，
# 每个班级有五个学生，求出每个班级的平均分，以及这4个班级中平均分最高的班级位置
#求所有学生的总分以及平均分
# clslist=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
# sum=0
# sum0=0
# sum1=0
# sum2=0
# sum3=0
# for a in clslist[0]:
#     sum+=a
#     banji1=sum/clslist[0].__len__()
# print("一班平均分是：%d"%banji1)
# for a in clslist[1]:
#     sum1+=a
#     banji2=sum1/clslist[1].__len__()
# print("二班平均分是：%d"%banji2)
# for a in clslist[2]:
#     sum2+=a
#     banji3=sum2/clslist[2].__len__()
# print("三班平均分是：%d"%banji3)
# for a in clslist[3]:
#     sum3+=a
#     banji4=sum3/clslist[3].__len__()
# print("四班平均分是：%d"%banji4)
# all=clslist[0]+clslist[1]+clslist[2]+clslist[3]
# for a in all:
#     sum0+=a
# print("所有班级的总分是：%d"%sum0)
# pingjun=banji1+banji2+banji3+banji4
# print("所有班级的平均分是：%d"%pingjun)
# zuigao=0
# banji1=clslist[0]=0
# banji2=clslist[1]=1
# banji3=clslist[2]=2
# banji4=clslist[3]=3
# # banji=[banji1,banji2,banji3,banji4]
# # print(banji.index(max(banji)))
# if banji2 > banji1:
#     zuigao=banji2
#     if banji2 < banji3:
#         zuigao=banji3
#     if banji3 < banji4:
#         zuigao=banji4
# else:
#     zuigao=banji1
# print("平均分最高的班级是：%d"%zuigao)
# for a in range(1,8):
#     print("今天是星期%d"%a)
#     for t in range(1,8):
#         print("第%d个"%t)
# #嵌套循环
# clsList=[
#     [60,80,100,75,66],
#     [99,88,77,55,33],
#     [100,30,50,40,20],
#     [66,33,55,100,80]
# ]
# avgList=[]
# sum=0
# count=0
# allSum=0
# for s in clsList:
#     print("每个班级的成绩----------------")
#     for t in s:
#         sum=sum+t
#         count+=1
#         allSum=allSum+t
#     avg=sum/len(s)
#     avgList.append(avg)
#     sum=0
#     print("平均分是：%d"%avg)
#     print("总人数是：%d"%count)
#     print("总平均分是%d"%(allSum/count))
# maxAvg=avgList[0]
# #下标
# index = 0
# #循环比较
# for w in range(0, len(avgList)):
#     if avgList[w] > maxAvg:
#         maxAvg = avgList[w]
#         index = w
# print("最高平均分是%d最高平均分所在班级是%d" % (maxAvg, index))

# list1 = [1,'ww',3.1,'源昊']
# newList=[]
# for t in range(0,len(list1)):
#     if list1[t]==3.1 or list1[t]== "源昊" or list1[t]=="ww":
#         print(list1[t])
#         break
# print(newList)
#
# list1=[3.1,1,'ww','yh']
# for t in range(0,len(list1)):
#     if list1[t]== 'ww':
#         list1[t]="wang"
# print(list1)
#
# print(list1[2])
# print(list1[1:])
# list1.insert(1,'weixiao')
# print(list1)
# list1[2] = 'wang'
# print(list1)
# list1[0] = 2
# del list1[1]
# list1[1] = 'ww'
# print(list1[0:])
# list1[0] = 1
# del list1[1]
# del list1[1]
# print(list1[0:])


# list2=['小红','小兰','熊大']
# user=input("请输入姓名：")
# for s in range(0,len(list2)):
#     if user == list2[s]:
#         list2.remove(list2[s])
#         break
# if user in list2:
#     pass
# else:
#     user="gtq"
# list2.append(user)
# print(list2)

#元组的值不允许修改
#加值逗号
# tup=(12,33,22)
# tup2=(55,66)
# print(tup+(3,))


# myPhone={"jack","nick",12,"lisi"}
# tup=list(myPhone)#强转
# print(tup[0])
#
#
# a={'a','b','c','d','e'}
# b={'d','e','f'}
# print(a|b) #并集
# print(a&b) #交集
# print(a-b) #差
# print(a^b)#a和b中不同时存在的元素

#前面的值叫键值，
# 后面的值叫value值，
# 一个键值和一个value值叫做项
# dic={"s1":"jack","s2":"nick"}
# print(dic.keys())#获取所有键值
# print(dic.values())#获取所有value值
# print(dic.items())#获取所有的项
# print(dic["s1"])
# for s in dic.keys():#循环字典获取值
#     print(dic[s])

#求出整个年级的最高分所在班级名称
#求出tom这次考试的成绩
#从控制台输入一个学生学号，求出该学生是否在年级中如果在输出个人信息
#如果不在输出该学生不存在
#求出男女同学分别有多少个

dic={
    "s1":[
        {"sno":"1001","sname":"tom","score":80,"sex":"woman"},
        {"sno":"1002","sname":"jack","score":90,"sex":"man"},
        {"sno":"1003","sname":"nick","score":100,"sex":"woman"}
    ],
    "s2":[
        {"sno":"1004","sname":"mot","score":90,"sex":"man"},
        {"sno":"1005","sname":"kac","score":120,"sex":"woman"},
        {"sno":"1006","sname":"kin","score":70,"sex":"man"}
    ]
}
for s in dic.values():
    for t in s:
       print(t["score"])




# for s in dic.values():
#     for t in s:
#         if t["sname"]=="tom":
#             print(t)
#
# manCount=0
# woCount=0
# for s in dic.values():
#     for t in s:
#         if t["sex"]=="man":
#             manCount+=1
#         else:
#             woCount+=1
# print("男%d女%d"%(manCount,woCount))

# ListMsg=["张三","李四","王五","赵六","武大郎","武松"]
#
# name=0
# for i in ListMsg:
#     if i[0]=="李":
#         name+=1
# print ("该列表中姓李的人的个数是：%d"%name)
# # 左边姓查找
#
# xuehsng=[1,2,3,4,5]
# print(max(xuehsng))









