import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

M = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))

def binarySearch(nums, key) :
    left, right = 0, len(nums)-1
    
    while left <= right :
        middle = (left+right)//2
        if nums[middle] == key :
            return 1
        elif nums[middle] > key :
            right = middle - 1
        else :
            left = middle + 1
    return 0

for key in target :
    print(binarySearch(nums, key))