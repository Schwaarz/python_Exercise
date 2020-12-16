#encoding:utf-8
#从100每次递减5输出直至5
#输出结果: 100 95 90 85 80 75 70
# a=100
# while a>5:
#     a = a - 5
#     print(a)
for s in reversed(range(5,101,5)):
    print(s)