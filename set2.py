# 세트2

# 세트는 리스트,튜플과 달리 순서 보장이 안 된다고 했었음!
# 그렇지만 튜플처럼 읽기 전용인 것만은 아님

# ex) 이 음식만 먹고 살았는데
my_set = {'돈가스','보쌈','제육덮밥'}
# 어느날 닭갈비를 먹으니까 넘 맛있는 거!!
# add() 메소드 사용해서 값을 추가 가능!
my_set.add('닭갈비')
print(my_set)
# >> {'돈가스','보쌈','제육덮밥','닭갈비'}

# 제육덮밥 넘 많이 먹어서 질렸어!!
# remove() 메소드 사용해서 값 빼기 가능!
my_set.remove('제육덮밥')
print(my_set)
# >> {'돈가스','보쌈','닭갈비'}

# 다이어트 시작한다!
# clear() 메소드 사용해서 모든 값을 지우기 가능!
my_set.clear()
print(my_set)
# >> set()
# clear는 my_set의 값을 비워주는 것을 의미 = set()

del my_set
print(my_set)
# >> error! my_set이라는 세트가 없어요!
# clear와 달리 del은 세트 자체를 삭제하는 것
# 리스트와 튜플 또한 그렇다!