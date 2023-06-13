import sys

N = int(sys.stdin.readline())
result = []

def isPrime(n) :
    for i in range(2, int(n**(1/2))+1) :
        if n % i == 0 :
            return False
    return True

def dfs(depth, n) :
    if depth == N :
        if isPrime(n) :
            result.append(n)
        return
    for i in range(10) :
        nn = n*10 + i
        if isPrime(nn) :
            dfs(depth+1, n*10+i)

prime = [2, 3, 5, 7]
for p in prime :
    dfs(1, p)

for r in result :
    print(r)