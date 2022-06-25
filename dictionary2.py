# 딕셔너리2

person = {'이름':'배주용','나이':22,'키':180,'몸무게':80}

print(person['별명'])
# >> error! 별명이라는 key가 없기 때문!
print(person.get('별명'))
# >> None get()메소드를 쓰면 key값이 없어도 에러는 발생하지 않고 None 출력

# 새로운 데이터 추가
person['최종학력']='대학원'

# 특정 key의 value를 바꾸려면
person['키']=190 # 기존에 존재하던 key이면 '값 수정'
# 기존에 없던 key이면 '값 추가'가 됨

# 여러 key들의 value를 바꾸려면
person.update({'키':180, '몸무게':90})
# update() 메소드 사용

# 특정 key:value를 삭제하려면
person.pop('몸무게')
# pop() 메소드 사용

# 모든 데이터를 삭제
# person.clear()
# clear() 메소드

# 어떤 key들이 있는지 확인
print(person.keys())
# keys() 메소드

# 어떤 value들이 있는지 확인
print(person.values())
# values() 메소드

# 어떤 key:value 들이 있는지
print(person.items())
# items() 메소드

