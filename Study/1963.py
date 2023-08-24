import sys
from collections import deque

T = int(sys.stdin.readline())

def isPrime(n) :
    for i in range(2, int(n**(1/2))+1) :
        if n % i == 0 :
            return False
    return True

def bfs(a, b) :
    queue = deque()
    visited[a] = True
    queue.append((a, 0))
    
    while queue :
        password, count = queue.popleft()
        if password == b :
            print(count)
            return
        for i in range(4) :
            for j in range(10) :
                new_pass = list(str(password))
                new_pass[i] = str(j)
                new_pass = int(''.join(new_pass))
                if new_pass >= 1000 and not visited[new_pass] and isPrime(new_pass) :
                    queue.append((new_pass, count+1))
                    visited[new_pass] = True

for _ in range(T) :
    a, b = map(int, sys.stdin.readline().split())
    visited = [False] *10000
    bfs(a, b)