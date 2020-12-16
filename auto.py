#第一题
import random
sjs=random.randint(1,100)
for a in range(0,5):
    user=int(input('请随机输入一个整数:'))
    if sjs==user:
        print('中奖啦')
    else:
        print('不中')

#第二题
# num=0
# for b in range(1,201):
#     if b%3==0:
#         num=num+b
#     b=b+1
# print('1-200中能被3整除的数的总和是%d'%num)

#第三题
# testMsg={
#     "java":[
#             [
#                 {"name":"张三" ,"stuNo":"425306","score":80},
#                 {"name":"李四" ,"stuNo":"425307","score":90},
#                 {"name":"王五" ,"stuNo":"425308","score":75}
#             ],
#             [
#                 {"name": "赵六","stuNo":"729905","score":45},
#                 {"name": "王莉莉","stuNo":"729906","score":77},
#                 {"name": "孤独","stuNo":"729907","score":26}
#             ]
#          ],
#     "sql":[
#             [
#                 {"name": "刘小小","stuNo":"86870","score":88},
#                 {"name": "都铎","stuNo":"86871","score":64},
#                 {"name": "王大力","stuNo":"86872","score":45}
#             ],
#             [
#                 {"name": "贾贝贝","stuNo":"86873","score":33},
#                 {"name": "代玉","stuNo":"86874","score":76},
#                 {"name": "代三年","stuNo":"86875","score":53}
# 	  ]
#          ]
# }
#1
# for e in testMsg["java"][0]:
# a1=0
# b1=0
# for e in testMsg["java"]:
#    for t in e:
#        b1+=1
#        if t["score"]>60:
#            a1+=1
# print("合格率为%"+"%f"%(a/b*100))
#2
# for s in testMsg.keys():
#     if s == 'java':
#         for t in testMsg[s]:
#             for q in t:
#                 if q['score'] < 60:
#                     print(q)
#3



#第四题
# sum=0
# while 1==1:
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

#第五题
# stuList=["张三","李四","王五","赵六","克拉玛武七"]
#1
# num2=0
# shuru=input('请输入一个姓名：')
# for c in stuList:
#     if shuru==c:
#         print('已经存在')
#     else:
#         num2+=1
# if num2==len(stuList):
#     stuList.append(shuru)
#     print(stuList)
#2
# rs=0
# for d in stuList:
#     rs+=1
# print('集合一共有%d人'%rs)
#3
# zuichang=""
# for e in stuList:
#     if len(e)>len(zuichang):
#         zuichang=len(e)
# print("名字最长的人的姓名是：%s"%e)