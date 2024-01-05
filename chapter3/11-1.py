n = int(input())
array = list(map(int, input().split()))
array.sort()

group = 0
man = 0

for i in array:
    man += 1
    if man >= i:
        group += 1
        man = 0

print(group)