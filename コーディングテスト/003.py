result = []
result_truth = []
count = 0
for i in range(1, 101, 1):
    for j in range(i):
        if i % 3 == 0:
            result.append("Z")
            result.append("E")
            result.append("R")
            result.append("O")
            count += 4
        elif i % 3 == 1:
            result.append("O")
            result.append("N")
            result.append("E")
            count += 3
        else:
            result.append("T")
            result.append("W")
            result.append("O")
            count += 3
print(result)
for i in range(200, count + 1, 1000):
    result_truth.append(result[i - 1])
print("".join(result_truth))
    