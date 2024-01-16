n = int(input())
member_lst = []

for _ in range(n):
    age, name = list(input().split())
    age = int(age)
    member_lst.append((age, name))

member_lst.sort(ley = lambda x: x[0])

for i in member_lst:
    print(i[0], i[1])