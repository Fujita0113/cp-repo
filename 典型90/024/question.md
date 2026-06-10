-   [トップ](https://atcoder.jp/contests/typical90)
-   [問題](https://atcoder.jp/contests/typical90/tasks)
-   [質問](https://atcoder.jp/contests/typical90/clarifications)
-   [提出](https://atcoder.jp/contests/typical90/submit?taskScreenName=typical90_x)
-   [提出結果](https://atcoder.jp/contests/typical90/tasks/typical90_x#)
-   [コードテスト](https://atcoder.jp/contests/typical90/custom_test)
-   [解説](https://atcoder.jp/contests/typical90/editorial)

024 - Select +／- One（★2） [解説](https://atcoder.jp/contests/typical90/tasks/typical90_x/editorial)

___

実行時間制限: 2 sec / メモリ制限: 1024 MiB

配点: $2$ 点

### 問題文

長さ $N$ の正整数列 $A = (A_1, A_2, \ldots, A_N)$ および $B = (B_1, B_2, \ldots, B_N)$ が与えられます。

次の操作を**ちょうど** $K$ 回行うことで $A$ を $B$ に一致させることができるか判定してください。

操作：$1 \leq i \leq N$ を満たす $i$ をひとつ選び $A_i$ を $A_i - 1$ または $A_i + 1$ に置き換える

### 制約

-   $1 \leq N \leq 1000$
-   $1 \leq K \leq 10^9$
-   $1 \leq A_i, B_i \leq 10^6 \ (1 \leq i \leq N)$
-   入力は全て整数

___

### 入力

入力は以下の形式で標準入力から与えられます。

```
NN KK
A1A_1 A2A_2 ⋯\cdots ANA_N
B1B_1 B2B_2 ⋯\cdots BNB_N
```

### 出力

ちょうど $K$ 回の操作で $A$ を $B$ に一致させることができる場合は `Yes` を、そうでない場合は `No` を出力してください。

___

### 入力例 1Copy

Copy

```
2 5
1 3
2 1
```

### 出力例 1Copy

Copy

```
Yes
```

たとえば、次のようにちょうど $5$ 回の操作で $A$ を $B$ に一致させることができます。

-   $i = 1$ を選び、$A_1$ を $A_1 - 1$ で置き換える。すると、$A$ は $(0, 3)$ になる
-   $i = 2$ を選び、$A_2$ を $A_2 - 1$ で置き換える。すると、$A$ は $(0, 2)$ になる
-   $i = 2$ を選び、$A_2$ を $A_2 - 1$ で置き換える。すると、$A$ は $(0, 1)$ になる
-   $i = 1$ を選び、$A_1$ を $A_1 + 1$ で置き換える。すると、$A$ は $(1, 1)$ になる
-   $i = 1$ を選び、$A_1$ を $A_1 + 1$ で置き換える。すると、$A$ は $(2, 1)$ になり、$B$ に一致する

___

### 入力例 2Copy

Copy

```
3 1
7 8 9
7 8 9
```

### 出力例 2Copy

Copy

```
No
```

ちょうど $1$ 回操作をすると $A$ は以下のいずれかになります。

-   $(6, 8, 9)$
-   $(8, 8, 9)$
-   $(7, 7, 9)$
-   $(7, 9, 9)$
-   $(7, 8, 8)$
-   $(7, 8, 10)$

これらは全て $B$ に一致しないため `No` を出力してください。

___

### 入力例 3Copy

Copy

```
7 999999999
3 1 4 1 5 9 2
1 2 3 4 5 6 7
```

### 出力例 3Copy

Copy

```
Yes
```

___

### 出典

[「競プロ典型90問」24日目](https://twitter.com/e869120/status/1386449961072553990)

___

言語

Python (PyPy 3.11-v7.3.20)

ソースコード

※ 512 KiB まで

___