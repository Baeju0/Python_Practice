# while 문

# ~하는 동안에

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