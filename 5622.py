S = input()
res = 0
for index in range(len(S)):
    for i in range(8):
        if S[index] in [chr(65+(i*3)),chr(66+(i*3)),chr(67+(i*3))]:
            res = res + 3 + i
            break
print(res)