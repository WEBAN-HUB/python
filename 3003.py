nlist = list(map(int,input().split()))
chs = [1,1,2,2,2,8]
for index, value in enumerate(chs):
    print(value - nlist[index],end=" ")