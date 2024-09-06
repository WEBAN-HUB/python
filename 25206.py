point = 0
grade = 0
for i in range(20):
    s,p,g = map(str,input().split())
    p = float(p)
    if g == "A+":
        point += p
        grade += p*4.5
    elif g == "A0":
        point += p
        grade += p*4
    elif g == "B+":
        point += p
        grade += p*3.5
    elif g == "B0":
        point += p
        grade += p*3
    elif g == "C+":
        point += p
        grade += p*2.5
    elif g == "C0":
        point += p
        grade += p*2
    elif g == "D+":
        point += p
        grade += p*1.5
    elif g == "D0":
        point += p
        grade += p       
    elif g == "F":
        point += p
    elif g == "P":
        pass
print(grade/point)