import sys

n = int(sys.stdin.readline())
row = [0] * n
result = 0

# https://seongonion.tistory.com/103 참고

# 퀸을 놓을 수 있는 위치인지 여부 판단
def isPromising(x) :
    for i in range(x) :
        # 1. 같은 열에 있는지 확인
        # 2. 대각선에 존재하는지 확인
        if row[x] == row[i] or abs(row[x]-row[i]) == abs(x-i) :
            return False
    return True
    

# x = 행, row[x] = 열
def nQueens(x) :
    global result
    
    # x가 n이 되면 모든 행에 퀸이 채워졌다는 의미로 함수 종료
    if x == n : 
        result += 1
        return
    else :
        for i in range(n) :
            row[x] = i
            if isPromising(x) :
                nQueens(x+1)

nQueens(0)
print(result)