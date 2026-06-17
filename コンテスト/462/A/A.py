# def checkNum(char):
#     return char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9" or char == "0"

# S = input()
# res = ""

# for i in range(len(S)):
#     if checkNum(S[i]):
#        res = res + S[i]
# print(res)

S = input()
print("".join(c for c in S if c.isdigit()))