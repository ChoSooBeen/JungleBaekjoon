import sys

s = sys.stdin.readline().strip()

# 식의 값을 최소로 만들기 위해서는 - 빼기가 나중에 되어야한다.
# 즉, +를 먼저 하고 나중에 -를 해야하므로 - 를 기준으로 나눈다.
minus = s.split('-')

result = sum(list(map(int,minus[0].split('+'))))
for i in range(1, len(minus)) :
    result -= sum(list(map(int,minus[i].split('+'))))

print(result)