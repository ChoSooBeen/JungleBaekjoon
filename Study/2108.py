import sys
import math

N = int(sys.stdin.readline().strip())
nums = {}       # 입력받은 수들의 등장 횟수
lst = [0] * N   # 입력받은 수들

sum = 0
for i in range(N) :
    num = int(sys.stdin.readline().strip())
    if num in nums :
        nums[num] += 1
    else :
        nums[num] = 1
    lst[i] = num
    sum += num

lst.sort()
nums = dict(sorted(nums.items()))
nums = sorted(nums.items(), key= lambda x : -x[1])

print(round(sum/N)) # 산술 평균 값
print(lst[N//2]) # 중앙값
if len(nums) > 2 and nums[0][1] == nums[1][1]: # 최빈값
    print(nums[1][0])
else :
    print(nums[0][0])
print(lst[len(lst)-1] - lst[0]) # 범위