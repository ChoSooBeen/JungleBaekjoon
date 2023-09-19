import sys

# 두 행렬을 곱하는 함수
def mul (a, b) :
  result = [[0] * len(b[0]) for _ in range(2)]
  for r in range(2) :
      for c in range(len(b[0])) :
          for i in range(2) :
              result[r][c] += a[r][i] * b[i][c]
          result[r][c] %= 1000000007
  return result

# 행렬 제곱
def power(matrix, m) :
  if m == 1 :
    return matrix
  elif m % 2 : #홀수일 경우
    return mul(power(matrix, m-1), matrix)
  else : #짝수일 경우
    return power(mul(matrix, matrix), m//2)

n = int(sys.stdin.readline())
if n < 3 :
  print(1)
else :
  matrix = [[1, 1], [1, 0]]
  start = [[1], [1]]
  print(mul(power(matrix, n-2), start)[0][0])