A, B = input().split()

# 리스트 슬라이싱 속성 중 [::-1] 사용하여 문자열을 뒤집기
reverse_A, reverse_B = A[::-1], B[::-1]

if int(reverse_A) > int(reverse_B) :
    print(reverse_A)
else :
    print(reverse_B)