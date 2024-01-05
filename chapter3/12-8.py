array = list(input())
a = list()
b = 0

print(array)

for i in range(len(array)):
    if array[i].isalpha():
        a.append(array[i])
    else:
        b += int(array[i])

a.sort()
a = ''.join(a)

result = ''
result += str(a)
result += str(b)

print(result)