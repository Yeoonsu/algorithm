import sys

input = sys.stdin.readline().rstrip()

n = int(input())

a = list(map(int, input().split()))

m = int(input())

b = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in b:
    result = binary_search(a, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# 계수 정렬

n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')