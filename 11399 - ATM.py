n = int(input())
p = list(map(int, input().split()))

p.sort()
result = 0

for i in range(n):
    for j in range(i+1):
        result += p[j]

print(result)
