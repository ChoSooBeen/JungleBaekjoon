import sys

def hanoi(n, x, y) : 
    if n == 1 :
        print(f'{x} {y}')
        return
    hanoi(n-1, x, 6-x-y)
    print(f'{x} {y}')
    hanoi(n-1, 6-x-y, y)
num = int(sys.stdin.readline())

# https://st-lab.tistory.com/96 참고
print(2**num-1)
if num <= 20 :
    hanoi(num, 1, 3)
