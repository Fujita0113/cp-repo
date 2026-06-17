実行時間制限: 2 sec / メモリ制限: 1024 MiB

配点: $200$ 点

### 問題文

人 $1$ から人 $N$ の $N$ 人がギフトを送り合いました。

人 $i$ は人 $A_{i,1},A_{i,2},\ldots,A_{i,K_i}$ の $K_i$ 人にギフトを送りました。

$i=1,2,\ldots,N$ に対し、人 $i$ にギフトを送った人を全て求めてください。

### 制約

- $2\le N\le 100$
- $1\le K_i\le N-1$
- $1\le A_{i,1} < A_{i,2} < \cdots < A_{i,K_i}\le N$
- $A_{i,j} \neq i$
- 入力される値は全て整数

---

### 入力

入力は以下の形式で標準入力から与えられる。

```
NN
K1K_1 A1,1A_{1,1} A1,2A_{1,2} …\ldots A1,K1A_{1,K_1}
K2K_2 A2,1A_{2,1} A2,2A_{2,2} …\ldots A2,K2A_{2,K_2}
⋮\vdots
KNK_N AN,1A_{N,1} AN,2A_{N,2} …\ldots AN,KNA_{N,K_N}
```

### 出力

$N$ 行出力せよ。

$i$ 行目には、人 $i$ にギフトを送った人の番号を昇順に $B_1,B_2,\ldots,B_{X}$ （ただし $X$ は人 $i$ にギフトを送った人数）としたとき、以下の形式で出力せよ。

```
XX B1B_1 B2B_2 …\ldots BXB_X
```

---

### 入力例 1

```
4
1 2
1 3
1 2
3 1 2 3
```

### 出力例 1

```
1 4
3 1 3 4
2 2 4
0
```

人 $1$ は人 $2$ に、人 $2$ は人 $3$ に、人 $3$ は人 $2$ に、人 $4$ は人 $1,2,3$ にギフトを送りました。

人 $1$ は人 $4$ からギフトを送られました。したがって、 $1$ 行目には `1 4` を出力してください。

人 $2$ は人 $1,3,4$ からギフトを送られました。したがって、 $2$ 行目には `3 1 3 4` を出力してください。

人 $3$ は人 $2,4$ からギフトを送られました。したがって、 $3$ 行目には `2 2 4` を出力してください。

人 $4$ は誰からもギフトを送られませんでした。したがって、 $4$ 行目には `0` を出力してください。

---

### 入力例 2

```
4
3 2 3 4
2 1 4
2 1 2
2 2 3
```

### 出力例 2

```
2 2 3
3 1 3 4
2 1 4
2 1 2
```

---

### 入力例 3

```
7
1 3
4 3 4 6 7
1 7
3 2 6 7
2 3 7
1 4
1 5
```

### 出力例 3

```
0
1 4
3 1 2 5
2 2 6
1 7
2 2 4
4 2 3 4 5
```

Score: $200$ points

### Problem Statement

$N$ people, numbered $1$ through $N$, exchanged gifts with each other.

Person $i$ sent gifts to $K_i$ people: persons $A_{i,1}, A_{i,2}, \ldots, A_{i,K_i}$.

For each $i = 1, 2, \ldots, N$, find all people who sent a gift to person $i$.

### Constraints

- $2\le N\le 100$
- $1\le K_i\le N-1$
- $1\le A_{i,1} < A_{i,2} < \cdots < A_{i,K_i}\le N$
- $A_{i,j} \neq i$
- All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
NN
K1K_1 A1,1A_{1,1} A1,2A_{1,2} …\ldots A1,K1A_{1,K_1}
K2K_2 A2,1A_{2,1} A2,2A_{2,2} …\ldots A2,K2A_{2,K_2}
⋮\vdots
KNK_N AN,1A_{N,1} AN,2A_{N,2} …\ldots AN,KNA_{N,K_N}
```

### Output

Output $N$ lines.

For the $i$ -th line, let $B_1, B_2, \ldots, B_X$ be the numbers of the people who sent a gift to person $i$, listed in ascending order (where $X$ is the count of people who sent a gift to person $i$), and output in the following format:

```
XX B1B_1 B2B_2 …\ldots BXB_X
```

---

### Sample Input 1

```
4
1 2
1 3
1 2
3 1 2 3
```

### Sample Output 1

```
1 4
3 1 3 4
2 2 4
0
```

Person $1$ sent a gift to person $2$, person $2$ sent a gift to person $3$, person $3$ sent a gift to person $2$, and person $4$ sent gifts to persons $1, 2, 3$.

Person $1$ received a gift from person $4$. Thus, output `1 4` on the first line.

Person $2$ received gifts from persons $1, 3, 4$. Thus, output `3 1 3 4` on the second line.

Person $3$ received gifts from persons $2, 4$. Thus, output `2 2 4` on the third line.

Person $4$ did not receive any gifts. Thus, output `0` on the fourth line.

---

### Sample Input 2

```
4
3 2 3 4
2 1 4
2 1 2
2 2 3
```

### Sample Output 2

```
2 2 3
3 1 3 4
2 1 4
2 1 2
```

---

### Sample Input 3

```
7
1 3
4 3 4 6 7
1 7
3 2 6 7
2 3 7
1 4
1 5
```

### Sample Output 3

```
0
1 4
3 1 2 5
2 2 6
1 7
2 2 4
4 2 3 4 5
```

---

2026-06-15 (月)  
12:00:49 +09:00