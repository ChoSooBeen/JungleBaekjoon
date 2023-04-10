result = 0
index = 0

for i in range(1, 10) :
    num = int(input())
    if result < num :
        result = num
        index = i

print(result)
print(index)