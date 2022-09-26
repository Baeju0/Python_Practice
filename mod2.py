# 모듈에 클래스나 변수 등을 포함할 수 있다!

PI = 3.141592

class Math : 
    def solv(self, r) :
        return PI * (r ** 2)

def add(a, b) :
    return a+b

# 원의 넓이를 계산하는 Math 클래스, 두 값을 더하는 add 함수
# 원주율 값에 해당되는 PI 변수처럼 클래스, 함수, 변수 등을 (이 파일에서) 모두 포함하고 있다!

# mod1.py와 같이 cmd를 실행하여 
# 경로 입력, import mod2를 입력
# print(mod2.PI)
# >> 3.141592 (mod2에 있는 PI의 변수 값 사용!)

# a = mod2.Math()
# print(a.solv(2))
# 위와 같이 입력하여 Math 클래스를 사용
# 모듈 안에 있는 클래스를 사용하려면 "."(도트 연산자)로 클래스 이름 앞에 모듈 이름을 먼저 입력해야 한다!

# print(mod2.add(mod2.PI, 4.4))
# >> 7.541592
# mod2.py에 있는 add 함수 역시 이처럼 사용 가능!