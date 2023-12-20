from itertools import combinations

n, s = map(int, input().split())

arr = [_ for _ in range(1, n+1)]

for i in combinations(arr, s):
    print(*i)