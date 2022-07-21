# while 문

# ~하는 동안에
# for는 정해진 만큼만 반복하는 것이라면
# while은 일단 계속 해봐!의 느낌?

# while 조건:
#     반복 수행할 문장

# ex) 비행기 타고 여행가기로 함
# 짐 싸야지! 항공권을 보니 수하물을 부치는 짐은 최대 25kg까지만 허용
# 집에서 캐리어에 짐을 넣으면서 무게 체크!
# 25kg를 초과하지 않는 범위까지 짐 넣음
# 편의상 챙긴 물건은 모두 3kg라고 가정, 최대 8개의 짐 넣기 가능! 물론 25kg 초과하지 않게

# 3kg * 8개 = 24kg
# ? <= 25kg

# 코드로 구현하기
max = 25
weight = 0
item2 = 3

while weight + item2 <= max:
    weight += item2
    print('짐을 추가합니다')
print(f'총 무게는 {weight}입니다')


# ex) 
num = 1

while num <= 100: # num이 100보다 작거나 같은 동안에
    print(num)
    num = num + 1 # num에 1씩 더해주세요

# num = num + 1 대신에 num += 1을 사용해도 똑같은 실행


# Q_1. while문 사용하여 하나의 정수 입력받고, 그 값만큼 출력하기
# ex) 3입력했다면 3을 세 번 출력
a = int(input('숫자 입력:'))
b = 0

while b < a :
    print(a)
    b += 1


# Q_2. while문 사용하여 하나의 정수를 입력받고,
# 그 값에 1부터 입력받은 수까지 각각에 대해 제곱 구하기
# ex) 3 입력,
# 1 1
# 2 4
# 3 9 출력

c = int(input('숫자 입력:'))
d = 1

while d <= c :
    print(d,d*d)
    d += 1


# 코드 보고 실행 결과 맞히기
number = 358

rem = rev = 0 # rem = 0 , rev = 0
while number >= 1:
    rem = number % 10 # 1. rem = 8  2.rem = 5  3. rem = 3
    rev = rev * 10 + rem # 1. rev = 8  2.rev = 85  3. rev = 853
    number = number // 10 # 358/10 1. number = 35  2. number = 3  3. number = 0

print(rev) # 853