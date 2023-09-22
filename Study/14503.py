import sys
from collections import deque

n, m  = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
place = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 1
place[r][c] = 2

while True :
    flag = False
    for _ in range(4) :
        d = (d + 3) % 4
        x, y = r + dx[d], c + dy[d]
        if place[x][y] == 0 :
            place[x][y] = 2
            count += 1
            r, c = x, y
            flag = True
            break
    if not flag :
        x, y = r - dx[d], c - dy[d]
        if place[x][y] == 1 :
            print(count)
            break
        else :
            r, c = x, y