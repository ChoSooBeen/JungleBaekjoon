import sys

N = int(sys.stdin.readline())
stack = []

def push(x) :
    stack.append(x)

def empty() :
    if len(stack) == 0 :
        return 1
    return 0

def pop() :
    if empty() == 1 :
        return -1
    return stack.pop()

def size() :
    return len(stack)

def top() :
    if empty() == 1 :
        return -1
    return stack[-1]
    

for i in range(N) :
    command = sys.stdin.readline().split()
    
    if command[0] == 'push' :
        push(command[1])
    elif command[0] == 'pop' :
        print(pop())
    elif command[0] == 'size' :
        print(size())
    elif command[0] == 'empty' :
        print(empty())
    else :
        print(top())