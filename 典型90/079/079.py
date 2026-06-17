import sys

def action(i, j, A, B, H, W, count):
    num = B[i][j] - A[i][j]
    if num:
        for ni, nj in [(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)]:
            if ni < H and nj < W:
                A[ni][nj] += num
        count += abs(num)
    return A, count

H, W = map(int, input().split())
A = list(list(map(int, input().split())) for _ in range(H))
B = list(list(map(int, input().split())) for _ in range(H))

count = 0
for i in range(min(H - 1, W - 1)):
    A, count = action(i, i, A, B, H, W, count)
    for j in range(i + 1, H - 1):
        A, count = action(j, i, A, B, H, W, count)
    for k in range(i + 1, W - 1):
        A, count = action(i, k, A, B, H, W, count)
if A[H - 1] != B[H - 1]:
    print("No")
    sys.exit()
else:
    print("Yes")
    print(count)