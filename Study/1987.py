import sys

r, c = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [False] * 26
result = 0
a = ord('A')

def dfs(x, y, count) :
    global result, a
    for i in range(4) :
        nx, ny = x + dx[i], y + dy[i]
        if nx >= 0 and nx < r and ny >= 0 and ny < c :
            if not visited[ord(board[nx][ny]) - a] :
                visited[ord(board[nx][ny]) - a] = True
                dfs(nx, ny, count + 1)
                visited[ord(board[nx][ny]) - a] = False
    result = max(result, count)

visited[ord(board[0][0]) - a] = True
dfs(0,0,1)
print(result)