N, K = input().split()
K = int(K)

for _ in range(K):
    N = int(N, 8)
    s = ""
    while True:
        s = str(N % 9) + s
        N //= 9
        if N == 0:
            break
    N = s.replace("8", "5")
print(N)
    