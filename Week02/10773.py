import sys

K = int(sys.stdin.readline())
list = []

for i in range(K) :
    input = int(sys.stdin.readline())
    if input == 0 :
        list.pop()
    else :
        list.append(input)

print(sum(list))