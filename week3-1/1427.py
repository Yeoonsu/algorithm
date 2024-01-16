
n = list(input())

n.sort(key=lambda x: -int(x))

print(''.join(n))