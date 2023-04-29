import sys

X = list(sys.stdin.readline().strip())
Y = list(sys.stdin.readline().strip())

def LCS_Length(x, y) :
    m, n = len(x), len(y)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1, m+1) :
        for j in range(1, n+1) :
            if x[i-1] == y[j-1] : # 두 문자가 같을 경우
                dp[i][j] = dp[i-1][j-1] + 1
            # 같지 않을 경우 두 값 중 큰 값 선택
            elif dp[i-1][j]  >= dp[i][j-1] : 
                dp[i][j] = dp[i-1][j]
            else :
                dp[i][j] = dp[i][j-1]
    print(dp[m][n])
    
    # 9252번 - LCS2 
    # https://www.acmicpc.net/problem/9252
    # dp 배열을 반대로 타고 올라가기!!
    if dp[m][n] > 0 :
        i, j = m, n
        result = ''
        while i != 0 and j != 0 :
            if x[i-1] == y[j-1] :
                result = x[i-1] + result
                i -= 1
                j -= 1
            elif dp[i-1][j]  >= dp[i][j-1] :
                i -= 1
            else :
                j -= 1
        print(result)
                    
LCS_Length(X, Y)