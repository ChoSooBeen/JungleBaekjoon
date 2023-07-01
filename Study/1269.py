import sys

a, b = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()
B.sort()

a_idx = 0
b_idx = 0
count = 0
while a_idx < len(A) and b_idx < len(B) :
    if A[a_idx] == B[b_idx] :
        a_idx += 1
        b_idx += 1
    elif A[a_idx] > B[b_idx] :
        count += 1
        b_idx += 1
    else :
        count += 1
        a_idx += 1
if a_idx < len(A) :
    count += (len(A)-a_idx)
if b_idx < len(B) :
    count += (len(B)-b_idx)
print(count)