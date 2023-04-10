import sys

# def findZ(num, row, col) :
#     global count
#     if num == 1 :
#         return
#     elif row < num/2 and col < num/2 :
#         findZ(num/2, row, col)
#     elif row < num/2 and col >= num/2 :
#         count += num * num /4
#         findZ(num/2, row, col-num/2)
#     elif row >= num/2 and col < num/2 :
#         count += (num * num /4) * 2
#         findZ(num/2, row-num/2, col)
#     else :
#         count += (num * num /4) * 3
#         findZ(num/2, row-num/2, col-num/2)

def find(N, r, c) :
    if N == 0 : 
        return 0
    return 2*(r%2)+(c%2) + 4*find(N-1, r//2, c//2)
        
N, r, c = map(int, sys.stdin.readline().split())
# count = 0
# findZ(2**N, r, c)
# print(int(count))
print(find(N, r, c))