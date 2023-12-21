
n, m = map(int, input().split())

def fact(i):
    num = 1
    for k in range(1, i+1):
        num *= k
    return num

print(int(fact(n)//(fact(n-m) * fact(m))))

