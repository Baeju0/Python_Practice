# if 조건문 1
# 모든 문장이 출력될 필요가 없을 경우
# 만약, ~ 라면 True - 실행, False 다음 문장


# if 조건:
#     이 문장 (#if : 반드시 앞에 들여쓰기 해야됨)
# 다음 문장

today = '화요일'
if today == '화요일':
    print('게임 한 판!') # true일 때
print('공부 시작')
# >> 공부 시작


# if 조건:
#     이 문장
# else:
#     저 문장
# 다음 문장

today = '화요일'
if today == '일요일':
    print('게임 한 판!') # true일 떄
else:
    print('좀만 더 놀다가!') # false 일 때
print('공부 시작')
# >> 좀만 더 놀다가!
# >> 공부 시작


# if, else
# 만약 ~라면 이 문장을 실행하고,
# 그렇지 않다면 else 내의 문장 실행

# if else 
# 만약 달다면:
    # 삼킨다.
# 그렇지 않으면 :
    # 뱉는다.

# if 달다면:
#     삼킨다.
# else:
#     뱉는다.

# 예제) 더 큰 수 출력하기
a2 = 1234 * 4
b2 = 13456 / 2

if a2 > b2 :    # 만약 a2가 b2보다 크면
    print('a2',a2) # a2를 출력하고
else:           # 그렇지 않으면
    print('b2',b2) # b2를 출력한다.
# >> b2 출력


# and, or, not

# x or y , x와 y 둘 중 하나만 참이어도 참
# x and y , x와 y 모두 참이어야 참
# not x , x가 거짓이면 참

# ex) 돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어가라!

# or 연산자 사용법
money = 2000
card = True
if money >= 3000 or card :
    print("택시 타!")
else :
    print("걸어 가!")
# >> 택시 타!


# x in s, x not in s
# x in 리스트   x not in 리스트
# x in 튜플     x not in 튜플
# x in 문자열   x not in 문자열

# ex) in, ~안에
# 리스트
1 in [1,2,3] # [1,2,3]리스트 안에 1이 포함되어 있는가? 참
# >> True

1 not in [1,2,3] # [1,2,3]리스트 안에 1이 포함 되어 있지 않은가? 거짓
# >> False


# 튜플과 문자열
'a' in ('a','b','c') # a가 튜플에 포함? 참
# >> True

'j' not in 'python' # j가 문자열에 포함되어 있지 않?
# >> True


# ex) 택시 예제에 in 적용
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket :  # pocket이라는 리스트 안에 'money'가 포함되어 있으면
    print('택시 타!')
else :
    print("걸어 가!")
# >> 택시 타!

# 조건문에서 아무런 일도 실행하고 싶지 않다?
# ex) 주머니에 돈 있으면 가만히 있고 없으면 카드 꺼내!
if 'money' in pocket :
    pass # 아무런 일도 수행하지 않게 넘어감
else:
    print('카드 꺼내!')