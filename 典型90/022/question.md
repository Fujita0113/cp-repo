-   [トップ](https://atcoder.jp/contests/typical90)
-   [問題](https://atcoder.jp/contests/typical90/tasks)
-   [質問](https://atcoder.jp/contests/typical90/clarifications)
-   [提出](https://atcoder.jp/contests/typical90/submit?taskScreenName=typical90_v)
-   [提出結果](https://atcoder.jp/contests/typical90/tasks/typical90_v#)
-   [コードテスト](https://atcoder.jp/contests/typical90/custom_test)
-   [解説](https://atcoder.jp/contests/typical90/editorial)

022 - Cubic Cake（★2） [解説](https://atcoder.jp/contests/typical90/tasks/typical90_v/editorial)

___

実行時間制限: 2 sec / メモリ制限: 1024 MiB

配点：$2$ 点

### 問題文

幅 $A$、奥行き $B$、高さ $C$ の直方体の形をしたケーキがあります。

あなたはケーキに対して、次の操作を行うことができます。

-   ある面に平行な方向に切断する
-   ただし、ケーキは動かしてはならない（複数のケーキに分割されている場合、これらを変形したり、別々に切ることはできない）

最小何回の操作で、全てのピースを立方体にすることができますか？

### 制約

-   $1 \leq A, B, C \leq 10^{18}$
-   入力はすべて整数

___

### 入力

入力は以下の形式で標準入力から与えられます。

```
AA BB CC
```

### 出力

最小の操作回数を $1$ 行で出力してください。

___

### 入力例 1Copy

Copy

```
2 2 3
```

### 出力例 1Copy

Copy

```
4
```

$4$ 回ケーキを切断することで、一辺の長さが $1$ の立方体が $12$ 個できます。

___

### 入力例 2Copy

Copy

```
2 2 4
```

### 出力例 2Copy

Copy

```
1
```

$1$ 回ケーキを切断することで、一辺の長さが $2$ の立方体が $2$ 個できます。

___

### 入力例 3Copy

Copy

```
1000000000000000000 999999999999999999 999999999999999998
```

### 出力例 3Copy

Copy

```
2999999999999999994
```

オーバーフローに注意してください。

___

### 出典

[「競プロ典型90問」22日目](https://twitter.com/e869120/status/1385363292739104775)

___

言語

Python (PyPy 3.11-v7.3.20)

ソースコード

※ 512 KiB まで

___