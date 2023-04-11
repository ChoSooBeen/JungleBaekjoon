import sys
from collections import deque

N = int(sys.stdin.readline())

array = []
'''
상하좌우 표현
x[0], y[0] = -1, 0 = 왼쪽
x[1], y[1] = 1, 0 = 오른쪽
x[2], y[2] = 0, -1 = 아래쪽
x[3], y[3] = 0, 1 = 위쪽
'''
x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]

for i in range(N) :
    array.append(list(map(int, sys.stdin.readline().split())))

result = 0

# 높이 제한 : 1이상 100이하의 정수
for height in range(101) :
    # 방문 여부 저장 배열
    visited = [[0] * N for i in range(N)]
    count = 0
    
    for j in range(N) :
        for k in range(N) :
            if array[j][k] > height and visited[j][k] == 0 :
                queue = deque()
                queue.append((j, k))
                visited[j][k] = 1
                
                # BFS 구현
                # queue 큐 = 선입선출 구조
                while queue:
                    a, b = queue.popleft()
                    for i in range(4) :
                        nx = a + x[i]
                        ny = b + y[i]
                        # 상하좌우 확인 + 범위 내인지 확인
                        if nx >= 0 and nx < N and ny >= 0 and ny < N :
                            if array[nx][ny] > height and visited[nx][ny] == 0 :
                                visited[nx][ny] = 1
                                queue.append((nx, ny))
                count += 1
    # 이미 다 잠겼을 경우 반복문 중지
    if count == 0:
        break
    result = max(result, count)
        
print(result)