from itertools import combinations
import math

N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

count = 0
for combo in combinations(A, 5):
    prod = 1
    for x in combo:
        prod = prod * x % P
    if prod == Q:
        count += 1
print(count)