import sys
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]
for _ in range(n-1) :
    x, y, w = map(int, sys.stdin.readline().split())
    tree[x].append((y, w))
    tree[y].append((x, w))

visited = [-1] * (n+1)

def dfs(v, weight) :  
    for vertex, w in tree[v] :
        if visited[vertex] == -1 :
            visited[vertex] = weight + w
            dfs(vertex, weight + w)

visited[1] = 0
dfs(1, 0)

idx, distance = 0, 0
for i in range(1, n+1) :
    if visited[i] > distance :
        idx = i
        distance = visited[i]

visited = [-1] * (n+1)
visited[idx] = 0
dfs(idx, 0)

print(max(visited))