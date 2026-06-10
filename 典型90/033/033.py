def convert_num(num):
    if num % 2 == 0:
        return num // 2
    else:
        return num // 2 + 1
H, W = map(int, input().split())

if H == 1 or W == 1:
    print(H * W)
else:
    print(convert_num(H) * convert_num(W))