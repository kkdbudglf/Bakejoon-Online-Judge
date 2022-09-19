n, k = map(int, input().split())  # 동전 개수, 만드려는 돈 입력 받기
a = []
count = 0

for i in range(n):
    a.append(int(input()))

a.sort(reverse=True)  # 내림차순 정렬

for j in a:
    count += k // j
    k %= j

print(count)
