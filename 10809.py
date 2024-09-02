S = input()
alphaList = [chr(i) for i in range(97,123)]
printAlpha = []
for alpha in alphaList:
    if alpha not in S:
        printAlpha.append(-1)
    else:
        printAlpha.append(S.index(alpha))
print(*printAlpha,sep=" ")