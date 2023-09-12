import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = 0

max_value = max(map(max, paper)) # 입력받은 값 중 가장 큰 값 저장
visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, count, value) :
    global result 
    
    if result >= value + max_value * (4-count) : # 최댓값에 도달하지 못할 경우
        return
    if count == 4 :
        result = max(result, value)
        return
    for i in range(4) :
        nx, ny = x + dx[i], y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m :
            if not visited[nx][ny] :
                if count == 2 : # ㅏ, ㅓ, ㅗ, ㅜ 를 위한 작업
                    visited[nx][ny] = True
                    dfs(x, y, count + 1, value + paper[nx][ny])
                    visited[nx][ny] = False
                visited[nx][ny] = True
                dfs(nx, ny, count + 1, value + paper[nx][ny])
                visited[nx][ny] = False
    
for i in range(n) :
    for j in range(m) :
        visited[i][j] = True
        dfs(i, j, 1, paper[i][j])
        visited[i][j] = False
print(result)