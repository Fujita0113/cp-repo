def myPow(k, n, mod):
    # 指数を2進数に
    s = ""
    while True:
        s = s + str(n % 2)
        n //= 2
        if n == 0:
            break
    
    # 繰り返し二乗法
    res = 1
    for i in range(len(s)):
        if s[i] == "1":
            res *= k % mod
        k = k ** 2 % mod
    return res

N, K = map(int, input().split())

NUM = 10 ** 9 + 7

result = K % NUM
if N > 1:
    result = result * (K - 1) % NUM
    if N > 2:
        result = result * myPow(K - 2, N - 2, NUM) % NUM

print(result)