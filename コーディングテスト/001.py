result = 0
for i in range(1, 78, 1):
    if i % 2 == 0:
        result += -1 * (i ** 4)
    else:
        result += i ** 4
print(result)