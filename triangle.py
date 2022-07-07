# 인터프리터 / 컴파일러
# 명령 한 줄 씩 입력하면 그때그때 답을 돌려주는 방법 / 말하는 것을 처음부터 끝까지 듣고 한 번에 번역


# 인터프리터 예시
print('직각삼각형 그리기\n')
leg = int(input('변의 길이: '))

for i in range(leg):
	print('* ' * (i + 1))

area = (leg ** 2) /2
print('넓이:', area)


# Q. 사용자에게 정수를 입력 받아, 그 수의 제곱을 계산해 출력하기
print('제곱 출력')
a = int(input('숫자 입력: '))
b = a*a
print(b)