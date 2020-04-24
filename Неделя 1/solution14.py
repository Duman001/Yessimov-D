n = int(input())

n = (n % 1440)

print(n // 60, ' ', n % 60, sep="")
