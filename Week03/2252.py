import sys

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N)]

for _ in range(M) :
    x, y = map(int, sys.stdin.readline().split())
    graph[x-1].append(y-1)

def topologicalSort(v) :
    visited[v] = 1
    
    for i in graph[v] :
        if visited[i] == 0:
            topologicalSort(i)
    stack.append(v) # 현재 노드를 가장 마지막에 스택에 push하도록!

visited = [0] * N
stack = [] # 가장 마지막 말단노드부터 쌓이도록 해야한다.
for i in range(N) :
    if visited[i] == 0 :
        topologicalSort(i)

while stack : # 스택에서 꺼내는 순서가 위상 순서
    print(stack.pop()+1, end=' ')
    
########################### BFS를 이용한 풀이 ##############################
# import sys
# from collections import deque

# N, M = map(int, sys.stdin.readline().split())

# graph = [[] for _ in range(N)]
# inDegree = [0] * N

# for _ in range(M) :
#     x, y = map(int, sys.stdin.readline().split())
#     graph[x-1].append(y-1)
#     inDegree[y-1] += 1

# def topologicalSort(d) :
#     queue = deque()
#     visited = [0] * N
#     result = [] # 정렬 결과 저장
    
#     # 진입 차수가 0인 정점 처리
#     for i in range(N) :
#         if d[i] == 0 :
#             visited[i] = 1
#             queue.append(i) 
            
#     while queue :
#         current = queue.popleft()
#         result.append(current+1) # 정렬 결과 저장
#         # 현재 정점에 연결된 정점의 차수 -1감소
#         for i in graph[current] :
#             if visited[i] == 0 and d[i]:
#                 d[i] -= 1
#             if d[i] == 0 : # 정점의 진입차수가 0이되면 큐에 삽입하여 정렬 준비
#                 visited[i] = 1
#                 queue.append(i)
#     print(*result)

# topologicalSort(inDegree)