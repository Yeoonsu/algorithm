from collections import deque

# 정점, 간선수, 시작점
n, m, v = map(int, input().split())

graph = [[False] * (n+1) for _ in range(n+1)]

# 간선 수만큼 그래프를 이어준다.
for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

# 방문 여부를 담을 리스트
visited1 = [False] * (n+1)
visited2 = [False] * (n+1)

def dfs(v):
    visited1[v] = True
    print(v, end=" ")
    for i in range(1, n+1):
        if not visited1[i] and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    q = deque([v])
    visited2[v] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, n+1):
            if not visited2[i] and graph[v][i] == 1:
                q.append(i)
                visited2[i] = True

dfs(v)
print()
bfs(v)