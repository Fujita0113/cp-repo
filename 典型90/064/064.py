N, Q = map(int, input().split())
A = list(map(int, input().split()))
# 階差数列を作る
B = []
sum = 0
for i in range(N - 1):
    B.append(A[i + 1] - A[i])
    sum += abs(A[i + 1] - A[i])
actions = [tuple(map(int, input().split())) for _ in range(Q)]
# おそらくここまではあってる

for L, R, V in actions:
    if R == N:
        pass
    else:
        sum += abs(B[R - 1] - V) - abs(B[R - 1])
        B[R - 1] = B[R - 1] - V
    # elif B[R - 1] < 0:
    #     sum += V
    # else:
    #     sum -= V

    # ここの部分が間違っている
    if L == 1:
        pass
    else:
        sum += abs(B[L - 2] + V) - abs(B[L - 2])
        B[L - 2] += V
    # elif B[L - 2] < 0:
    #     sum -= V
    # else:
    #     sum += V
    print(sum)
    # ---
    
    # if not (L == 1 and R == N):
    #     if L == 1:
    #         B[R - 1] -= V
    #     elif R == N:
    #         B[L - 2] += V
    #     else:
    #         B[L - 2] += V
    #         B[R - 1] -= V

