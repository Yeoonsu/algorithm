import math

def sosu(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

N = int(input())

for i in range(N):
    num = int(input())
    a, b = num//2, num//2

    for _ in range(num//2):
        if sosu(a) and sosu(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1