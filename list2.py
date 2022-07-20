# 리스트2


# 리스트 = [값1,값2,...]
my_list = ['오예스','몽쉘','초코파이'] # 리스트의 값은 순서가 보장
# ex) 인덱스에 해당하는 값은?
print(my_list[0])
# >> 오예스

# 리스트는 그냥 편의점 봉투가 아니라
# 내부의 칸막이가 있어서 집어넣는 *순서대로* 관리가 되는 특수한 비닐봉투!!!

# 순서대로이기 때문에
# ex) 어디서부터 어디까지 슬라이싱??
print(my_list[0:2]) # :을 통해서 시작, 종료값 입력
# >> ['오예스','몽쉘']

# ex) 리스트에 원하는 값이 포함되어 있는지?
print('몽쉘'in my_list)
# >> True

# ex) 리스트 내에 몇 개의 값이 있는지?
print(len(my_list))
# >> 3

# ex) 리스트의 값을 수정하려면?
my_list[1] = '몽쉘카카오' # 값 수정하기, 인덱스를 지정해서 변수 값 변경하는 것처럼 값 입력
print(my_list)
# >> ['오예스','몽쉘카카오','초코파이']

# 또한
# 리스트 값 추가
my_list.append('빅파이') # append 리스트 맨 끝에 새로운 값 추가
print(my_list)
# >> ['오예스','몽쉘','초코파이','빅파이']

# 리스트 값 삭제
my_list.remove('오예스') # remove() 지우려는 값 입력
print(my_list)
# >> ['몽쉘','초코파이','빅파이']

# 리스트 값 병합
# my_list = ['오예스', '몽쉘', '초코파이']
your_list = ['빅파이','오뜨']
my_list.extend(your_list) # 리스트 병합
print(my_list)
# >> ['오예스',몽쉘','초코파이','빅파이','오뜨']


# 리스트 슬라이싱
a_s = [1,2,3,4,5]
print(a_s[0:2])
# >> [1,2]

b_s = a_s[:2]
c_s = a_s[2:]
print(b_s)
# >> [1,2]
print(c_s)
# >> [3,4,5]

# 중첩 리스트에서 슬라이싱
a_s2 = [1,2,3,['a','b','c'],4,5]
print(a_s2[2:5])
# >> [3,['a','b','c'],4]
print(a_s2[3][:2])
# >> ['a','b']