N = int(input())
group = 0
for i in range(N):
    s = input()
    chkGroup = []
    chkChr = ""
    add = 1
    for value in s:
        if chkChr != value:
            chkChr = value
            if value not in chkGroup:
                chkGroup.append(value)
            else:
                add = 0
    group += add
print(group)