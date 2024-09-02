N, M = map(int,input().split())
nlist = list(range(1,N+1))
for i in range(M):
    i, j = map(int,input().split())
    nlist[i-1], nlist[j-1] = nlist[j-1], nlist[i-1]
print(*nlist,sep=" ")