# 딕셔너리1

# 딕셔너리(key,value)
# ex) 사전 검색
# 공부 (=key)
# :[명사] 학문이나 기술을 배우고 익힘(=value)

# key는 중복불가

# 딕셔너리 = {key1:value1, key2:value2, ...}

# ex) key    value
#     이름    배주용
#     나이    22세
#     키      180cm
#     몸무게  80kg

person = {
    '이름':'배주용',
    '나이':22,
    '키':180,
    '몸무게':80
}

# 숫자,문자,불리안,리스트,튜플도 다 입력 가능

# 출력하기
print(person['이름'])
# >> 배주용

print(person['나이'])
# >> 22