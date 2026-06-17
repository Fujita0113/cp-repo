N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]

A.sort()
min_y = 10 ** 6 # > N
count = 0
for x, y in A:
    if y < min_y:
        min_y = y
    else:
        count += 1
print(N - count)