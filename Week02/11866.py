import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

def josephus(n, k) :
    queue = deque(i for i in range(1, n+1))
    result = []
    count = 1
    
    while queue :
        if count == k :
            result.append(queue.popleft())
            count = 1
        else :
            queue.append(queue.popleft())
            count += 1
    print('<', end='')
    for i in range(n-1) :
        print(f'{result[i]}, ', end='')
    print(f'{result[-1]}>')
    
josephus(N, K)