import sys

N = int(input())
A = list(map(int, input().split()))

if sum(A) % 10 != 0:
    print("No")
    sys.exit(0)
piece = sum(A) / 10

i, j = 0, 0
S = 0
while True:
    if i == N:
        break
    if S == piece:
        print("Yes")
        sys.exit()
    elif S > piece:
        S -= A[i]
        i += 1
        continue
    S += A[j]
    # インデックス更新部分
    j += 1
    if j == N:
        j = 0
print("No")