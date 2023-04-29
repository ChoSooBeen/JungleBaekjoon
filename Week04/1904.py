import sys

N = int(sys.stdin.readline())

def binary(n) :
    if n < 3 :
        return n
    
    a = 1
    b = 2
    cnt = 2
    while cnt != n :
        cur = (a + b) % 15746
        a, b = b ,cur
        cnt += 1
    return cur
    
    # dp = [0] * (n+1)
    # dp[1] = 1
    # if n == 1 :
    #     return dp[1]
    
    # dp[2] = 2
    # for i in range(3, n+1) :
    #     dp[i] = (dp[i-1] + dp[i-2]) % 15746
    # return dp[n]

print(binary(N))