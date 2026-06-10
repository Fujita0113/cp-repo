```
5
e869120
atcoder
e869120
square1001
square1001
```
のように入力が与えられる。Nは10^5まで。
それで、上から順番にこのユーザー名で登録を行い、重複していた場合は登録が拒否される。拒否されなかった日を出力する。例えば以下のように
```
1
2
4
```
## 考える
setを使えば行けると思うのだけれど、setの使い方を忘れた。特に検索。確かあれ、Order(1)だった気がするんだけど
setは
```
myset1 = set([1,2,3])
```
のように引数に配列を入れる形で定義し、
```Python
print(1 in myset1)
# trueが出力される
```
のように使う。
じゃあ定義してからあとから値を追加する方法はあるのかな
```
myset.add(4)
```
のようにすると追加できる

## 改善点
Pythonは以下のように書ける
```
fruits = ["apple", "orange"]
for fruit in fruits:
    print(fruit)
```
これを応用して
```
fruits = [(0, "apple"), (1, "orange")]
for index, fruit in fruits:
    print(f"{index}:{fruit}")
```
も行ける。さらに
```
fruits = ["apple", "orange"]
for index, fruit in enumerate(fruits):
     同様
```
も行ける。これは1個上のやつと同じ出力が出る。enumerateは数え上げるの意味で、インデックスとvalueをタプルのリストにして返すのだ。
さらに
```
for index, fruit in enumerate(fruits, start=1):
```
のようにすれば、インデックスを1から開始できる。それを今回のに使うべきだった