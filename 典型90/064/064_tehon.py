N, Q = map(int, input().split())
A = [map(int, input().split())]

B = [A[i + 1] - A[i] for i in range(N - 1)]
actions = [tuple(map(int, input().split())) for _ in range(Q)]

S = sum(abs(b) for b in B)
for L, R, V in actions:
    if L > 1:
        S -= abs(B[L - 2])
        B[L - 2] += V
        S += abs(B[L - 2])
    if R < N:
        S -= abs(B[R - 1])
        B[R - 1] -= V
        S += abs(B[R - 1])
    print(S)
