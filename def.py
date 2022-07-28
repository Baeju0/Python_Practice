# def 함수(), return

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


# Q. 삼각형의 넓이를 구하는 함수 만들기
# 함수의 인자로는 삼각형의 밑변과 높이,
# 반환(return) 값은 삼각형의 넓이
# 삼각형의 넓이, 밑변 * 높이 / 2

def f3(m,h) :
    s = (m*h)/2
    return s

w = f3(5,10)
print(w)