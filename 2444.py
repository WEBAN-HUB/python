N = int(input())
for i in range(0,N):
    print(" "*(N-i-1)+ "*"*(1+(i*2)))
for j in range(0,N-1):
    print(" "*(1+j)+"*"*(((N-1-j)*2)-1))