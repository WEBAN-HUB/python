a=list()
for i in range(28):
  m=int(input())
  a.append(m)

for i in range(1,31):
  if i not in a:
    print(i)