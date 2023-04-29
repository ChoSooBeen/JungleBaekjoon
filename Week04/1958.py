import sys

X = list(sys.stdin.readline().strip())
Y = list(sys.stdin.readline().strip())
Z = list(sys.stdin.readline().strip())

def LCS_Length(x, y, z) :
    m, n, k = len(x), len(y), len(z)
    dp = [[[0] * (n+1) for _ in range(m+1)] for _ in range(k+1)]
    for l in range(1, k+1) :
        for i in range(1, m+1) :
            for j in range(1, n+1) :
                if x[i-1] == y[j-1] == z[l-1] :
                    dp[l][i][j] = dp[l-1][i-1][j-1] + 1
                else :
                    dp[l][i][j] = max(dp[l-1][i][j], dp[l][i-1][j], dp[l][i][j-1])
    print(dp[k][m][n])
                    
LCS_Length(X, Y, Z)