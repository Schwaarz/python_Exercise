def factor(n):
    res=1
    for i in range(1,n+1):
        res *= i
    return res

print(factor(520))