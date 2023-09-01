import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

# dp[0][k] : 특정 숫자를 제거하지 않았을 경우
# dp[1][k] : 특정 숫자를 제거했을 경우
dp = [[x for x in nums] for _ in range(2)]

for i in range(1, n) :
    dp[0][i] = max(dp[0][i-1]+nums[i], dp[0][i]) # 연속된 수를 더한 경우
    dp[1][i] = max(dp[1][i-1]+nums[i], dp[0][i-1]) # i번째 숫자를 뺀 경우

print(max(max(dp[0]), max(dp[1])))