import sys
from collections import deque

s = int(sys.stdin.readline())

queue = deque()
visited = {}

queue.append((1, 0)) # 현재 이모티콘 개수, 클립보드 개수
visited[(1, 0)] = 0

while queue :
    current, clipboard = queue.popleft()
    if current == s :
        print(visited[(current, clipboard)])
        break
    if (current, current) not in visited.keys() :
        visited[(current, current)] = visited[((current, clipboard))] + 1
        queue.append((current, current))
    if (current + clipboard, clipboard) not in visited.keys() :
        visited[(current + clipboard, clipboard)] = visited[(current, clipboard)] + 1
        queue.append((current + clipboard, clipboard))
    if (current - 1, clipboard) not in visited.keys() :
        visited[(current - 1, clipboard)] = visited[(current, clipboard)] + 1
        queue.append((current-1, clipboard))