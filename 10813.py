N, M = map(int,input().split())
nlist = [i + 1 for i in range(N)]
for i in range(M):
    i, j = map(int,input().split())
    temp = nlist[i-1]
    nlist[i-1] = nlist[j-1]
    nlist[j-1] = temp
print(*nlist,sep=" ")