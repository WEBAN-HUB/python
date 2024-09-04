a,b = [ int(x[::-1]) for x in input().split()]
print(a if a>b else b)