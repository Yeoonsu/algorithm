
# 입력받은걸 0, 1, 2, 3, 4.. 로 지정해주고
# 다시 입력 순서대로 출력

n = int(input())

arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))
dic = {arr2[i]: i for i in range(len(arr2))}
for i in arr:
    print(dic[i], end= ' ')