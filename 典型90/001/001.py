N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

def canCutWithMinLength(minLength):
    cutCount = 0
    prePosition = 0

    for i in range(N):
        # 当然、minLengthで切れている場合もOK
        if A[i] - prePosition >= minLength:
            cutCount += 1
            prePosition = A[i]
    
    # minLengthで切れているときも当然OK
    if L - prePosition >= minLength:
        cutCount += 1
    # 仮にK+1だったとしても当然minLenght以上の長さのK+1個に分けることができる
    return cutCount >= K + 1

left = -1
right = L + 1
while right - left > 1:
    mid = (left + right) // 2
    if canCutWithMinLength(mid):
        left = mid
    else:
        right = mid
print(left)

