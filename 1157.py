s = input().upper()
max = ""
count = 0
for value in s:
    if s.count(value) > count:
        max = value
        count = s.count(value)
    elif s.count(value) == count and max != value:
        max = '?'
print(max)