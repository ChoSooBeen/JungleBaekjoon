import sys

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

def dfs(count, result) :
    if count == m :
        print(*result)
        return
    
    for num in nums :
        if num not in result :
            result.append(num)
            dfs(count + 1, result)
            result.pop()
dfs(0, [])