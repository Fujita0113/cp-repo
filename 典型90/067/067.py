def tenToNine(N):
    arr = []
    while True:
        arr.append(N % 9)
        N = N // 9
        if N == 0:
            break
    return sum(arr[i] * (10 ** i) for i in range(len(arr)))

def eightToTen(N):
    S = 0
    i = 0
    while True:
        S += N % 10 * (8 ** i)
        N = N // 10
        i += 1
        if N == 0:
            break
    return S

def convertNum(N):
    arr = []
    while True:
        if N % 10 == 8:
            arr.append(5)
        else:
            arr.append(N % 10)
        N = N // 10
        if N == 0:
            break
    return sum(arr[i] * (10 ** i) for i in range(len(arr)))

N, K = map(int, input().split())
for _ in range(K):
    N = convertNum(tenToNine(eightToTen(N)))
print(N)