import math

S = input()
output = 1
for i in range(math.ceil(len(S)/2)):
    if S[i] != S[-i-1]:
        output = 0
print(output)
