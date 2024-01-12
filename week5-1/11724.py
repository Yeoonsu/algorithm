from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (1+n)
count = 0

def dfs(start, depth):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth+1)

for i in range(1, n+1):
    if not visited[i]:
        if not graph[i]:
            count += 1
            visited[i] = True
        else:
            dfs(i, 0)
            count += 1

print(count)