# 문자열 메소드1

# 클래스 내에 정의된 어떤 동작, 기능을 하는 코드들의 묶음
# 쉽게 기능

# 문자열.메소드(...)
# ex)
letter = 'how are YOU?'

# 모든 내용을 소문자로
print(letter.lower())
# >> how are you?

# 모든 내용을 대문자로
print(letter.upper())
# >> HOW ARE YOU

# 첫 글자만 대문자로
print(letter.capitalize())
# >> How are you?

# 각 단어들의 첫 글자만 대문자로?
print(letter.title())
# >> How Are You?

# 대소문자를 뒤바꾸려면
print(letter.swapcase())
# >> HOW ARE you?

# 문자열을 나누려면?
print(letter.split())
# >> ['how','are','YOU?']

# how가 몇 번 쓰였는지?
print(letter.count('how'))
# >> 1

# _commit -m 정정