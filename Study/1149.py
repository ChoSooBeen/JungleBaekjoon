import sys

n = int(sys.stdin.readline())
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1, n) :
    cost[i][0] += min(cost[i-1][1], cost[i-1][2]) #R
    cost[i][1] += min(cost[i-1][0], cost[i-1][2]) #G
    cost[i][2] += min(cost[i-1][0], cost[i-1][1]) #B
print(min(cost[n-1]))