import sys

N = int(sys.stdin.readline())
taste = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = sys.maxsize

'''
depth : taste 현재 깊이
count : 몇 개의 재료를 선택할 것인지
x : 신 맛
y : 쓴 맛
'''
def cook(depth, count, x, y) :
    global result
    
    if count :
        result = min(result, abs(x-y))
        
    if depth == N :
        return
    
    cook(depth+1, count+1, x*taste[depth][0], y+taste[depth][1]) #현재 값을 추가하고 재귀
    cook(depth+1, count, x, y) #현재 값은 추가하지 않고 재귀
    
cook(0,0,1,0)
print(result)