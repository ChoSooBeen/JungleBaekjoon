import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

def NGE(nums, N) : 
    stack = [nums[N-1]]
    result = [-1] * N

    for k in range(1, N) :
        idx = N-1-k
        n = nums[idx]
        # 현재 나보다 작은 모든 값 제거
        while stack:
            if stack[-1] > n :
                break
            stack.pop()
        # 오큰수 입력
        if stack :
            result[idx] = stack[-1]
        else :
            result[idx] = -1
        stack.append(n) 
    print(*result)

NGE(nums, N)