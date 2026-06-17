C - Not Covered Points

---

実行時間制限: 2 sec / メモリ制限: 1024 MiB

配点: $300$ 点

### 問題文

$2$ 次元平面上に点 $1$ から点 $N$ までの $N$ 個の点があります。点 $i$ $(1\le i\le N)$ の座標は $(X_i,Y_i)$ です。ここで、 $X,Y$ はそれぞれ $(1,2,\ldots,N)$ の順列であることが保証されます。

左下の頂点を $(0,0)$ 、右上の頂点を $(X_i,Y_i)$ とする $x$ 軸に平行な辺と $y$ 軸に平行な辺のみからなる長方形の内部（辺上を含まない）に点 $1$ から点 $N$ までの $N$ 個の点をどれも含まないような $i$ の個数を求めてください。

### 制約

- $1\le N\le 3\times 10^5$
- $1\le X_i,Y_i\le N$
- $X,Y$ はそれぞれ $(1,2,\ldots,N)$ の順列
- 入力される値は全て整数

---

### 入力

入力は以下の形式で標準入力から与えられる。

```
NN
X1X_1 Y1Y_1
X2X_2 Y2Y_2
⋮\vdots
XNX_N YNY_N
```

### 出力

答えを出力せよ。

---

### 入力例 1

```
3
2 1
1 3
3 2
```

### 出力例 1

```
2
```

$i=1,2$ の $2$ つが条件を満たします。

$i=3$ の場合、左下を $(0,0)$ 、右上を $(3,2)$ とする $x$ 軸に平行な辺を持つ長方形の内部（辺上を含まない）に点 $1$ を含みます。

---

### 入力例 2

```
5
1 1
4 2
2 3
5 5
3 4
```

### 出力例 2

```
1
```

---

### 入力例 3

```
7
3 4
6 1
5 5
2 7
7 2
1 3
4 6
```

### 出力例 3

```
2
```

Score: $300$ points

### Problem Statement

There are $N$ points numbered $1$ through $N$ on a two-dimensional plane. Point $i$ $(1\le i\le N)$ has coordinates $(X_i,Y_i)$. Here, it is guaranteed that $X$ and $Y$ are each permutations of $(1,2,\ldots,N)$.

Find the number of values of $i$ such that the interior (not including the boundary) of the rectangle with sides parallel to the $x$ -axis and $y$ -axis, with lower-left vertex $(0,0)$ and upper-right vertex $(X_i,Y_i)$, contains none of the $N$ points numbered $1$ through $N$.

### Constraints

- $1\le N\le 3\times 10^5$
- $1\le X_i,Y_i\le N$
- $X$ and $Y$ are each permutations of $(1,2,\ldots,N)$.
- All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
NN
X1X_1 Y1Y_1
X2X_2 Y2Y_2
⋮\vdots
XNX_N YNY_N
```

### Output

Output the answer.

---

### Sample Input 1

```
3
2 1
1 3
3 2
```

### Sample Output 1

```
2
```

The two values $i=1,2$ satisfy the condition.

For $i=3$, the interior (not including the boundary) of the rectangle with sides parallel to the $x$ -axis, with lower-left vertex $(0,0)$ and upper-right vertex $(3,2)$, contains point $1$.

---

### Sample Input 2

```
5
1 1
4 2
2 3
5 5
3 4
```

### Sample Output 2

```
1
```

---

### Sample Input 3

```
7
3 4
6 1
5 5
2 7
7 2
1 3
4 6
```

### Sample Output 3

```
2
```

---

2026-06-16 (火)  
18:35:11 +09:00