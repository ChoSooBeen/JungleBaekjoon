import sys
from collections import deque

# 지역변수로 활용하기 위한 main() 함수 사용
def main():
    N = int(sys.stdin.readline())

    array = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
    '''
    상하좌우 표현
    x[0], y[0] = -1, 0 = 왼쪽
    x[1], y[1] = 1, 0 = 오른쪽
    x[2], y[2] = 0, -1 = 아래쪽
    x[3], y[3] = 0, 1 = 위쪽
    '''
    x = [-1, 1, 0, 0]
    y = [0, 0, -1, 1]

    result = 0

    # 입력받은 높이 중 가장 높은 것만큼만 반복
    for height in range(max(map(max, array))):
        # 방문 여부 저장 배열
        visited = [[0] * N for i in range(N)]
        count = 0

        for j in range(N):
            for k in range(N):
                if array[j][k] > height and visited[j][k] == 0:
                    queue = deque()
                    queue.append((j, k))
                    visited[j][k] = 1

                    # BFS 구현
                    '''
                    deque 사용 이유 : 시간복잡도 차이
                    list.pop(0) = O(n)
                    deque.popleft() = O(1)
                    위의 두 경우 모두 맨 앞의 원소를 꺼낸다.
                    '''
                    while queue:
                        a, b = queue.popleft()
                        for i in range(4):
                            nx = a + x[i]
                            ny = b + y[i]
                            # 상하좌우 확인 + 범위 내인지 확인
                            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                                if array[nx][ny] > height and visited[nx][ny] == 0:
                                    visited[nx][ny] = 1
                                    queue.append((nx, ny))
                    # while문이 종료되었다는 의미는 영역 1개의 탐색을 완료했다는 의미
                    count += 1
        result = max(result, count)
    print(result)

main()