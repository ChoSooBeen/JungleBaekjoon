import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

# 누적합을 저장하기 위한 변수
preSum = nums[0]
# 각 누적합을 M으로 나눈 각 나머지의 개수를 저장할 배열
div = [0] * M

# 0번째 값 먼저 저장 - 초기화
div[preSum % M] += 1

for i in range(1, N) :
    preSum = preSum + nums[i]
    div[preSum % M] += 1

count = 0
# 각각 1번부터 구한 누적합에서 가능한 개수 
# 무조건 2개를 선택하여 조합한다.
for i in range(M) :
    if div[i] > 1 :
        count += (div[i] * (div[i]-1)) // 2

# 0번 부터 구한 누적합에서 가능한 개수도 더해준다.
print(count + div[0])