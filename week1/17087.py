import math

n, s = map(int, input().split())
distance = list(map(int, input().split()))

result = []

for i in distance:
    result.append(abs(s-i))

ans = result[0]
for i in range(1, n):
    ans=math.gcd(result[i], ans)

print(ans)