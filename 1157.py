s = input().upper()
sSet = list(set(s))
max = 0
chara = ""
for value in sSet:
    count = s.count(value)
    if max < count:
        chara = value
        max = count
    elif max == count:
        chara = "?"
print(chara)
