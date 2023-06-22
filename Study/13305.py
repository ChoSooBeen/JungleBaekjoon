import sys

N = int(sys.stdin.readline())
length = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

total_cost = 0
min_price = cost[0]
for i in range(1, N):
    total_cost += min_price * length[i-1]
    min_price = min(min_price, cost[i])
print(total_cost)