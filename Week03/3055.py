import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
# 입력받은 맵
arr = [list(sys.stdin.readline().strip()) for _ in range(R)]

forest = [[-1]*C for _ in range(R)] # 고슴도치의 경로를 알아낼 그래프
water = [[-1]*C for _ in range(R)] # 시간에 따른 물의 높이를 알아낼 그래프
queue = deque() # water에 사용할 큐
fqueue = deque() # forest에 사용할 큐
end = [] # 도착 좌표 지정

'''
비어있는 곳 .
물이 차 있는 구역 *
돌 X
비버의 굴 D = 도착해야할 곳
고슴도치 위치 S = 시작할 곳
'''
for i in range(R) :
    for j in range(C) :
        if arr[i][j] == '*' :
            queue.append((i, j))
            water[i][j] = 0 # 처음부터 물이 차있는 경우
        elif arr[i][j] == 'D' :
            # 고슴도치가 도착해야할 장소
            # 물이 찰 수 없는 공간
            end = [i, j]
        elif arr[i][j] == 'S' :
            fqueue.append((i, j)) # 시작 좌표 큐에 삽입
            forest[i][j] = 0 # 이미 고슴도치가 위치한 곳
            # 물이 차오를 수 있는 지역이므로 표현을 바꿔준다.
            arr[i][j] = '.' 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 물이 차오르는 시간을 측정하는 함수
def water_bfs() :
    while queue :
        curX, curY = queue.popleft()
        for i in range(4) :
            nx, ny = curX + dx[i], curY + dy[i]
            # 물이 차오르지 못하는 지역 = 비버의 집(D), 돌(X)
            # 그 외의 지역을 . 으로 표현
            if 0 <= nx < R and 0 <= ny < C and water[nx][ny] == -1 and  arr[nx][ny] == '.':
                water[nx][ny] = water[curX][curY] + 1
                queue.append((nx, ny))

# 고슴도치의 이동 시간을 측정하는 함수
def forest_bfs() :
    while fqueue :
        curX, curY = fqueue.popleft()
        for i in range(4) :
            nx, ny = curX + dx[i], curY + dy[i]
            # 고슴도치는 다음에 물이 차지 않을 지역으로만 가능하고 움직일 수 있는 지역으로는 . 과 D만 존재한다.
            if 0 <= nx < R and 0 <= ny < C and forest[nx][ny] == -1 and (arr[nx][ny] == '.' or arr[nx][ny] == 'D') :
                # 현재 이동한 시간에 1을 더한 것보다 다음 이동할 지역이 물에 차는 시간이 크면 
                # 다음날에 잠길일이 없으므로 이동 가능
                # 물에 아예 잠기지 않는 지역이 있을 수 있으므로 or 조건 추가
                if forest[curX][curY] + 1 < water[nx][ny] or water[nx][ny] == -1 :
                    forest[nx][ny] = forest[curX][curY] + 1
                    fqueue.append((nx, ny))

water_bfs()
forest_bfs()

if forest[end[0]][end[1]] == -1 :
    print("KAKTUS")
else :
    print(forest[end[0]][end[1]])