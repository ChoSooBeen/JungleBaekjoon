import sys

N, K = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

result = sum(nums[:K]) # 구해야할 값
curr = result # 현재 0부터 K-1까지 연속된 값의 합
for i in range(K, N) :
    curr = curr - nums[i-K] + nums[i] # 맨앞의 값은 빼고 뒤에 값 추가(슬라이딩 윈도우)
    if curr > result :
        result = curr
print(result) 