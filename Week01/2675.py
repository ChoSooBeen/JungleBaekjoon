T = int(input())

result = ""
while T > 0:
    tmp = input().split()
    R = int(tmp[0])
    S = tmp[1]
    ans = ""
    for i in range(len(S)):
        ans += S[i] * R
    result += ans + "\n"
    T -= 1
print(result)