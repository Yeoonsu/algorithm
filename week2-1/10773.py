k = int(input())

stack = []

for _ in range(k):
    command = int(input())
    if command:
        stack.append(command)
    elif command == 0:
        stack.pop()

print(sum(stack))