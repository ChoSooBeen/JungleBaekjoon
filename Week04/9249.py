import sys

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

s = A + "1" + B
n = len(s)

# 접미사 배열 suffix[i] = i -> i번째부터 끝까지 포함하는 부분문자열
# Get Suffix Array
suffix = [i for i in range(n)]
g = [0] * (n+1) # 순위
ng = [0] * (n+1) # 새로운 순위를 갱신할 때 이용

for i in range(n):
    g[i] = ord(s[i])

g[n] = -1 
ng[suffix[0]] = 0
ng[n] = -1

t = 1 # 단계를 나타내는 변수
while t < n:
    suffix.sort( key=lambda x :(g[x], g[min(x+t, n)]) )
    
    for i in range(1, n):
        p, q = suffix[i-1], suffix[i]

        if g[p] != g[q] or g[min(p + t, n)] != g[min(q + t, n)]:
            ng[q] = ng[p] + 1
        else:
            ng[q] = ng[p]
    
    # 처음 부터 정렬이 바로 되어 있을 때 바로 탈출 하기 위해서
    if ng[n-1] == n-1:
        break

    t= t*2
    g = ng[:]


# Get LCP Array
LCP = [0] * n
length = 0 
for i in range(n):
    k = g[i]
    if k == 0: # 처음은 들어가지 않는다.
        continue 
    p = suffix[k-1]

    while i+length < n and p+length < n and s[i+length] == s[p+length]:
        length += 1
    LCP[k] = length

    if length:
        length -= 1


# 나누어진 영역에서의 최대값 구하기
m =(0,0) # length, start_index
for i, j in enumerate(LCP):
    if 0 <= suffix[i-1] + j - 1 < len(A) and len(A) < suffix[i] + j-1 < len(s):
        m = max(m,(j,i))
    if 0 <= suffix[i] + j - 1 < len(A) and len(A) < suffix[i-1] + j-1 < len(s):
        m = max(m,(j,i))
    
length, start = m
print(length)
print(s[suffix[start]: suffix[start] + length])