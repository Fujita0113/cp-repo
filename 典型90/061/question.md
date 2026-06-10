-   [トップ](https://atcoder.jp/contests/typical90)
-   [問題](https://atcoder.jp/contests/typical90/tasks)
-   [質問](https://atcoder.jp/contests/typical90/clarifications)
-   [提出](https://atcoder.jp/contests/typical90/submit?taskScreenName=typical90_bi)
-   [提出結果](https://atcoder.jp/contests/typical90/tasks/typical90_bi#)
-   [コードテスト](https://atcoder.jp/contests/typical90/custom_test)
-   [解説](https://atcoder.jp/contests/typical90/editorial)

061 - Deck（★2） [解説](https://atcoder.jp/contests/typical90/tasks/typical90_bi/editorial)

___

実行時間制限: 2 sec / メモリ制限: 1024 MiB

配点: $2$ 点

### 問題文

あなたはカードを整理するために $1$ つの山札を作ります。 最初、山札にカードは $1$ 枚もありません。

これから $Q$ 個の操作を行います。$i$ 番目 $(1 \leq i \leq Q)$ の操作では以下を行います：

-   $t_i = 1$ のとき、整数 $x_i$ が書かれたカードを山札の一番上にいれる
-   $t_i = 2$ のとき、整数 $x_i$ が書かれたカードを山札の一番下にいれる
-   $t_i = 3$ のとき、山札の上から $x_i$ 番目のカードに書かれた数を紙に書き出す

$t_i = 3$ の操作で書き出された整数を操作順に出力するプログラムを書いてください。

### 制約

-   $2 \leq Q \leq 10^5$
-   $1 \leq t_i \leq 3$
-   $t_i = 1, 2$ のとき $1 \leq x_i \leq 10^9$
-   $t_i = 3$ のとき $1 \leq x_i \leq k_i$（$k_i$ は $1 \leq j \leq i$ かつ $t_j = 1, 2$ を満たす $j$ の個数）
-   $t_i = 1, 2$ を満たす $i$ が少なくとも $1$ つ存在する
-   $t_i = 3$ を満たす $i$ が少なくとも $1$ つ存在する
-   与えられる入力は全て整数

___

### 入力

入力は以下の形式で標準入力から与えられます。

```
QQ
t1t_1 x1x_1
t2t_2 x2x_2
::
tQt_Q xQx_Q
```

### 出力

与えられた $Q$ 個の操作のうち $t_i = 3$ の操作で書き出した整数を順に、改行で区切って $1$ 行ずつ出力してください。

___

### 入力例 1Copy

Copy

```
6
1 2
1 1
2 3
3 1
3 2
3 3
```

### 出力例 1Copy

Copy

```
1
2
3
```

山札は各操作の後に次の状態になります。

-   $1$ 番目の操作の直後：カードに書かれた整数は上から順に $(2)$ である
-   $2$ 番目の操作の直後：カードに書かれた整数は上から順に $(1, 2)$ である
-   $3$ 番目の操作以降：カードに書かれた整数は上から順に $(1, 2, 3)$ である

したがって、書き出された数は順番に $1$、$2$、$3$ となります。

___

### 入力例 2Copy

Copy

```
6
2 1
3 1
2 2
3 1
2 3
3 1
```

### 出力例 2Copy

Copy

```
1
1
1
```

カードを山札の一番下にいれる操作のみを行います。

最初、$1$ が書かれたカードを山札にいれるので、$t_i = 3$ で書き出す数は常に $1$ となります。　

___

### 入力例 3Copy

Copy

```
6
1 1000000000
2 200000000
1 30000000
2 4000000
1 500000
3 3
```

### 出力例 3Copy

Copy

```
1000000000
```

___

### 出典

[「競プロ典型90問」61日目](https://twitter.com/e869120/status/1402034055734980608)

___

言語

Python (PyPy 3.11-v7.3.20)

ソースコード

※ 512 KiB まで

___