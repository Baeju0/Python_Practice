# for 반복문

# ex) 팔 벌려 뛰기 10회 시작! = 같은 동작 반복
# print('팔 벌려 뛰기') * 10번

# for 변수 in 반복 범위 or 대상:
#     반복 수행 문장

 # range()는 어떤 범위 내로 숫자를 만들어 주는 것, 예로 range(10)을 하면 0이상 10미만의 숫자 생성
 # for x in range(10)는 0~9까지의 숫자들을 순서대로 x에 하나씩 넣는다!
 # x는 임의의 값이며 원하는 이름으로 지정 가능
for x in range(10):
    print(f'팔 벌려 뛰기 {x}회')


# ex) 기본 for문
test_list = ['one','two','three']
for i in test_list :
    print(i)

# ex) 튜플 for문
a3 = [(1,2),(3,4),(5,6)] # 첫번째 값과 마지막 값 +
for (first, last) in a3 :
    print(first + last)
# >> 3 7 11

# ex) 응용 for문
# 총 5명의 학생, 시험 점수가 60점이 넘으면 합격 그렇지 않으면 불합격
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks :
    number = number +1
    if mark >= 60 :
        print("%d번 학생, 합격!" %number)
    else :
        print("%d번 학생, 불합격!" %number)