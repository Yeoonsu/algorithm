from itertools import combinations

s = list(map(int, input().split()))
n = s[0]

for i in range(7, n+1):
    comb = list(combinations(s[1:], i))
    if len(comb) == n:
        print(comb)