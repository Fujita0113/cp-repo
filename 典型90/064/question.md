-   [トップ](https://atcoder.jp/contests/typical90)
-   [問題](https://atcoder.jp/contests/typical90/tasks)
-   [質問](https://atcoder.jp/contests/typical90/clarifications)
-   [提出](https://atcoder.jp/contests/typical90/submit?taskScreenName=typical90_bl)
-   [提出結果](https://atcoder.jp/contests/typical90/tasks/typical90_bl#)
-   [コードテスト](https://atcoder.jp/contests/typical90/custom_test)
-   [解説](https://atcoder.jp/contests/typical90/editorial)

064 - Uplift（★3） [解説](https://atcoder.jp/contests/typical90/tasks/typical90_bl/editorial)

___

実行時間制限: 2 sec / メモリ制限: 1024 MiB

配点: $3$ 点

### 問題文

日本は $N$ 個の区画に分けられており、西から $i$ 番目の区画（以下、区画 $i$ とする）の標高は $A_i$ です。

これから $Q$ 回の地殻変動が起こります。$i$ 回目の地殻変動では、区画 $L_i, L_i+1, \cdots, R_i$ の標高が $V_i$ だけ変化します。（$V_i \geq 0$ のとき標高が $|V_i|$ 上がり、$V_i < 0$ のとき標高が $|V_i|$ 下がることを意味します）

さて、区画 $1$ から $N$ へ行く際の**不便さ**は次のように定義されます。

> 区画 $i$ の標高を $E_i$ とするとき、不便さは $|E_1 - E_2| + |E_2 - E_3| + \cdots + |E_{N-1} - E_N|$

各地殻変動後の**不便さ**をそれぞれ求めてください。

### 制約

-   $1 \leq N, Q \leq 10^{5}$
-   $-10^{9} \leq A_i, V_i \leq 10^{9}$
-   $1 \leq L_i \leq R_i \leq N$
-   入力は全て整数

___

### 入力

入力は以下の形式で標準入力から与えられます。

```
NN QQ
A1A_1 A2A_2 ⋯\cdots ANA_N
L1L_1 R1R_1 V1V_1
L2L_2 R2R_2 V2V_2
⋮\vdots
LQL_Q RQR_Q VQV_Q
```

### 出力

$Q$ 行出力してください。

$i$ 行目には、$i$ 番目の地殻変動が終わった後の不便さを出力してください。

___

### 入力例 1Copy

Copy

```
3 3
1 2 3
2 3 1
1 2 -1
1 3 2
```

### 出力例 1Copy

Copy

```
3
4
4
```

$1$ 回目の地殻変動後の各区画の標高は、西から順に $1, 3, 4$ であり、不便さは $|1 - 3| + |3 - 4| = 3$ です。

$2$ 回目の地殻変動後の各区画の標高は、西から順に $0, 2, 4$ であり、不便さは $|0 - 2| + |2 - 4| = 4$ です。

$3$ 回目の地殻変動後の各区画の標高は、西から順に $2, 4, 6$ であり、不便さは $|2 - 4| + |4 - 6| = 4$ です。

___

### 入力例 2Copy

Copy

```
20 10
61 51 92 -100 -89 -65 -89 -64 -74 7 87 -2 51 -39 -50 63 -23 36 74 37
2 2 -45
6 19 82
2 9 36
7 13 71
16 20 90
18 20 -24
14 17 -78
10 11 -55
7 19 -26
20 20 -7
```

### 出力例 2Copy

Copy

```
1164
1328
1256
1350
1440
1416
1572
1482
1430
1437
```

___

### 出典

[「競プロ典型90問」64日目](https://twitter.com/e869120/status/1403121388773249024)

___

言語

Python (PyPy 3.11-v7.3.20)

ソースコード

※ 512 KiB まで

___