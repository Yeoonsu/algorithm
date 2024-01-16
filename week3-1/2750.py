
n = int(input())
arr = []

for _ in range(n):
    command = int(input())
    arr.append(command)
    arr.sort()

for i in range(n):
    print(arr[i])
