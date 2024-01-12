import sys

input = sys.stdin.readline

n = int(input())

stack = []

for _ in range(n):
    command = list(input().split())
    if command[0] == 'push':
        stack.append(command[1])
    if command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else: print(stack.pop())
    if command[0] == 'size':
        print(len(stack))
    if command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else: print(0)
    if command[0] == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else: print(-1)