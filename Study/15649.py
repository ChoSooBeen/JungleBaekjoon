import sys

n, m = map(int, sys.stdin.readline().split())

def dfs(count, result) :
    if count == m :
        print(*result)
        return
    
    for i in range(n) :
        if i+1 not in result:
            result.append(i+1)
            dfs(count + 1, result)
            result.pop()

dfs(0, [])