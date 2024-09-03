T = int(input())
for index in range(T):
    R, S = map(str,input().split())
    printStr = ""
    for chara in S:
        printStr += chara*int(R)
    print(printStr)