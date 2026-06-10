import math

def myFactorization(N):
    if N == 1:
        return 1
    count = 0
    zero_flag = True
    while True:
        # 素数フラグ
        flag = True
        # ループの始まりについて
        # 1で割り切れるのは全部そうなので２からスタート

        # ループ上限について
        # 2.5だとしたら、2まではiが到達してほしい。intで2にしてからrange(3)にしている。
        # 4だとしたら、4まで回ってほしいのでどちらにせよOK
        for i in range(2, int(math.sqrt(N)) + 1):
            if N % i == 0:
                count += 1
                N //= i
                flag = False
                zero_flag = False
                break
        if N == 1 or zero_flag:
            break
        # Nが2か3になると、√が1.いくつなので、for i in range(2, 2)になり、無限ループ
        if flag:
            count += 1
            break
        
    return count

N = int(input())
if myFactorization(N) == 0:
    print(0)
else:
    print(math.ceil(math.log2(myFactorization(N)))) 