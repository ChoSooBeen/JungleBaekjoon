import sys

K = int(sys.stdin.readline())

# dfs 반복문으로 구현
def dfs(g, n) : # n 시작 정점
    stack = []
    visited[n] = 1
    stack.extend(g[n]) # n과 연결되 모든 정점 추가
    
    while stack :
        par, cur = stack.pop()
        if visited[cur] == 0 :
            visited[cur] = 3 - visited[par] # 1 아니면 2 로 저장
            stack.extend(g[cur]) # cur과 연결되 모든 정점 추가
        elif visited[cur] == visited[par] :
            return False
    return True

for _ in range(K) :
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V)]
    # 빨강색 = 1, 파란색 = 2
    visited = [0] * V
    flag = True
    for _ in range(E) :
        x, y = map(int, sys.stdin.readline().split())
        graph[x-1].append((x-1, y-1))
        graph[y-1].append((y-1, x-1))
    
    # 비연결 그래프일 경우도 존재하므로
    # 모든 정점을 탐색할 수 있도록!
    for i in range(V) :
        if visited[i] == 0 :
            if dfs(graph, i) == False:
                flag = False
                break
    if flag :
        print("YES")
    else :
        print("NO")