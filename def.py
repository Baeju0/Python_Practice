# def 함수(), return

# def 함수! 간단한 설명
from unittest import result


def add(a,b) :
    return a + b
print(add(3,4))
# 함수 이름은 add이며 입력으로 두 개의 값(a,b)를 받고 결괏값은 2개의 입력값을 더한 값이다!
# a,b는 매개변수(parameter)로 함수에 입력으로 전달된 값을 받는 변수
# 인수(arguments)는 함수를 호출할 때 전달하는 입력값


# 입력값이 없는 함수
def say() :
    return 'Hi!'
# 사용? 위 함수를 쓰기 위해서는 괄호 안에 아무 값도 넣지 않아야 됨
# 이 함수는 입력값이 없지만 결괏값으로 Hi라는 문자열 반환
# a = say() a라는 변수에 Hi라는 문자열이 대입되는 것
a = say()
print(a)
# >> Hi
# 이처럼 입력값이 없고 결괏값만 있는 함수는
# 결괏값을 받을 변수 = 함수이름() 처럼 사용된다!!


# 결괏값이 없는 함수
def add2(a,b) :
    print("%d, %d의 합은 %d입니다." %(a,b, a+b))
a2 = add2(3,4)
# >> 3,4의 합은 7입니다.
# 결괏값이 없는 함수는
# 함수이름(입력인수1, 입력인수2, 입력인수n) 처럼 사용한다!
# 문장을 출력해 줬는데 왜 결괏값이 없다는 건가요!? 
# -> print문은 함수의 구성 요소 중 하나인 수행할 문장에 해당되는 부분일 뿐!
# 결괏값은 당연히 없다. 결괏값은 오직 return 명령어로만 돌려받을 수 있음!

a2 = add(3,4)
print(a2)
# >> None
# 결괏값을 확인해보기 위해 위와 같이 출력


def f1(x) :
    a = 3
    b = 5
    y = a * x + b
    # y = 3 * 10 + 5 >> 35  
    return y # y값 반환
    # f1(x)의 값은 35

c = f1(10) # x값에 10 넣고 반환해서 c라는 변수에 값 저장
print(c) # >> 35 


# return을 사용하지 않고 print했을때
def f2(x):
    a = 3
    b = 5
    y = a * x + b # y = 3 * x + 5
    # y = 3 * 10 + 5
    print(y) # y값 출력

# y값을 반환하지 않았을 경우
d = f2(10) # f2()함수가 실행되어 35 출력 
# 하지만, d에 값을 반환하지는 않음
print(d) # >> None 


# 매개변수 지정하여 호출
def add3(a3,b3) :
    return a3+b3

result = add3(a3=3,b3=8)
print(result)
# >> 11

# 순서에 상관없이 사용도 가능
result = add3(b3=6, a3=2)
print(result)
# >> 8


# 입력값이 몇 개가 될지 모를 때
# def 함수이름(*매개변수) :
#     <수행할 문장>

# ex)
def add_many(*args): # 매개 변수 이름 앞에 *을 붙이면 입력값을 모두 튜플로 만들어 줌
    result = 0
    for i in args:
        result = result + i
    return result

result = add_many(1,2,3)
print(result)
# >> 6

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)
# >> 55


# 매개변수, 여러 개의 입력값을 의미하는 매개변수
def add_mul(choice, *args) :
    if choice == "add" : # choice가 'add'라면
        result = 0 # result = 0
        for i in args : # args 매개변수에 1,2,3,4,5 차례대로 입력
            result = result + i # 결과값에 +
    elif choice == "mul" : # mul이라면
        result = 1 # result = 1
        for i in args : # args 매개변수에 1,2,3,4,5 입력
            result = result * i # 결과값에 *
    return result

result = add_mul('add',1,2,3,4,5)
print(result)
# >> 15

result = add_mul('mul',1,2,3,4,5)
print(result)
# >> 120


# 키워드 파라미터 kwargs(Keyword arguments)
def kk(**kwargs) :
    print(kwargs)
kk(a=1)
# >> {'a':1 }
kk(name='foo',age=3)
# >> {'age':3, 'name':'foo'}
# 이처럼 입력값이 모두 딕셔너리로 만들어져 출력된다
# **kwargs처럼 매개변수 kwargs는 딕셔너리가 되고 모든 값이
# key=value 형태의 결괏값이 그 딕셔너리에 저장된다!!


# 함수의 결괏값은 언제나 하나
def add_and_mul(a,b) :
    return a+b, a*b # 결괏값은 a+b와 a*b 두 개인데

result = add_and_mul(3,4) # 받아들이는 변수는 result 하나만 쓰였다!
# 오류가 발생하는가?
# 아님! 이유는 함수의 결괏값은 2개가 아니라 언제나 1개
# 따라서 결괏값은 a+b와 a*b를 튜블값 하나인 (a+b, a*b)로 돌려준다!
result = (7, 12) # 이러한 결괏값 도출
# 만약 이 하나의 튜플 값을 2개의 결괏값으로 받고 싶다?
result1, result2 = add_and_mul(3,4) # 이렇게 호출하면
result1 = 7
result2 = 12 #로 결괏값을 도출해낸다

# 그렇다면 이런 함수를 만들면 되는 것 아닌가?
def add_and_mul(a,b) :
    return a+b
    return a*b
# !안 됨!
# 왜냐하면 함수는 return문을 만나는 순간 결괏값을 반환 후 함수를 빠져나간다.


# return의 또 다른 쓰임새
# 특별한 상황일 때 함수를 빠져나가고 싶다!?
# return 단독으로 사용하기!
# ex)
def say_nick(nick) :
    if nick == "주앵":
        return
    print("내 별명은 %s" %nick)
# 위의 함수 반환값 없음, 오로지 return문에 의해서만 생성
# 만약 입력값으로 "주앵"이라는 값이 들어오면  문자열을 출력하지 않고 함수를 즉시 빠져나감
say_nick("주용")
# >> 내 별명은 주용
say_nick("주앵")
# >> 문자열 출력x 함수 빠져나감


# 매개변수에 초깃값 미리 설정하기
def say_myself(name, old, woman=True): # 3개의 매개변수, 마지막 인수인 woman이 True면 여자, False면 남자
    print("내 이름은 %s" %name)
    print("나이는 %d살" %old)
    if woman :
        print("여자")
    else :
        print("남자")
# 매개변수에 미리 값을 넣어줌, 함수의 매개변수 초깃값을 설정하는 방법!
# 항상 변하는 것이 아닐 경우 함수의 초깃값을 미리 설정해 두면 유용하다!
say_myself("배주영", 23)
say_myself("배주영", 23, True)
# >> 내 이름은 배주영
# >> 나이는 23살
# >> 여자
# woman이란 변수에 입력값을 주지 않았지만 초깃값 True, 동일한 결과값 출력

say_myself("배주영", 23, False)
# >> 남자

# 초깃값을 설정할 때 주의점!
# def say_myself(name, woman=True, old) :
#     ~
# 위의 값은 오류가 발생한다
# 초기화 시키고 싶은 매개변수를 항상 뒤쪽에 놓아야 된다!


# 변수, 함수 밖에서 사용
a = 1
def vartest(a): # 다음 입력으로 들어온 값에 1을 더해주고 결괏값은 돌려주지 않는 vartest 함수 선언
    a = a +1

vartest(a)
print(a)
# print(a)의 결괏값은 2?
# 아님! 1이 출력된다
# 왜냐면 함수 안에서 새로 만든 매개변수는 함수 안에서만 사용하는 '함수만의 변수'이기 때문
# 즉, def vartest(a)에서 입력값을 전달받는 매개변수 a는 함수 안에서만 사용하는 변수임!(밖에선 사용 안 해)
# 따라서
def vartest(a2):
    a2 = a2 + 1
# 위의 함수와 똑같다는 얘기다
def vartest(a3) :
    a3 = a3 + 1

vartest(3)
# print(a3)

# 오류 발생!
# vartest(3)을 수행하면 vartest함수 안에서 a3는 4가 되지만
# 함수를 호출한 후 print(a3) 문장은 오류 발생
# print(a3)에서 입력받아야 하는 a3변수를 찾을 수 없기 때문이다!
# 함수 안에서 선언한 매개변수는 함수 안에서만 사용될 뿐이지
# 함수 밖에서는 사용되지 않는다

# 함수 안에서 함수 밖의 변수를 변경하는 방법
# 1. return 사용하기
a = 1
def vartest(a) :
    a = a +1
    return a

a = vartest(a)
print(a)
# vartest함수는 입력으로 들어온 값에 1을 더한 값을 돌려줌
# 따라서 a = vartest(a)라고 대입하면 a가 vartest 함수의 결괏값으로 바뀜
# 물론 vartest 함수 안의 a 매개변수는 함수 밖의 a와 다름!!!

# 2. global 명령어 사용하기
a = 1
def vartest():
    global a
    a = a+1

vartest()
print(a)
# vartest 함수 안의 global a 문장은 함수 안에서 함수 밖의 a변수를 직접 사용하겠다는 뜻!
# 하지만 global 사용하지 않는게 좋음
# 함수는 독립적으로 존재하는 것이 좋기 때문!!


# Q. 삼각형의 넓이를 구하는 함수 만들기
# 함수의 인자로는 삼각형의 밑변과 높이,
# 반환(return) 값은 삼각형의 넓이
# 삼각형의 넓이, 밑변 * 높이 / 2

def f3(m,h) :
    s = (m*h)/2
    return s

w = f3(5,10)
print(w)