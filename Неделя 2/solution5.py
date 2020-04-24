a, b, c = int(input()), int(input()), int(input())

print(min(a, b, c), a + b + c - min(a, b, c) - max(a, b, c), max(a, b, c))
