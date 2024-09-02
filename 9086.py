T = int(input())
strList = []
for i in range(T):
    inputStr = input()
    strList.append(inputStr[0] + inputStr[-1])
print(*strList,sep="\n")