import sys

nlist = []

for i in range(0,9):
    N = int(sys.stdin.readline())
    nlist.append(N)

N = 0
index = 0

for idx, value in enumerate(nlist):
    if N < value:
        N = value
        index = idx
print(str(N),index+1,sep="\n")