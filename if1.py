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