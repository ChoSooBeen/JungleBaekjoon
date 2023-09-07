import sys

n, l = map(int, sys.stdin.readline().split())
water = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
water.sort()

count = 0
current = -1
for x, y in water :
    if current < x : 
        current = x
    length = y - current
    if length % l == 0 :
        count += length // l
        current += (length // l) * l
    else :
        count += (length // l + 1)
        current += (length // l + 1) * l
print(count)