S = input()
b = [['A','B','C'],['D','E','F'],['G','H',"I"],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
res = 0
for index in range(len(S)):
    for i, arr in enumerate(b):
        if S[index] in arr:
            res += 3+i
            break
print(res)