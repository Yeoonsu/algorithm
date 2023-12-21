from math import gcd

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

num1 = 1
num2 = 1

for i in arr1:
    num1 *= i
for i in arr2:
    num2 *= i

print(str(gcd(num1, num2))[-9:])