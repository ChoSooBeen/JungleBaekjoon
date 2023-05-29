import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
queue = deque(list(range(1, N+1)))
nums = list(map(int, sys.stdin.readline().split()))

count = 0
for n in nums :
    while queue[0] != n :
        count += 1
        if queue.index(n) < len(queue)//2+1 :
            queue.append(queue.popleft())
        else :
            queue.appendleft(queue.pop())
    queue.popleft()
            
print(count)