import sys

name = list(sys.stdin.readline().strip())
name.sort()
length = len(name)
result = ['a'] * length

idx = 0
start = 0
end = length-1
tmp = []
while idx + 1 < length :
    if name[idx] == name[idx + 1] :
        result[start] = name[idx]
        result[end] = name[idx+1]
        start += 1
        end -= 1
        idx += 2
    else :
        tmp.append(name[idx])
        idx += 1
if idx == length - 1 :
    tmp.append(name[idx])

if len(tmp) > 1 :
    print("I'm Sorry Hansoo")
else :
    if len(tmp) == 1 :
        result[length//2] = tmp[0]
    for i in range(length) :
        print(result[i], end="")