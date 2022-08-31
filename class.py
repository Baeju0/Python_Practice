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