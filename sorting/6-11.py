n = int(input())

array = []
for i in range(n):
    array.append(input())

array = sorted(key=array[1])

for i in range(n):
    print(array[0], end=' ')