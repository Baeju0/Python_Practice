# 모듈 만들기

def add(a, b) :
    return a + b

def sub(a, b) :
    return a - b

# ● 결과를 출력하는 문장 추가
if __name__=="__main__" : # 결괏값 출력말고 함수 사용할거야!
    # 경로에서 mod1.py처럼 파일을 직접 실행했을 때는 __name__=="__main__"이 참이 되어 다음 문장 실행!
    # 반대로 대화형 인터프리터나 다른 파일에서 이 모듈을 불렀을 때는 거짓이 되어 if문 다음 문장 수행xxx
    print(add(1,4))
    print(sub(4,2))

# __name__변수??
# 파이썬이 내부적으로 사용하는 특별한 변수 이름!
# 경로에서 직접 파일을 실행할 경우
# mod1.py의 __name__변수에는 __main__값이 저장된다!
# 하지만 파이썬 셸, 다른 파이썬 모듈에서 mod1을 import할 경우?
# mod1.py의 __name__변수에는 mod1.py의 모듈 이름 값 mod1이 저장된다!

import mod1
mod1.__name__
# >> 'mod1'


# 모듈 생성 후 cmd로 불러오기
# cmd 창 열고 모듈을 저장한 경로로 이동
# C:\Users\Windows10\Desktop\vs\Python_Practice>

# cmd창에

# import mod1
# print(mod1.add(3,4)) 입력하면
# >> 7 결괏값이 나온다
# print (mod1.sub(4,2)) 입력하는 것도
# >> 2


# ● 결과 출력 문장 추가 후
# cmd 창, 경로 이동, python mod1.py 를 입력하면
# 위의 print값인 5,2가 나온다
# ※그런데 import를 할 때는  이상한 문제가 발생한다!
# mod1의 값이 출력된다! 난 mod1.py의 add, sub 함수만 사용하려고 했는데!
# 위의 문제를 방지하기 위해서는 mod1.py의 파일을 다음과 같이 변경해야된다 ↑↑↑

# import는 이미 만들어 놓은 파이썬 모듈을 사용할 수 있게 해주는 명령어
# import를 하는 방법은
# import 모듈이름
# 을 입력하면 된다. ※ 단, 모듈이름.py는 안 됨

# mod1.add나 mod1.sub를 사용하지 않고 모듈 이름 없이 함수 이름만 쓰고 싶다면?
# from 모듈 이름 import 모듈 함수
# 를 사용하면 된다!!

# from mod1 import add
# add(3, 4)
# >> 7 이라는 결괏값 나옴
# 근데 함수 하나만 사용할 수 있냐!? 아님!
# 2가지 방법이 있다!

# from mod1 import add, sub
# 위처럼 사용하거나
# from mod1 import *
# 을 사용하면 된다!
