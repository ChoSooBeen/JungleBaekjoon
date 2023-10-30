import sys

input = sys.stdin.readline

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

if cranes[0] < boxes[0] : # 옮길 수 없는 경우
    print(-1)
else :
    count = 0
    while boxes :
        for crane in cranes :
            for box in boxes :
                if box <= crane :
                    boxes.remove(box)
                    break
        count += 1
    print(count)