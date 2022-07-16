# if 조건문 2

# elif (이거 아냐!? 그럼 이건 어때??)
# 앞의 조건이 참이 아닌 경우 다른 조건을 다시 한번 확인하기 위한 용도

# if, elif, elif, elif, else 
# 만약 ~ 라면(if) / 아니라고? 그럼 이건 어때?(elif) * 3 / 그렇지 않다면!(else)
# else는 생략 가능!

# if 조건1:
#     이 문장
# elif 조건2:
#     저 문장
# else:
#     그 문장
# 다음 문장

# if -> True -> '이 문장' 실행 -> 다음 문장
# if -> False -> elif -> True -> '저 문장' 실행 -> 다음 문장
# elif -> False -> '그 문장' 실행 -> 다음 문장

# ex)
from time import monotonic


today = '월요일'
if today == '일요일':
    print('게임 한 판')
elif today == '토요일':
    print('폰 5분만')
else:
    print('물 한 잔')
print('공부 시작!')

# if와 else 사이에 elif 조건은 얼마든지 추가 가능!
c2 = 15 * 5
d2 = 15 + 15 + 15 + 15 + 15
if c2 > d2:
    print('c is greater than d')
elif c2 == d2:
    print('c is equal to d')
elif c2 < d2:
    print('c is less than d')
else:
    print('I don\'t know')
# c2와 d2 값 같음


# ex) if1.py에서의 택시 예제 elif 사용하기
# ex) 주머니에 돈 있으면 택시 타고, 없지만 카드가 있다면 택시 타!
#     근데 둘 다 없으면 걸어 가

# 이건 if와 else로만 문장을 표현한 것
pocket = ['paper','cellphone']
card = True
if 'money' in pocket:
    print("택시 타!")
else:
    if card:
        print('택시 타!')
    else:
        print('걸어 가!')
# >> 택시 타!

# 위의 문장을 if와 elif를 사용하여 더 간단하게 표현
pocket = ['paper','cellphone']
card = True
if 'money' in pocket :
    print('택시 타')
elif card :
    print('택시 타')
else :
    print('걸어 가')
# >> 택시 타
# elif는 이전 조건문이 거짓일 때 수행