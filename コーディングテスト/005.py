# 8000以下の面積になる直角三角形は何個あるかを数えろ。ただし相似なものは1苞カウントする
# 解き方
# seen = set()で重複排除したsetを作って、len(seen)で数えられる
# ループの回数に関しては1から8000 * 2の16000の平方数までと平方数から16000まででループを作る
# seen.add()でsetは追加する
# isqrt(N)をすると、Nが5だったら、2が入ってくる。平方根の切り捨て
from math import gcd, isqrt

N = 8000
seen = set()
max_i = isqrt(2 * N)
for i in range(1, max_i + 1):
    for j in range(i, N * 2 + 1):
        if i * j > 2 * N:
            break
        g = gcd(i, j)
        seen.add((i // g, j // g))
print(len(seen))
        