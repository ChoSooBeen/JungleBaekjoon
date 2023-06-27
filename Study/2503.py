import sys
import itertools

N = int(sys.stdin.readline())
baseball = []
for _ in range(N) :
    baseball.append(list(map(int, sys.stdin.readline().split())))
    
candidate = list(itertools.permutations(list(range(1, 10)), 3))

count = 0
for game in candidate :
    num = game
    flag = True
    for i in baseball :
        n = str(i[0])
        strike = i[1]
        ball = i[2]
        s = 0
        b = 0
        for j in range(3) :
            if str(num[j]) == n[j] :
                s += 1
            elif str(num[j]) in n :
                b += 1
        if strike != s or ball != b :
            flag = False
            break
    if flag :
        count += 1
print(count)