num1 = int(input())
num2 = int(input())
hund = int(num2 / 100)
ten = int(num2 % 100 / 10)
one = num2 % 10

print(num1 * one)
print(num1 * ten)
print(num1 * hund)
print(num1 * num2)