import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort() # 정렬

start = 0 # 현재 가장 작은 값의 인덱스
end = N-1 # 현재 가장 큰 값의 인덱스
count = 0

while start < end :
    s = nums[start] + nums[end]
    if s == M : # 갑옷을 만들 수 있다.
        count += 1
        start += 1
        end -= 1
    elif s < M : # M보다 작으므로 작은 값을 올려준다.
        start += 1
    else : # M보다 크므로 큰 값을 줄여준다.
        end -= 1

print(count)