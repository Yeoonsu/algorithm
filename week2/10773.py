
stack = []

n = int(input())

for _ in range(n):
    command = int(input())
    if command == 0:
        stack.pop()
    else:
        stack.append(command)

if stack:
    print(sum(stack))
elif not stack:
    print(0)