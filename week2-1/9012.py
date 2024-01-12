import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    stack = []
    command = input()
    for word in command:
        if word == '(':
            stack.append(word)
        elif word == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
                
    else:
        if not stack:
            print('YES')
        else:
            print('NO')