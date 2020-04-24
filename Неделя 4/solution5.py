import math

n = int(input())

if n == 2:
    print("YES")
    quit()

i = 2
limit = int(math.sqrt(n))

while i <= limit:
    if n % i == 0:
        print("NO")
        quit()
    i += 1

print("YES")
