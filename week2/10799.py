"""
1. (이 나오면 스택에 넣는다.
2. ()이 나오면 현재 스택에 있는 ( 수만큼 정답에 더해준다. 
3. )이 나오면 스택의 (를 pop하고 정답에 1을 더해준다.
"""

bar_razor = list(input())
answer = 0
stack = []

for i in range(len(bar_razor)):
    if bar_razor[i] == '(':
        stack.append('(')
    
    else:
        if bar_razor[i-1] == '(':
            stack.pop()
            answer += len(stack)

        else:
            stack.pop()
            answer += 1

print(answer)