import sys
from collections import deque
input = sys.stdin.readline

r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]

air = []
for i in range(r) :
    if room[i][0] == -1 :
        air.append(i)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs() :
    while queue :
        x, y, amount = queue.popleft()
        count = 0
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and nx < r and ny >= 0 and ny < c :
                if room[nx][ny] != -1 :
                    count += 1
                    room[nx][ny] += (amount // 5)
        room[x][y] -= (amount // 5) * count

def cycle_up() :
    d = 1
    before = 0
    x, y = air[0], 1
    while True :
        nx, ny = x + dx[d], y + dy[d]
        if nx == r or nx == -1 or ny == c or ny == -1 :
            d = (d-1) % 4
            continue
        if x == air[0] and y == 0 :
            break
        room[x][y], before = before, room[x][y]
        x, y = nx, ny

def cycle_down() :
    d = 1
    before = 0
    x, y = air[1], 1
    while True :
        nx, ny = x + dx[d], y + dy[d]
        if nx == r or nx == -1 or ny == c or ny == -1 :
            d = (d+1) % 4
            continue
        if x == air[1] and y == 0 :
            break
        room[x][y], before = before, room[x][y]
        x, y = nx, ny
          
for _ in range(t) :
    queue = deque()
    for i in range(r) :
        for j in range(c) :
            if room[i][j] > 0 :
                queue.append((i, j, room[i][j]))
    bfs()
    cycle_up()
    cycle_down()

result = 2
for i in range(r) :
    result += sum(room[i])
print(result)    