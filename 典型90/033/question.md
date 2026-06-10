-   [トップ](https://atcoder.jp/contests/typical90)
-   [問題](https://atcoder.jp/contests/typical90/tasks)
-   [質問](https://atcoder.jp/contests/typical90/clarifications)
-   [提出](https://atcoder.jp/contests/typical90/submit?taskScreenName=typical90_ag)
-   [提出結果](https://atcoder.jp/contests/typical90/tasks/typical90_ag#)
-   [コードテスト](https://atcoder.jp/contests/typical90/custom_test)
-   [解説](https://atcoder.jp/contests/typical90/editorial)

033 - Not Too Bright（★2） [解説](https://atcoder.jp/contests/typical90/tasks/typical90_ag/editorial)

___

実行時間制限: 1 sec / メモリ制限: 1024 MiB

配点: $2$ 点

### 問題文

E869120 くんは、冬に公開するイルミネーションを作成することを計画しています。

E869120 くんが計画しているイルミネーションは、縦 $H$ $\times$ 横 $W$ の $HW$ 個のLEDで構成されます。

イルミネーションの各 LED は、点灯・消灯の状態を任意に切り替えることができます。

このイルミネーションは、以下の条件を満たすとき **不適切である** といいます。

-   イルミネーション全体に完全に含まれる 縦 $2$ $\times$ 横 $2$ の、$4$ つの LED を含む領域であって、点灯している LED が領域内に $2$ つ以上あるものが存在する。

適切な（不適切な状態ではない）イルミネーションの点灯パターンのうち、点灯している LED の個数としてありうる最大値を求めてください。

### 制約

-   $1 \leq H, W \leq 100$
-   入力はすべて整数

___

### 入力

入力は以下の形式で標準入力から与えられます。

```
HH WW
```

### 出力

答えを出力してください。

___

### 入力例 1Copy

Copy

```
2 3
```

### 出力例 1Copy

Copy

```
2
```

点灯している LED を `'#'`、消灯している LED を `'.'` とすると、たとえば以下の状態が、適切である中で点灯している LED の個数が最大となります。

```
#.#
...
```

一方、以下の状態は不適切であるため、条件を満たしません。

上から $1$ ～ $2$ つ目、左から $1$ ～ $2$ つ目の LED からなる領域内に点灯している LED が $2$ つ存在します。

```
#.#
.#.
```

___

### 入力例 2Copy

Copy

```
3 4
```

### 出力例 2Copy

Copy

```
4
```

たとえば以下の状態が、適切である中で点灯している LED の個数が最大となります。

```
#..#
....
#..#
```

___

### 入力例 3Copy

Copy

```
3 6
```

### 出力例 3Copy

Copy

```
6
```

___

### 出典

[「競プロ典型 90 問」33 日目](https://twitter.com/e869120/status/1390074137192767489)

___

言語

Python (PyPy 3.11-v7.3.20)

ソースコード

※ 512 KiB まで

___