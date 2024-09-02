import sys

N = int(sys.stdin.readline())
nList = list(map(int,input().split()))
print(min(nList),max(nList),sep=" ")
