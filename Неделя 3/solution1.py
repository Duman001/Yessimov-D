a = float(input())
b = float(input())
c = float(input())
p = (a + b + c) / 2
S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
if S % 1 == 0:
    S = int(S)
else:
    S = '{0:.6f}'.format(S)
print(S)
