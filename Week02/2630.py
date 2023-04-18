import sys

N = int(sys.stdin.readline())
# 파란색 = 1, 하얀색 = 0
paper = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

blue, white = 0, 0

'''
현재 영역 내에 모두 같은 값이 존재하는지 판별하는 함수
row : 시작 행
col : 시작 열
size : 얼만큼의 크기를 확인할 것인지
'''
def isEquals(row, col, size) :
    current = paper[row][col]
    for i in range(row, row+size) :
        for j in range(col, col+size) :
            if current != paper[i][j] :
                return False
    return True

# 색종이의 개수를 세는 함수
def paperCount(row, col, size) :
    global blue, white
    
    if isEquals(row, col, size) : 
        if paper[row][col] == 0 :
            white += 1
        else :
            blue += 1
    else :
        newSize = size // 2
        paperCount(row, col, newSize)
        paperCount(row, col+newSize, newSize)
        paperCount(row+newSize, col, newSize)
        paperCount(row+newSize, col+newSize, newSize)

paperCount(0, 0, N)
print(white)
print(blue)