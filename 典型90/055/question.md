-   [トップ](https://atcoder.jp/contests/typical90)
-   [問題](https://atcoder.jp/contests/typical90/tasks)
-   [質問](https://atcoder.jp/contests/typical90/clarifications)
-   [提出](https://atcoder.jp/contests/typical90/submit?taskScreenName=typical90_bc)
-   [提出結果](https://atcoder.jp/contests/typical90/tasks/typical90_bc#)
-   [コードテスト](https://atcoder.jp/contests/typical90/custom_test)
-   [解説](https://atcoder.jp/contests/typical90/editorial)

055 - Select 5（★2） [解説](https://atcoder.jp/contests/typical90/tasks/typical90_bc/editorial)

___

実行時間制限: 5 sec / メモリ制限: 1024 MiB

配点: $2$ 点

### 問題文

$N$ 個の整数 $A_1$, $A_2$, $\cdots$, $A_N$ があります。 この中から $5$ 個を選ぶ方法のうち、これら $5$ 個の整数の積を $P$ で割ると $Q$ 余るようなものが何通りあるか求めてください。

### 制約

-   $5\leq N\leq 100$
-   $0\leq A_i\leq 10^9$
-   $0\leq Q < P\leq 10^9$
-   入力はすべて整数

___

### 入力

入力は、以下の形式で与えられます。

```
NN PP QQ
A1A_1 A2A_2 A3A_3 ⋯\cdots ANA_N
```

### 出力

この問題の答えを $1$ 行に出力してください。

___

### 入力例 1Copy

Copy

```
6 7 1
1 2 3 4 5 6
```

### 出力例 1Copy

Copy

```
1
```

$A_1,A_2,A_3,A_4,A_5$ を選んだときのみ、積を $7$ で割った余りが $1$ になります。

___

### 入力例 2Copy

Copy

```
10 1 0
0 0 0 0 0 0 0 0 0 0
```

### 出力例 2Copy

Copy

```
252
```

___

### 出典

[「競プロ典型90問」55日目](https://twitter.com/e869120/status/1399496993014116352)

___

言語

Python (PyPy 3.11-v7.3.20)

ソースコード

※ 512 KiB まで

___