import sys
from collections import deque

N = int(sys.stdin.readline())

def final_card(N) :
    queue = deque(i for i in range(1, N+1))
    flag = True    
    while len(queue) > 1 :
        if flag :
           queue.popleft()
           flag = False
        else :
            queue.append(queue.popleft())
            flag = True
    print(queue.popleft())

final_card(N)