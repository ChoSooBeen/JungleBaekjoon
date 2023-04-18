import sys
import heapq

# https://velog.io/@piopiop/백준-13334-철로파이썬 참고

########input 값##########################################################
N = int(sys.stdin.readline())
tmp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 철로 길이
d = int(sys.stdin.readline())
roads = []
# 입력받은 집,회사 사이의 거리가 철로 길이보다 긴 경우 제외 -> 애초에 포함될 수 없기에 상관없음
for i in tmp :
    i.sort()
    if i[1] - i[0] <= d :
        roads.append(i)
roads.sort(key= lambda x : x[1])
############################################################################

count = 0
heap = [] # 현재 위치에서 철로 길이 안에 포함된 좌표 저장
for r in roads :
    if not heap :
        heapq.heappush(heap, r)
    else :
        # 현재 보고 있는 r의 오른쪽 좌표에서 d만큼 뺀 값 = 철로 시작점
        # 현재 힙 안의 최솟값의 시작점이 위의 값보다 작으면 철로에 포함되지 않는다.
        while heap[0][0] < r[1] - d :
            heapq.heappop(heap)
            if not heap :
                break
        heapq.heappush(heap, r)
    # 최댓값 저장
    count = max(count, len(heap))

print(count)