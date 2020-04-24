n = int(input())
res = 0
while n != 0:
    sqr = n**2
    n -= 1
    res += sqr
print(res)
