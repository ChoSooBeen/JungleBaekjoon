import sys

N = int(sys.stdin.readline())

# 하향식 동적 프로그래밍
dic = {0 : 0, 1 : 1}
def top_down_fib(n) :
    if n not in dic.keys() :
        dic[n] = top_down_fib(n-1) + top_down_fib(n-2)
    return dic[n]

# 상향식 동적 프로그래밍
def bottom_up_fib(n) :
    memo = [0] * (n+1)
    memo[1] = 1
    
    for i in range(2, n+1) :
        memo[i] = memo[i-1] + memo[i-2]
    
    return memo[n]

print(top_down_fib(N))
print(bottom_up_fib(N))