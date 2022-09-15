# class

# 계산기의 '더하기' 기능 구현 코드
result = 0

def add(num) : # add함수는 매개변수에 받은 값을 이전에 계산한 결괏값에 더한 후 돌려주는 함수
    global result # 이전 계산값을 유지하기 위해 result 전역 변수(global)사용
    result += num
    return result

print(add(3))
# >> 3
print(add(4))
# >> 7

# 근데 만일 한 프로그램에서 2대의 계산기가 필요한 상황!?
# 각 계산기는 각각의 결괏값을 유지해야 하기 때문에
# 위와 같이 add 함수 하나만으로는 결괏값을 따로 유지할 수 없음!!
# 함수를 각각 따로 만들어야 함
result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
# >> 3
print(add1(4))
# >> 7
print(add2(3))
# >> 3
print(add2(3))
# >> 7

# 근데 만약 더 많은 계산기가 필요하다면?!?!? 빼기 곱하기 등의 기능을 더 추가해야된다면!?!!?!?

# 위와 같은 경우 클래스를 사용하면 간단하게 해결 가능!
class Calculator: # Calculator 클래스로 만든 별개의 계산기 cal1,cal2(객체)/ 다른 계산기의 결괏값과 상관없이 독립적인 값 유지!!
    # 계산기가 늘어나더라도 객체를 생성하기만 하면 매우 간단해짐다!
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
# >> 3
print(cal1.add(4))
# >> 7
print(cal2.add(3))
# >> 3
print(cal2.add(7))
# >> 10

# 만약 빼기 기능을 추가하려면 Calculator 클래스에 함수를 추가해 주면 됨!
def sub(self, num):
    self.result -= num
    return self.result


# 사칙연산 가능하게 하는 클래스
# class FourCal :
#     pass
# #  a = FourCal()
# #  type(a)
# # <class '__main__.FourCal'>

# a.setdata(4,2)
# print(a.add())
# # >> 6

# print(a.mul())
# # >> 8

# print(a.sub())
# # >> 2

# print(a.div())
# # >> 2

# 다시 해보기
# class FourCal : # FourCal이라는 클래스
#     # 클래스 안에 구현된 함수(메서드)
#     def setdata(self, first, second): # 매개변수
#         self.first = first
#         self.second = second

# a = FourCal()
# a.setdata(4,2) # ?? 3개의 매개변수가 필요한 거 아닌가요?
# 위처럼 호출하면 setdata의 첫 번째 매개변수 self에는 setdata메서드를
# 호출한 객체 a가 자동으로 전달됨

# 다른 호출 방법
# a = FourCal()
# FourCal.setdata(a, 4, 2) # 이처럼 클래스 이름.메서드 형태로 호출할 때에는
# # 객체 a를 첫 번째 매개변수 self에 꼭 전달해 주어야 됨

# # 반면, 객체.메서드 형태의 호출은 self를 반드시 생략해서 호출함
# a = FourCal
# a.setdata(4, 2)
# print(a.first)
# # >> 4
# print(a.second)
# # >> 2
# # self는 전달된 객체 a이므로
# # a.first = 4
# # a.second = 2 로 해석된다


# # 이번에는 다음과 같이 a,b 객체 만들어보기
# a = FourCal()
# b = FourCal()

# # 그리고 a객체의 객체변수 first를 다음과 같이 생성
# a.setdata(4,2)
# print(a.first)
# # >> 4

# # 이번에는 b객체의 객체변수 first를 다음과 같이 생성
# b.setdata(3, 7)
# print(b.first)
# # >> 3

# # 위와 같이 진행하면 b객체의 객체변수 first에는 값 3이 저장
# # 그렇다면 a 객체의 first는 3으로 변할까 기존 값 4를 유지할까!?
# print(a.first)
# >> 4
# a객체의 first값은 b객체의 first 값에 영향받지 않고 원래 값을 유지하고 있다!
# 클래스로 만든 객체의 객체변수는 다른 객체의 객체변수에 상관없이 독립적인 값을 유지한다!!!!
# 클래스에서 가장 중요한 부분!!!


# 더하기 기능 만들기
class FourCal() :
    def setdata(self, first, second) :
        self.first = first
        self.second = second
    def add(self) :
        result = self.first + self.second
        return result
    # 곱하기, 빼기, 나누기 기능 추가하기
    def mul(self) :
        result = self.first * self.second
        return result
    def sub(self) :
        result = self.first - self.second
        return result
    def div(self) :
        result = self.first / self.second
        return result
# 위 클래스에 add 메서드 추가
a = FourCal()
b = FourCal()
a.setdata(4,2) # a 객체의 first, second 객체변수에 각각 값 4와 2 저장
b.setdata(3,8)

# add 메서드 호출
print(a.add())
# >> 6
print(b.sub)
# >> -5