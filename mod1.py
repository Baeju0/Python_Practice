# 모듈 만들기

def add(a, b) :
    return a + b

def sub(a, b) :
    return a - b

# 모듈 생성 후 cmd로 불러오기
# cmd 창 열고 모듈을 저장한 경로로 이동
# C:\Users\Windows10\Desktop\vs\Python_Practice>

# cmd창에

# import mod1
# print(mod1.add(3,4)) 입력하면
# >> 7 결괏값이 나온다
# print (mod1.sub(4,2)) 입력하는 것도
# >> 2

# import는 이미 만들어 놓은 파이썬 모듈을 사용할 수 있게 해주는 명령어
# import를 하는 방법은
# import 모듈이름
# 을 입력하면 된다. ※ 단, 모듈이름.py는 안 됨

# mod1.add나 mod1.sub를 사용하지 않고 모듈 이름 없이 함수 이름만 쓰고 싶다면?
# from 모듈 이름 import 모듈 함수
# 를 사용하면 된다!!

from mod1 import add
add(3, 4)
# >> 7 이라는 결괏값 나옴
# 근데 함수 하나만 사용할 수 있냐!? 아님!
# 2가지 방법이 있다!

from mod1 import add, sub
# 위처럼 사용하거나
from mod1 import *
# 을 사용하면 된다!