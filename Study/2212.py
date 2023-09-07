import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
sensor = list(map(int, sys.stdin.readline().split()))

sensor.sort()

distance = [0] * (n-1)
for i in range(1, n) :
    distance[i-1] = sensor[i] - sensor[i-1]

distance.sort(reverse=True)
print(sum(distance[k-1:]))