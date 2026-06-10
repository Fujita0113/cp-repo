from collections import deque

Q = int(input())
collection = []
for _ in range(Q):
    t, x = map(int, input().split())
    collection.append((t, x))

dq = deque()

for t, x in collection:
    if t == 1:
        dq.appendleft(x)
    elif t == 2:
        dq.append(x)
    else:
        print(dq[x - 1])