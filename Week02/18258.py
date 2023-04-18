from collections import deque
import sys

N = int(sys.stdin.readline())
queue = deque()

def isEmpty() :
    if len(queue) == 0 :
        return 1
    return 0

for _ in range(N) :
    command = list(sys.stdin.readline().split())
    if command[0] == "push" :
        queue.append(command[1])
    elif command[0] == "pop" :
        if isEmpty() == 1 :
            print(-1)
        else :
            print(queue.popleft())
    elif command[0] == "size" :
        print(len(queue))
    elif command[0] == "empty" :
        print(isEmpty())
    elif command[0] == "front" :
        if isEmpty() == 1 :
            print(-1)
        else :
            print(queue[0])
    else :
        if isEmpty() == 1 :
            print(-1)
        else :
            print(queue[-1])