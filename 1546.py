N = int(input())
nList = list(map(int,input().split()))
nMax = max(nList)
total = 0
for value in nList:
    total += value/nMax*100
print(total/len(nList))
