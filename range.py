# range

# ex) range(10) 0이상 10미만
#  => () 값은 stop을 의미, 0이상 stop 미만!

for x in range(10):
    print(x)
# >> 0,1,2,3...,9 으로 결과값 나오지만 우리 실생활에서는 1부터 숫자 셈
# 이럴때는 ,를 사용해서
# range(start,stop)
# => start 이상 stop 미만!
range(1,10)
# 1이상 10미만

# 이렇게도 가능
# range(start,stop,step)
# => start이상 stop 미만 step만큼 증가
# ex) 홀수, 짝수, 3의 배수
range(1,10,2) # 홀수
range(2,10,2) # 짝수
range(3,10,3) # 3 이상 10미만 3만큼 증가, 3의 배수

# 교실에 30명의 학생, 설문지 제출하기 위해 각 번호의 1번들이 모아서 제출하려고 함
for s in range(10) :
    print(f'{s}번은 {s}번부터 {s+9}번까지 모아줘!')
# >> 결과가 1번~ 1번부터 10번까지
            # 11번~ 11번부터 20번까지
            # 21번~ 21번부터 30번까지
# 로 나오려면 range()안에 들어가는 값은? 1,31,10


# for, range로 구구단 만들기
# for문 두 번 사용
for i in range(2,10) : # 2~9까지의 숫자 i에 대입
    for x in range(1, 10) : # 1~9까지의 ㅅ숫자 x에 대입
        print(i*x, end=" ") # end, 해당 결과값을 출력할 때 다음 줄로 넘기지 않고 그 줄에 계속해서 출력하기 위해 입력
    print('')
