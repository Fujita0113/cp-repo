N = int(input())
classes, point = [0] * N, [0] * N
for i in range(N):
    classes[i], point[i] = map(int, input().split())

# [0] = 0, [1] = 1番までの和、...[N] = N番までの和
sum1, sum2 = [0] * (N + 1), [0] * (N + 1)
for i in range(N):
    sum1[i + 1] += sum1[i]
    sum2[i + 1] += sum2[i]
    if classes[i] == 1:
        sum1[i + 1] += point[i]
    else:
        sum2[i + 1] += point[i]

Q = int(input())
L, R = [0] * Q, [0] * Q
for i in range(Q):
    L[i], R[i] = map(int, input().split())

ans = []
# iはLとRの連番
for i in range(Q):
    a = sum1[R[i]] - sum1[L[i] - 1]
    b = sum2[R[i]] - sum2[L[i] - 1]
    ans.append(f"{a} {b}")
print("\n".join(ans))
