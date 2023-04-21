import sys
from collections import deque

computer = int(sys.stdin.readline())
net = int(sys.stdin.readline())

network = [[0] * (computer+1) for _ in range(computer+1)]

for _ in range(net) :
    x, y = map(int, sys.stdin.readline().split())
    network[x][y] = 1
    network[y][x] = 1

def virus(v) :
    visited = [0] * (computer+1)
    queue = deque()
    count = 0
    
    visited[v] = 1
    queue.append(v)
    
    while queue :
        cur = queue.popleft()
        for i in range(computer+1) :
            if network[cur][i] == 1 and visited[i] == 0 :
                queue.append(i)
                visited[i] = 1
                count += 1
    return  count

print(virus(1))
    