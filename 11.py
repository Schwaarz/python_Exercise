#encoding:utf-8
import random
#升级第4章第10题，猜数字游戏
#系统随机产生1～100之间的随机数（使用 Random）
#然后使用循环判断，记录次数
#演示：(假设系统随机的数字为58)
	#请输入您第1次猜的数字:50
	#小了
	#这个数应该在50～100之间
	#请输入您第2次猜的数字：75
	#大了
	#这个数应该在50～75之间
	#请输入您第3次猜得数字：60
	#大了
	#这个数应该在50~60之间
	#请输入您第4次猜得数字:55
	#小了
	#这个数应该在55~60之间
	#请输入您第5次猜得数字:58
	#太棒了，您猜中了
#您猜的次数为：5次
#生成一个随机数
count=0
randNum=random.randint(1,101)
while True:
    cai = int(raw_input("请输入你要猜的数"))
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




