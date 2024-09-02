N, M = map(int,input().split())
nList = list(range(1,N+1))

for index in range(0,M):
    i, j = map(int,input().split())
    rList = []
    for num in range(i-1, j):
        rList.append(nList[num])
    rList.reverse()
    for index, value in enumerate(range(i-1, j)):
        nList[value] = rList[index]
print(*nList)