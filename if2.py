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
today = '월요일'
if today == '일요일':
    print('게임 한 판')
elif today == '토요일':
    print('폰 5분만')
else:
    print('물 한 잔')
print('공부 시작!')

# if와 else 사이에 elif 조건은 얼마든지 추가 가능!