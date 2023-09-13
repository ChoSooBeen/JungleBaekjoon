import sys

t = int(sys.stdin.readline())

# def isEqual(a, b) :
#     if a == b :
#         return 0
#     return 1

for _ in range(t) :
    n = int(sys.stdin.readline())
    mbti = sys.stdin.readline().split()
    result = sys.maxsize
    
    if n > 32 : # 똑같은 mbti가 무조건 3개 존재한다.
        print(0)
        continue
    
    for i in range(n-2) :
        for j in range(i+1, n-1) :
            for k in range(j+1, n) :
                distance = 0
                for x in range(4) :
                    if mbti[i][x] != mbti[j][x] : distance += 1
                    if mbti[i][x] != mbti[k][x] : distance += 1
                    if mbti[k][x] != mbti[j][x] : distance += 1
                    # distance += isEqual(mbti[i][x], mbti[j][x])
                    # distance += isEqual(mbti[i][x], mbti[k][x])
                    # distance += isEqual(mbti[k][x], mbti[j][x])
                result = min(result, distance)
    print(result)