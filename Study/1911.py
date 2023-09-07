import sys

n, l = map(int, sys.stdin.readline().split())
water = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
water.sort()

count = 0
current = -1 # 널빤지가 덮여지지 않는 시작점
for x, y in water :
    if current < x : 
        current = x
        
    length = y - current # 덮어야할 물 웅덩이의 길이
    need = 0 # 현재 필요한 널빤지의 개수
    
    if length % l == 0 :
        need = length // l
    else :
        need = length // l + 1
        
    count += need
    current += need * l
print(count)