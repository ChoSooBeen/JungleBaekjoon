import sys

A, B, C = map(int, sys.stdin.readline().split())

# https://velog.io/@grace0st/곱셈-백준-1629번-파이썬 참고

def mult(A, B) :
    if B == 1 :
        return A % C
    else :
        tmp = mult(A, B//2)
        # 지수가 짝수일 경우
        if B % 2 == 0 :
            return (tmp * tmp) % C
        # 지수가 홀수일 경우
        else :
            return (tmp * tmp * A) % C

print(mult(A, B))