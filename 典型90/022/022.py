from math import gcd

a, b, c = map(int, input().split())
side = gcd(a, b, c)

answer = (a // side - 1) + (b // side - 1) + (c // side - 1)
print(answer)