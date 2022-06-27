# 자료형 변환

# 튜플(읽기 전용)
# 수정x, 추가x, 삭제x
# but, 수정하는 방법 있음!
my_tuple = ('오예스','몽쉘')
my_list = list(my_tuple) # list() 리스트 형태로 변환됨
my_list.append('초코파이') # list의 추가 메소드 append()사용해서 추가한 후
my_tuple=tuple(my_list) # my_list를 다시 tuple()로 튜플 형태로 변환


# 리스트
# 중복값 허용인데, 중복값을 제거해야될 경우
my_list2 = ['오예스','몽쉘','초코파이','초코파이','초코파이']
my_set = set(my_list2) # set는 중복값을 허용하지 않기 때문에 set()으로 변환 후
my_list2 = list(my_set) # 다시 list()로 변환


# 세트
# 중복 허용x, 순서도 허용x
# 위의 예시, 리스트 -> 세트 -> 리스트로 형변환 했을 시
# 순서가 뒤죽박죽 섞일 수도 있음
# 따라서 순서가 중요하다면 세트로 변환하면 안 됨
# 그대신! 딕셔너리 이용하기!


# 딕셔너리
# 중복 x, 순서 o
my_list3 = ['오예스','몽쉘','초코파이','초코파이','초코파이']
my_dic = dict.fromkeys(my_list3)
print(my_dic)
# >> {'오예스':None, '몽쉘':None, '초코파이':None}
# 위의 결과처럼 key로 가지는 새로운 딕셔너리 생성, value값은 None
# 이러한 값을 다시 list()로 변환
my_list3=list(my_dic)
print(my_list3)
# >> ['오예스','몽쉘','초코파이']
# key 값들만 뽑아서 리스트로 다시 변환 가능!(순서도 보장!)