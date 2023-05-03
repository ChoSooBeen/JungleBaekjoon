import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

count = 0
for i in range(N) :
    start = 0
    end = N-1
    while start < end :
        # start와 end는 현재 값이면 안된다.
        if start == i :
            start += 1
        elif end == i :
            end -= 1
        else :
            current = nums[i] # 현재값
            t = nums[start] + nums[end] # 두개 더한값
            if current == t :
                count += 1
                break
            elif current > t :
                start += 1
            else :
                end -= 1
print(count)