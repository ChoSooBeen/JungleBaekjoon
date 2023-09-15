import sys
from collections import deque

v = int(sys.stdin.readline())
tree = [[] for _ in range(v+1)]
for _ in range(v) :
    input = list(map(int, sys.stdin.readline().split()))
    vertex = input[0]
    input = input[1:-1]
    for i in range(len(input)//2) :
        tree[vertex].append((input[i*2], input[i*2+1]))

def bfs(s, flag) :
    visited = [-1] * (v+1)
    queue = deque()
    
    queue.append(s)
    visited[s] = 0
    
    while queue :
        vertex = queue.popleft()
        for a, b in tree[vertex] :
            if visited[a] == -1 :
                visited[a] = visited[vertex] + b
                queue.append(a)
    if not flag :
        return visited.index(max(visited))
    else :
        return max(visited)
idx = bfs(1, False)
print(bfs(idx, True))

# def dfs(vertex) :
#     for x, y in tree[vertex] :
#         if visited[x] == -1 :
#             visited[x] = visited[vertex] + y
#             dfs(x)
    
# visited = [-1] * (v+1)
# visited[1] = 0
# dfs(1)

# max_value = visited.index(max(visited))
# visited = [-1] * (v+1)
# visited[max_value] = 0
# dfs(max_value)
# print(max(visited))