import sys

N = int(sys.stdin.readline())

height = [int(sys.stdin.readline()) for i in range(N)]

current = height.pop()
count = 1

for i in range(N-2, -1, -1) :
    if current < height[i] :
        count += 1
        current = height[i]

print(count)