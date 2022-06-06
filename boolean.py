# 불리안

#형변환
# bool()
# 값이 있으면 True
# 값이 없으면 False

# 문자 자료형 ex)
from doctest import FAIL_FAST
from tkinter.messagebox import NO


a = 'hello!'
b = '  '
c = ''

print(bool(a))
print(bool(b))
print(bool(c))

# 숫자 자료형 ex)
d = 1
e = -1
f = 0

print(bool(d))
print(bool(e))
print(bool(f))


# 그 외
# None
# print(bool(None))
# >> False

# 정리!
# 참이면 True
# 거짓이면 False
# 값이 있으면 True
# 값이 없으면 False