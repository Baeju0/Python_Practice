# 사용자 입력

# input의 사용
a = input()
# input은 입력되는 모든 것을 문자열 취급


# 프롬프트 띄워서 사용자 입력 받기
number = input("숫자를 입력하세요 : ")
print(number)
# >> 입력된 숫자 출력
# 그러나, number는 숫자가 아닌 문자열

# print문 자세히 알기
# ""로 둘러싸인 문자열은 + 연산과 동일
print("life""is""too short")
print("life"+"is"+"too short")
# >> lifeistoo short 처럼 동일한 결괏값이 나온다

# 띄어쓰기는 콤마로
print("life", "is", "too short")
# >> life is too short

# 한 줄에 결괏값 출력
for i in range(10) :
    print(i, end=' ')
# 한 줄에 결괏값을 계속 이어서 출력하려면 매개변수 end를 사용해 끝 문자를 지정
# >> 0 1 2 3 4 5 6 7 8 9