import sys
from collections import deque

front = list(sys.stdin.readline().strip())
back = deque()

m = int(sys.stdin.readline())
for _ in range(m) :
    op = sys.stdin.readline().split()
    if op[0] == 'L' and len(front) :
        back.appendleft(front.pop())
    elif op[0] == 'D' and len(back) :
        front.append(back.popleft())
    elif op[0] == 'B' and len(front) :
        front.pop()
    elif op[0] == 'P' :
        front.append(op[1])

for i in front :
    print(i, end="")
for i in back :
    print(i, end="")