n = int(input())
score = list(map(int, input().split()))
avg = (sum(score) / max(score) * 100) / n
print(avg)