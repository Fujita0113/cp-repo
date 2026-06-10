-   [トップ](https://atcoder.jp/contests/typical90)
-   [問題](https://atcoder.jp/contests/typical90/tasks)
-   [質問](https://atcoder.jp/contests/typical90/clarifications)
-   [提出](https://atcoder.jp/contests/typical90/submit?taskScreenName=typical90_aa)
-   [提出結果](https://atcoder.jp/contests/typical90/tasks/typical90_aa#)
-   [コードテスト](https://atcoder.jp/contests/typical90/custom_test)
-   [解説](https://atcoder.jp/contests/typical90/editorial)

027 - Sign Up Requests （★2） [解説](https://atcoder.jp/contests/typical90/tasks/typical90_aa/editorial)

___

実行時間制限: 1 sec / メモリ制限: 1024 MiB

配点: $2$ 点

### 問題文

低橋くんはプログラミングコンテストサイト「LowCoder」を作り、サービスを開始しました。

今日の時点では、LowCoder にはユーザはいません。

今日から数えて $i$ $(1 \leq i \leq N)$ 日後には、ユーザ名 $S_i$ を希望するユーザが登録申請を行います。

申請を行った時点でユーザ名が $S_i$ であるユーザが存在する場合、その登録申請は無視されます。

そのようなユーザが存在しない場合は登録申請が受理され、LowCoder にそのユーザが登録されます。

何日目の登録申請が受理されるかを求めてください。

### 制約

-   $1 \leq N \leq 10^5$
-   $S_i$ ($1 \leq i \leq N$) は英小文字および数字からなる $1$ 文字以上 $15$ 文字以下の文字列である。
    -   より正確には、$S_i$ は正規表現 `[a-z0-9]{1,15}` で表せる文字列である。

___

### 入力

入力は以下の形式で標準入力から与えられます。

```
NN
S1S_1
S2S_2
⋮\vdots
SNS_N
```

### 出力

今日から数えて何日目に送られる登録申請が受理されるか、昇順 (値の小さい順) に出力してください。

___

### 入力例 1Copy

Copy

```
5
e869120
atcoder
e869120
square1001
square1001
```

### 出力例 1Copy

Copy

```
1
2
4
```

$1$ 日目にはユーザ名 `e869120` が申請され、このユーザ名のユーザはいないため、LowCoder に登録されます。

$2$ 日目にはユーザ名 `atcoder` が申請され、このユーザ名のユーザはいないため、LowCoder に登録されます。

$3$ 日目にはユーザ名 `e869120` が申請されますが、このユーザ名のユーザは既に登録されているため、受理されません。

$4$ 日目にはユーザ名 `square1001` が申請され、このユーザ名のユーザはいないため、LowCoder に登録されます。

$5$ 日目にはユーザ名 `square1001` が申請されますが、このユーザ名のユーザは既に登録されているため、受理されません。

___

### 入力例 2Copy

Copy

```
4
taro
hanako
yuka
takashi
```

### 出力例 2Copy

Copy

```
1
2
3
4
```

受理されない登録申請が存在しない場合もあります。

___

### 入力例 3Copy

Copy

```
10
square869120
square869120
square869120
square869120
square869120
square869120
square869120
square869120
square869120
square869120
```

### 出力例 3Copy

Copy

```
1
```

$S_i$ がすべて同じである可能性もあります。

___

### 出典

[「競プロ典型90問」27問目](https://twitter.com/e869120/status/1387538790017769474)

___

言語

Python (PyPy 3.11-v7.3.20)

ソースコード

※ 512 KiB まで

___