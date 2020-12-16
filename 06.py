#encoding:utf-8
sum=0 #总金额
while True:
    num=int(raw_input("请选择购买的商品编号:1.T恤   2.网球鞋  "
                      " 3.网球拍"))
    count=int(raw_input("请输入购买数量:"))
    if num==1:
        print("T恤￥245.0   数量%d  合计%d"%(count,count*245))
        sum=sum+count*245
    if num==2:
        print("网球鞋570   数量%d  合计%d"%(count,count*570))
        sum = sum + count * 570
    if num==3:
        print("网球拍700   数量%d  合计%d"%(count,count*700))
        sum = sum + count * 700
    anser=raw_input("是否继续?")
    if anser=="n":
        break
print("本次购物的总金额是:%d"%sum)


