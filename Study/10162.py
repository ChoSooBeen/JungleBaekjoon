import sys

t = int(sys.stdin.readline())
time = [300, 60, 10]

count = [0, 0, 0]
while t >= 10 :
    for i in range(3) :
        if t >= time[i] :
            t -= time[i]
            count[i] += 1
            break
if t == 0 :
    print(*count)
else :
    print(-1)