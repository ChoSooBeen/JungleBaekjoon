import sys

N = int(sys.stdin.readline())
nums = [i for i in range(1, N+1)]

def permutation(count, result) :
    if count == N :
        print(*result)
    else :
        for i in range(N) :
            if nums[i] not in result :
                result.append(nums[i])
                permutation(count+1, result)
                result.pop()

permutation(0, [])