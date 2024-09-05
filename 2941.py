croa = ["c=","c-","dz=","d-","lj","nj","s=","z="]
s = input()
count = 0 
for value in croa:
    count += s.count(value)
    s = s.replace(value," ")
s=s.replace(" ", "")
print(count+len(s))