N = int(input())
lst = map(int, (input().split()))
x = int(input())
print(min(lst, key=lambda a: abs(a - x)))
