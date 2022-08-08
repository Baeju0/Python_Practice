# for 활용

# 리스트
my_list = [1,2,3]
for x in my_list:
    print(x)
# >> 1
# 2
# 3

# ex)
list_com = [1,2,3,4]
result = []
for num in list_com :
    result.append(num*3)
print(result)
# >> [3,6,9,12]

# 위의 예제를 리스트 안에 for문 포함하는 리스트 내포(list comprehension) 사용하기
list_com = [1,2,3,4]
result = [num * 3 for num in list_com]
print(result)
# >> [3,6,9,12]

# [1,2,3,4] 중에서 짝수에만 3을 곱하여 담고 싶어요! 리스트 내포 안에 if 조건 사용하기
list_com = [1,2,3,4]
result = [num * 3 for num in list_com if num % 2 == 0]
print(result)
# >> [6, 12]

# 리스트 내포 문법 (여러 개 사용도 가능하다)
# [표현식 for 항목1 in 반복가능객체1 if 조건문1]

# 리스트 내포 사용하여 구구단 만들기
result = [x*y for x in range(2,10)
              for y in range(1,10)]
print(result)
# >> 구구단 출력

# 튜플
my_tuple = (1,2,3)
for y in my_tuple:
    print(y)
# >> 1
# 2
# 3


# 딕셔너리
person = {'이름':'배주용','나이':111,'키':123,'몸무게':13}
for v in person.values():
    print(v)
# >> 값에 해당하는 부분만 출력

for k in person.keys():
    print(k)
# >> key에 해당하는 부분만 출력

for k,v in person.items():
    print(k,v)
# >> key,value 함께 반환되어 출력


# 문자열
fruit = 'apple'
for z in fruit:
    print(z)
# >> a
# p
# p
# l
# e
# 문자열 내의 글자들이 하나씩 출력