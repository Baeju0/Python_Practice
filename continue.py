# continue

# ex)
drama1 = ['시즌1','시즌2','시즌3','시즌4','시즌5']
# 시즌3 재미없어!

# 그래서 시즌2까지만 봄
# 근데! 시즌3만 재미없단 소리지 4,5는 재밌다네!?
# 시즌3은 건너뛰고 봐!

# continue, 반복문 실행할 때 어떤 경우 동작을 건너뛰고 싶을 때 사용

for x in drama1 :
    if x == '시즌3' :
        print('건너뛰기!')
        continue
    print(f'{x} 시청')

# 실행 결과
# >> 시즌1 시청
# >> 시즌2 시청
# >> 건너뛰기!
# >> 시즌4 시청
# >> 시즌5 시청

# ex)
marks2 = [90, 25, 67, 45, 80]

number = 0
for mark in marks2 :
    number = number +1
    if mark < 60 :
        continue
    print("%d번 학생! 합격!"%number)
# 점수가 60점 이하인 학생일 경우, mark < 60이 참이 되어 continue문 수행
# 따라서 print 수행하지 않고 for문의 처음으로 돌아감