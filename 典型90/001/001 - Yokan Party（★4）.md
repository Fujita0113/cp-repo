![[Pasted image 20260118130035.png]]
## 考え方
最小値を最大化するという問題では、二分探索が有効な場合が多い。
最も短いものの長さをxと置き、x以上で羊羹を切った時にピースがK+1個以上になったら当然K＋１個として切ることができる。
これをcheck関数とし、このcheck関数をぎりぎりtrueになるxを二分探索で探していきたい

まず入力を受けるところから
```python
N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))
```

			canCutWithMinLength関数について考えていく。
これはまずcutCountと、prePositionを0で初期化する
```python
def canCutWithMinLength(minLength):
    cutCount = 0
    prePosition = 0
```

その後、for文で0からN-1の範囲内でA[i]についてチェックしていく。
A[i]-prePosition>=minLengthだったらA[i]で切ってもいいので、cutCountを増やし、prePositionを今切った位置で更新する
```python
def canCutWithMinLength(minLength):
    cutCount = 0
    prePosition = 0

    for i in range(N):
        if A[i] - prePosition >= x:
            cutCount += 1
            prePosition = A[i]
```

それで、forループを抜けた後に、最後の切れ目と端についても考えないといけない。
これは切った段階で数えていくから、端で切れているかについてforループだけでは考えられない。
もし、L - prePosition(i = N)がminLengthよりも小さければ、prePosition段階では切らず、端を最後の切れ目にしないといけないし、大きいのならば、cutCountはさらに一つ増えることになる
```python
def canCutWithMinLength(minLength):
    cutCount = 0
    prePosition = 0

    for i in range(N):
        if A[i] - prePosition >= x:
            cutCount += 1
            prePosition = A[i]
    
    if L - prePosition >= minLength:
        cutCount += 1
```

そしてこのcutCountがもし本来切らないといけないK＋１よりも多いなら、当然K+1個の切れ端を全部minLength以上の長さできることもできる
```python
def canCutWithMinLength(minLength):
    cutCount = 0
    prePosition = 0

    for i in range(N):
        if A[i] - prePosition >= x:
            cutCount += 1
            prePosition = A[i]
    
    if (L - prePosition) >= minLength:
        cutCount += 1
    
    return (cutCount >= K + 1)
```

そして、この関数で判定できる一番大きいminLengthを探していく。
leftを絶対にtrueにできる数(-1), rightを絶対にfalseになるL+1にしていく。
そして、midを(left+right) // 2にして、whileで探す範囲が1よりも大きい、つまりこの間の中でさらに整数が見つかる範囲で探す。絶対にleftかrightは整数なわけだから、1より小さい範囲で探しても整数が見つかるはずがない
left = mid, right = midとするのは、midを答え候補に含むため。普通の二分探索はkey == midではなかった時点でmidは答えの候補から外れるから考えなくてもいい。でも今回は最大のmidを探しているのでまだ答えに含まれる可能性がある。
```python
left = -1
right = L + 1

while right - left > 1:
    mid = (left + right) // 2
    if canCutWithMinLength(mid):
        left = mid # この時点でmidが答えから外れないからleftにmidを含める
    else:
        right = mid # 同様。この時点でmidが答えの可能性もあるのでrightにmidを含める
```

そして最後に答えがなにになるかという話。このコードブロックで何をしているのかというと、まずleftを絶対にcanCutがtrue、 rightがfalseになるように更新してきた。だから最終的にループが終わった後、leftとrightの間に整数が含まれなくなった時、leftをprintすれば済む
```python
left = -1
right = L + 1

while right - left > 1:
    mid = (left + right) // 2
    if canCutWithMinLength(mid):
        left = mid # この時点でmidが答えから外れないからleftにmidを含める
    else:
        right = mid # 同様。この時点でmidが答えの可能性もあるのでrightにmidを含める
print(left)
```
## 解説
https://drken1215.hatenablog.com/entry/2021/06/12/020300
```python
# coding: utf-8
# 入力
N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

# 判定問題 (すべての長さを x 以上にすることは可能か？)
def check(x):
    num = 0  # 何個切れたか
    pre = 0  # 前回の切れ目
    for i in range(N):
        # x を超えたら切断
        if A[i] - pre >= x:
            num += 1
            pre = A[i]

    # 最後のピースが x 以上なら加算
    if L - pre >= x:
        num += 1
	# なんで（）で囲むのかな？ほかのif文の条件式のところは囲まれてないからすごく違和感がある。いらないらしいです
    return (num >= K + 1)

# 二分探索
left, right = -1, L + 1
while right - left > 1:
    mid = (left + right) // 2
    if check(mid):
        left = mid
    else:
        right = mid
print(left)
```

if L - pre >= x:
        num += 1
ここが疑問。L-preがx以上だった時って、preの最後はA[N]であることを考えると、return falseじゃないの？

→そもそも全部の断片がx以上であることを判定する関数。
これ例えば、最後のpreがA[N]だったと仮定して、L-preがxを超えたらnumを加算した場合、実際のnumとずれない？だってA[N]より先に切れ目はなく、仮にL-A[N]がxを超えていたところで切れ目がないので切れないという話ではない。
なぜなら、この場合、前の切れ目からA[N]までがx以上であるから、A[N]で切れるって話。仮にL-A[N]がx未満だったらA[N]で切れるけど切らないし、x以上だったらA[N]で切ってさらにもう一個増やせるしって感じになる。

だからまとめるとcheck関数というのは、x以上の長さでようかんを切り分けていったときに、その数が実際に切り分けないといけないK＋１個よりも多かったらK＋１個でも分けられるということだからtrueを返すよって話

だから、この関数で判定できるxを二分探索で探すというのはわかった。
でも初期値がなぜleft = -1, right = L + 1になるのかがわからないし、right - left > 1のときにwhile文を続けるのかもわからない。だってLが仮に0だったとしても、right - leftは２になるからwhile文続いちゃうじゃん 
→leftは絶対にtrueになって、rightは確実にfalseでなるもので挟みたい。ここでいうleft, rightはxを探したい範囲の指定。だからleftは絶対にすべての断片が超えているに決まっている-1, rightは絶対に越えられないに決まっているL+1
whileがright - left > 1なのは、right - left == 1のときにもう探しても仕方がないから。探したいのはあくまでも整数の値であることを考えたときに、長さ1の中から探しても仕方がないじゃん？って話

最後にpythonの入力の受け方について質問させて。
```python
N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))
```
これどういうことなん？splitとmapがわからん
```python
N, L = map(int, input().split())
```
はまずinputは一行分を一つの文字列として受け取る。
splitはそれを空白文字で分割してリストにする。
map(int, list)はlistの要素を分解して全部int型に変換