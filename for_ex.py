# for 활용

# 리스트
my_list = [1,2,3]
for x in my_list:
    print(x)
# >> 1
# 2
# 3


# 튜플
my_tuple = (1,2,3)
for y in my_tuple:
    print(x)
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
    print(x)
# >> a
# p
# p
# l
# e
# 문자열 내의 글자들이 하나씩 출력