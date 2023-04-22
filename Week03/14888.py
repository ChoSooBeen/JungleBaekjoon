import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
plus, minus, mul, div = map(int, sys.stdin.readline().split())

max_result = -sys.maxsize
min_result = sys.maxsize

def dfs(count, total, plus, minus, mul, div) :
    global max_result, min_result
    
    if count == N :
        max_result = max(max_result, total)
        min_result = min(min_result, total)
        return
    if plus > 0 :
        dfs(count+1, total + nums[count], plus-1, minus, mul, div)
    if minus > 0 :
        dfs(count+1, total - nums[count], plus, minus-1, mul, div)
    if mul > 0 :
        dfs(count+1, total * nums[count], plus, minus, mul-1, div)
    if div > 0 :
        if total < 0 :
            tmp = (-total) // nums[count]
            tmp = -tmp
        else :
            tmp = total // nums[count]
        dfs(count+1, tmp, plus, minus, mul, div-1)

dfs(1, nums[0], plus, minus, mul, div)        

print(max_result)
print(min_result)