import sys
from collections import deque

##############input 값 정리###################################
N = int(sys.stdin.readline()) #보드의 크기
array = [[0] * (N+1) for _ in range(N+1)] # 문제에서 나온 보드는 (1,1) 부터 시작

L = int(sys.stdin.readline()) #사과의 개수
for _ in range(L) :
    tmp_x, tmp_y = map(int, sys.stdin.readline().split())
    array[tmp_x][tmp_y] = 1 # 사과 저장

K = int(sys.stdin.readline()) #방향 전환 횟수
v = {} # {시간 : 방향}
for _ in range(K) :
    t, c = sys.stdin.readline().split()
    v[int(t)] = c
##############################################################
# 뱀이 살아있는 시간 구하는 함수
def dummy() :
    ###############초기값 설정##################################
    # 우 -> 하 -> 좌 -> 상
    x = [1, 0, -1, 0]
    y = [0, 1, 0, -1]
    # 게임 시간
    time = 0
    # 초기 방향
    d = 0
    # 뱀의 초기 위치
    current_x, current_y = 1, 1
    # 뱀이 있는 곳
    snake = deque([(current_x, current_y)])
    ###########################################################
    while True :
        current_x, current_y = current_x + x[d], current_y + y[d]
        # 움직인 좌표값이 범위 내에 존재하고(즉, 벽에 부딪히지 않고) 자기 몸과 부딪히지 않으면
        if 0 < current_x <= N and 0 < current_y <= N and (current_x, current_y) not in snake:
            # x : 행 -> 좌우 움직여야 한다.
            # y : 열 -> 위아래 움직여야 한다.
            # 이차원 배열에 입력을 할 때 주의해야 함
            if array[current_y][current_x] != 1 : # 현재 위치에 사과가 존재하지 않으면
                snake.popleft()
            else :
                array[current_y][current_x] = 0
            snake.append((current_x, current_y))
            time += 1
            
            # 현재 시간이 방향을 바꿔야할 시간이라면
            if time in v.keys() :
                if v[time] == 'D' : # 오른쪽으로 돌아야 할 경우 +1
                    d = (d+1) % 4
                else : # 왼쪽으로 돌아야 할 경우 -1
                    d = (d-1) % 4
            
        else :
            # 미리 종료 여부를 검사하고 나오기 때문에 마지막 1초를 더해준다.
            return time + 1

print(dummy())          
