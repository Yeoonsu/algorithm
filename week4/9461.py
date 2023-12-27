
def pado(n):
    n = [n-3] + [n-2]
    return n

T = int(input())
for i in range(T+1):
    print(pado(T))