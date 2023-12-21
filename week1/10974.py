from itertools import permutations

n = int(input())
arr = [_ for _ in range(1, n+1)]
i = permutations(arr, n)

for k in i:
    for j in k:
        print(j, end=" ")
    print()