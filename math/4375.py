n = int(input())

def one(n):
    for i in range(10001):
        for j in range(10001):
            if str(n * i) == str(1) * j:
                break
    return j

print(one(n))