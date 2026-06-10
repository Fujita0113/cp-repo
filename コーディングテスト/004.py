n = 8
num_list = []
for i in range(2 ** n):
    result = 0
    for j in range(n):
        if((i >> j) & 1):
            result += 1 * (10 ** j)
        else:
            result += 8 * (10 ** j)
    # resultにfor文が終わった段階で今回の8桁の整数が入る
    num_list.append(result)
num_list.sort(reverse=True)
for i in range(len(num_list)):
    if num_list[i] % 181 == 88:
        print(num_list[i])
        break