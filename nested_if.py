# if 중첩

# if - true - 이 문장 - if - true - 저 문장 - 다음 문장


# if 조건1:
#     이 문장
#     if 조건2:
#         저 문장  # 들여쓰기 꼭!!! 주의!!!!
# 다음 문장


# ex) 축구 경기 하다가 반칙! -> 옐로 카드, 레드 카드
# 옐로 카드 2장이면, 레드 카드 1장! 퇴장!

yellow_card= 0
foul = True

if foul:
    yellow_card += 1
    if yellow_card == 2:
        print('경고 누적 퇴장!') # yellow_card 2장
    else:
        print('조심해야됨') # yellow_card 1장
else:
    print('주의') # foul = false인 경우(if문 자체가 실행 되지 않고)