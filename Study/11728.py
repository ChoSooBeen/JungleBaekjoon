import sys

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

a_idx = 0
b_idx = 0
result = []

while a_idx < N and b_idx < M :
    if A[a_idx] == B[b_idx] :
        result.append(A[a_idx])
        result.append(B[b_idx])
        a_idx += 1
        b_idx += 1
    elif A[a_idx] > B[b_idx] :
        result.append(B[b_idx])
        b_idx += 1
    else :
        result.append(A[a_idx])
        a_idx += 1
for i in range(a_idx, N) :
    result.append(A[i])
for i in range(b_idx, M) :
    result.append(B[i])
print(*result)