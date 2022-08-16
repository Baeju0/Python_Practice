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




# Q. 삼각형의 넓이를 구하는 함수 만들기
# 함수의 인자로는 삼각형의 밑변과 높이,
# 반환(return) 값은 삼각형의 넓이
# 삼각형의 넓이, 밑변 * 높이 / 2

def f3(m,h) :
    s = (m*h)/2
    return s

w = f3(5,10)
print(w)