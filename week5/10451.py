t = int(input())

def dfs(v):
    visited[v] = True # 현재 노드 방문 처리
    nv = graph[v] # 인접 노드
    # 아직 방문하지 않은 노드라면 dfs 호출
    if not visited[nv]:
        dfs(nv)

for _ in range(t):
    n = int(input()) # 순열 크기
    graph = list(map(int, input().split())) # 순열(n개)
    graph.insert(0, 0)
    visited = [False] * (n+1) # 1~n 사용
    cycle = 0 # 순열 사이클 개수

    for i in range(1, n+1):
        # 방문하지 않은 노드라면
        if not visited[i]:
            dfs(i)
            cycle += 1
    print(cycle)