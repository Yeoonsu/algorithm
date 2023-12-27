import sys
from collections import deque

N = int(input())
        
queue = deque([i for i in range(1, N+1)])

while (len(queue)>1):
    queue.popleft()
    move_num = queue.popleft()
    queue.append(move_num)

print(queue[0])
