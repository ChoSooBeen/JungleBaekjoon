import sys

N= int(sys.stdin.readline())
rope = [0] * N

for i in range(N) :
    rope[i] = int(sys.stdin.readline())
rope.sort()

weight = rope[N-1]
for i in range(N-1) :
    tmp = rope[i] * (N-i)
    if tmp > weight :
        weight = tmp
print(weight)