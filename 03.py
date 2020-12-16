#encoding:utf-8
#为了帮助张浩尽快提高成绩，老师给他安排了每天的学习任务，
#其中上午阅读教材，学习理论部分，下午上机编程，掌握代码部分。
#老师每天检查学习成果。如果不合格，则继续进行
from pip._vendor.distlib.compat import raw_input

answer=raw_input("请问你合格了么？")
while answer=="没合格":
    print("上午阅读教材，下午上机编程....")
    answer = raw_input("请问你合格了么？")

