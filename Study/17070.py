import sys

n = int(sys.stdin.readline())
house = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
count = 0
def dfs(x, y, dir) :
    global count
    
    if x == n-1 and y == n-1 :
        count += 1
        return
    if x+1 < n and y+1 < n : #대각선 이동
        if house[x+1][y+1] == 0 and house[x+1][y] == 0 and house[x][y+1] == 0 :
            dfs(x+1, y+1, 2)
    if dir == 0 or dir == 2 : #가로 이동
        if y+1 < n and house[x][y+1] == 0 :
            dfs(x, y+1, 0)
    if dir == 1 or dir == 2 : #세로 이동
        if x+1 < n and house[x+1][y] == 0 :
            dfs(x+1, y, 1)
dfs(0, 1, 0)
print(count)

def bfs() :
    from collections import deque
    
    n = int(sys.stdin.readline())
    house = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    queue = deque()

    # 가로, 세로, 대각선 방향
    dx = [0, 1, 1]
    dy = [1, 0, 1]
    queue.append([[0, 0], [0, 1]])
    while queue :
        current = queue.popleft()
        idx = []
        if current[0][0] - current[1][0] == 0 : #가로일 경우
            idx = [0,2]
        elif current[0][1] - current[1][1] == 0 : #세로일 경우
            idx = [1,2]
        else : #대각선일 경우
            idx = [0,1,2]
        for i in idx :
            nx, ny = current[1][0] + dx[i], current[1][1] + dy[i]
            if nx < n and ny < n and house[nx][ny] == 0 :
                if i != 2 or (i == 2 and house[nx-1][ny] == 0 and house[nx][ny-1] == 0) :
                    visited[nx][ny] += 1
                    queue.append([current[1], [nx, ny]])
    print(visited[n-1][n-1])