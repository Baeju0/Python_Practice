# 자료형 비교

# list
# 여러 값들을 순서대로 관리해야 될 때
list = []
# 순서 보장 o
# 중복 허용 o
# 접근 list[index]
# 수정 o
# 추가 append(), insert(), extend()
# 삭제 remove(), pop(), clear()


# tuple
# 값이 바뀔 일이 없거나, 바뀌면 안 될 떄
tuple = ()
# 순서 보장 o
# 중복 허용 o
# 접근 tuple[index]
# 수정 x
# 추가 x
# 삭제 x


# set
# 값의 존재 여부가 중요하거나 중복 허용 x 시
set = {}
# 순서 보장 x
# 중복 허용 x
# 접근 x
# 수정 x
# 추가 add(), update()
# 삭제 remove(), discard(), pop(), clear()


# dictionary
# Key를 통해 효율적으로 데이터를 관리하고 싶을 때
dictionary = {key:value}
# 순서 보장 o (3.7버전 이상!)
# 중복 허용 x (key 값)
# 접근 dictionary[key], dictionary.get(key)
# 수정 o (value 값만)
# 추가 dictionary[key]= value, update()
# 삭제 pop(), popitem(), clear() 