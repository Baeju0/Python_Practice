# 참, 거짓

1 == 1

# 1 + 1이 2가 맞으면(True) yes, 그렇지 않으면(False) no
if 1 + 1 == 2:
    print('yes')
else:
    print('no')
# >> yes
    
# 덧셈 문제 함수
def quiz():
    ans = input('1+2=')
    return 1 + 2 == int(ans)

quiz()
# >> 입력한 값이 3이면 True, 그 외의 값으면 False