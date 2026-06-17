次のように入力が与えられる
```
4
1 2
1 3
1 2
3 1 2 3
```
4人人が居て、人1は一人にプレゼントをあげます。それは人2です。。。

出力は
```
1 4
3 1 3 4
2 2 4
0
```
人1は一人からプレゼントをもらいました。それは人4です。
人2は３人からプレゼントを貰いましたみたいな

1 2の入力を受け取ったら、人2のところに1を追加したらいい。
つまりAをfor文で取り出して、record[i- 1]にappendすればいいって話？
iは1、つまりプレゼントを挙げた人。Aは2, つまりプレゼントを貰った人。record[i - 1]はiにプレゼントを挙げた人がはいった行列
つまり
record[0]: 1にプレゼントをあげた人 [4（人4）] 
```Python
N = int(input())
record = [[] for _ in range(N)]
for i in range(N):
    K, *A = map(int, input().split())
    for val in A:
        record[val - 1].append(i + 1)
print(record)
```
ここまででレコードできたはず。次に出力について考える
for文終了時点でrecordにはこれがはいっている
```
[[4], [1, 3, 4], [2, 4], []]
```
```Python
for res in record:
    print(f"{len(les) {" ".join(res)}}")
```