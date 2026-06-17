A - Secret Numbers

---

実行時間制限: 2 sec / メモリ制限: 1024 MiB

配点: $100$ 点

### 問題文

英小文字と数字のみからなる文字列 $S$ が与えられます。

$S$ から数字である文字だけを取り出し、元の順序のまま並べた文字列を求めてください。

### 制約

- $S$ は英小文字と数字のみからなる長さ $1$ 以上 $50$ 以下の文字列

---

### 入力

入力は以下の形式で標準入力から与えられる。

```
SS
```

### 出力

答えを出力せよ。

---

### 入力例 1

```
abc462
```

### 出力例 1

```
462
```

`abc462` に含まれる数字は `4`, `6`, `2` です。これらを元の順序のまま連結すると `462` となります。したがって、 `462` を出力してください。

---

### 入力例 2

```
codequeen
```

### 出力例 2

`codequeen` に数字は含まれないので空文字列を出力してください。

---

### 入力例 3

```
31415
```

### 出力例 3

```
31415
```

---

### 入力例 4

```
10plus2is12
```

### 出力例 4

```
10212
```

Score: $100$ points

### Problem Statement

You are given a string $S$ consisting of lowercase English letters and digits.

Extract only the digit characters from $S$ and output the string formed by arranging them in their original order.

### Constraints

- $S$ is a string of length between $1$ and $50$, inclusive, consisting of lowercase English letters and digits.

---

### Input

The input is given from Standard Input in the following format:

```
SS
```

### Output

Output the answer.

---

### Sample Input 1

```
abc462
```

### Sample Output 1

```
462
```

The digits contained in `abc462` are `4`, `6`, `2`. Concatenating them in their original order gives `462`. Thus, output `462`.

---

### Sample Input 2

```
codequeen
```

### Sample Output 2

`codequeen` contains no digits, so output the empty string.

---

### Sample Input 3

```
31415
```

### Sample Output 3

```
31415
```

---

### Sample Input 4

```
10plus2is12
```

### Sample Output 4

```
10212
```

---

2026-06-15 (月)  
11:17:47 +09:00