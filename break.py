# break

# ex) 헬스장에 가면 런닝머신이나 사이클 같은 유산소 운동하고 근력 운동함!
# 런닝머신 30분 후 근력 운동 시작
# 런닝머신에는 비상 정지 버튼이 있음!
# 아직 30분이 되지 않아도 누르면 정지 됨

# 반복문에도 이런 비상 정지 버튼같은 것이 있음
# 그게 바로 break!

# 반복 수행 중인 동작을 즉시 멈추고 반복문 탈출

# ex) 친구가 드라마 추천해줌!! 근데 시즌3부터는 재미 없다고 보지 말라 함!
drama = ['시즌1','시즌2','시즌3','시즌4','시즌5']
for x in drama :
    if x == '시즌3':
        print('그만 보자')
        break
    print(f'{x} 시청')