a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
x1 = d - a
x2 = d - b
x3 = d - c
x4 = e - a
x5 = e - b
x6 = e - c
if x1 >= 0 and x4 >= 0:
    print('Yes')
elif x1 >= 0 and x5 >= 0:
    print('Yes')
elif x1 >= 0 and x6 >= 0:
    print('Yes')
elif x2 >= 0 and x4 >= 0:
    print('Yes')
elif x2 >= 0 and x5 >= 0:
    print('Yes')
elif x2 >= 0 and x6 >= 0:
    print('Yes')
elif x3 >= 0 and x4 >= 0:
    print('Yes')
elif x3 >= 0 and x5 >= 0:
    print('Yes')
elif x3 >= 0 and x6 >= 0:
    print('Yes')
else:
    print('No')
