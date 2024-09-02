studentList = list(range(1,31))
nList = []
printN = []
for i in range(1,29):
    nList.append(int(input()))
for value in studentList:
    if value not in nList:
        printN.append(value)
printN.sort()
print(*printN, sep="\n")