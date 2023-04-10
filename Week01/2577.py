A = int(input())
B = int(input())
C = int(input())

num = str(A * B * C)
num_list = [0 for i in range(10)]

for n in range(len(num)):
    num_list[int(num[n])] += 1

for n in num_list:
    print(n)
