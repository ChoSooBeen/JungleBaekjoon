import sys
from collections import deque
    
def bfs(x, y, size) :
    queue = deque()
    distance = [[-1] * n for _ in range(n)]
    result = []
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue.append((x, y))
    distance[x][y] = 0
    
    while queue :
        cx, cy = queue.popleft()
        for i in range(4) :
            nx, ny = cx + dx[i], cy + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n :
                # 현재 크기보다 큰 물고기는 어떤한 경우에도 먹을 수 없다.
                # 현재 크기만한 물고기는 먹은 수를 채워서 다음에 먹을 수 있다.
                # BFS는 가장 최단 거리를 구하기 떄문에 먹을 수 없는 최단거리를 구하면 안된다.
                if distance[nx][ny] == -1 and space[nx][ny] <= size :
                    queue.append((nx, ny))
                    distance[nx][ny] = distance[cx][cy] + 1
                    # 아기상어는 자신의 크기보다 작은 물고기만 먹을 수 있다.
                    if space[nx][ny] < size and space[nx][ny] != 0:
                        result.append([nx, ny, distance[nx][ny]])
    # 거리가 멀고 아래쪽이고 오른쪽일수록 앞으로 오도록 정렬
    return sorted(result, key= lambda x : (-x[2], -x[0], -x[1]))

if __name__ == '__main__' :
    input = sys.stdin.readline
    
    n = int(input())
    space = [list(map(int, input().split())) for _ in range(n)]
    baby_x, baby_y = 0, 0
    for i in range(n) :
        for j in range(n) :
            if space[i][j] == 9 :
                baby_x, baby_y = i, j
                break
    count = 0
    size = 2
    time = 0
    while True :
        result = bfs(baby_x, baby_y, size)
        
        if len(result) == 0 :
            break
        
        x, y, dis = result.pop()
        time += dis
        space[baby_x][baby_y] = 0
        space[x][y] = 0
        baby_x, baby_y = x, y
        count += 1
        
        if count == size :
            size += 1
            count = 0
    print(time)