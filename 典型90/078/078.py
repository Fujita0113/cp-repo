N, M = map(int, input().split())
slides = [list(map(int, input().split())) for _ in range(M)]

count = [0] * N
appeared = set()
for i in range(M):
    max_num = max(slides[i])
    if max_num not in appeared:
        appeared.add(max_num)
        count[max_num - 1] = 1
    else:
        count[max_num - 1] = 0
print(sum(count))