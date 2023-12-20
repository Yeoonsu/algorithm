# 백트래킹으로도 풀 수 있음
import itertools

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]

array = itertools.permutations(nums, m) 

for i in array:
    for j in i:
        print(j, end=' ')
    print()