from collections import deque

n = int(input())
card_lst = deque([i for i in range(1, n+1)])

while len(card_lst) > 1:
    card_lst.popleft()
    move_num = card_lst.popleft()
    card_lst.append(move_num)
    
print(card_lst[0])