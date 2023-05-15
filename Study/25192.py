import sys

N = int(sys.stdin.readline())
record = {}
count = 0

for _ in range(N) :
    input = sys.stdin.readline().strip()
    if input == 'ENTER' :
        record = {} # 모든 기록 초기화
    elif input not in record :
        count += 1
        record[input] = 1

print(count)