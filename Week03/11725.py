import sys

N = int(sys.stdin.readline())

matrix = [[] for _ in range(N)]

# 연결 상태만 저장하는 방식
for _ in range(N-1) :
    x, y = map(int, sys.stdin.readline().split())
    matrix[x-1].append(y-1)
    matrix[y-1].append(x-1)

def dfs(v) :
    # 방문 여부 확인 겸 부모 노드의 번호 저장
    visited = [0] * N
    stack = []
    
    stack.append(v)
    visited[v] = 1
    
    while stack :
        flag = False
        cur = stack[-1] # 현재 노드
        # 현재 노드와 연결되어 있는 요소들의 리스트 반복
        for i in matrix[cur] : 
            if visited[i] == 0 :
                stack.append(i)
                visited[i] = cur+1 # 부모노드 저장
                flag = True # 아직 탐색할 노드 존재
                break
        if not flag : # 더이상 탐색할 노드가 없으면
            stack.pop()
    for i in visited[1:] :
        print(i)

dfs(0)