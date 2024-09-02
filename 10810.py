N, M = map(int,input().split())

nlist = [0 for i in range(N)]

for i in range(0,M):
    i, j, k = map(int, input().split())
    for num in range(i-1,j):
        nlist[num] = k
for value in nlist:
    print(value,end=" ")
    