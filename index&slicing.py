# 인덱스 & 슬라이싱

# 몇 번째 = 인덱스
# ex)
from cgi import test


lang = 'PYTHON'

# P Y T H O N
# 0 1 2 3 4 5

# P를 출력하려면
print(lang[0])

# 마지막 문자를 출력하려면
print(lang[-1])


# 어디부터 ~ 어디까지 = 슬라이싱
# 인덱스 1부터 6 직전까지
print(lang[1:6])
# >> YTHON

# 인덱스 1부터 끝까지
print(lang[1:])
# >> YTHON

# 처음부터 인덱스 4 직전까지
print(lang[:4])
# >> PYTH

# 처음부터 끝까지
print(lang[:])
# >> PYTHON

# test
fruit = 'apple'
print(fruit[:])
print(fruit[0:])
print(fruit[:5])
print(fruit[:-1])

# 결과 값이 apple과 다른 하나?
print(fruit[:-1])
# >> 직전까지만 출력, appl