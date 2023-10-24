import sys
import heapq

input = sys.stdin.readline
n = int(input())
lecture = [list(map(int, input().split())) for _ in range(n)]
lecture.sort()

room = []
heapq.heappush(room, lecture[0][1])
for i in range(1, n) :
    if room[0] <= lecture[i][0] :
        heapq.heappop(room)
    heapq.heappush(room, lecture[i][1])
print(len(room))