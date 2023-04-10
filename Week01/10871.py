N, X = map(int, input().split())
list = input().split()

result = ""
for i in range(N) :
    if int(list[i]) < X :
        result += f"{list[i]} "

print(result)