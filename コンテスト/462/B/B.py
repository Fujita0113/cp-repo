# N = int(input())
# res = [[] for _ in range(N)]
# for j in range(N):
#     A = list(map(int, input().split()))
#     for i in range(1, A[0] + 1):
#         res[A[i] - 1].append(j)
# for val in res:
#     print(len(val), end = " ")
#     for num in val:
#         print(num + 1, end = " ")
#     print("")

N = int(input())
record = [[] for _ in range(N)]
for i in range(N):
    K, *A = map(int, input().split())
    for val in A:
        record[val - 1].append(i + 1)
for res in record:
    print(len(res), *res)