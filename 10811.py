N, M = map(int, input().split())
nList = [i for i in range(1, N + 1)]
for _ in range(M):
    i, j = map(int, input().split())
    nList[i - 1 : j] = reversed(nList[i - 1 : j])
print(*nList, sep=" ")