# 문자열 메소드2

# 문자열.메소드(...)
# ex)
j = '자바스크립트'

# 어떤 문자로 시작하는지 확인하기
print(j.startswith('자바'))
# >> True

# 어떤 값으로 끝나는지
print(j.endswith('프레임워크'))
# >> False

# 문자열 앞 뒤로 불필요한 부분 제거
s = '.....자바스크립트..'
print(s.strip('.'))
# >> 자바스크립트

# strip()에 공백을 넣으면 문자열 앞뒤로 공백 제거 
a = '  자바스크립트   '
print(a.strip())
# >> 자바스크립트

# 문자 변경
# ex) '스크립트'를 '프레임워크'로 변경
print(j.replace('스크립트','프레임워크'))
# >> 자바프레임워크

# 특정 문자열 찾기
print(j.find('스크립트'))
# >> 2 (인덱스 기준으로 값 나옴)

# 다른 문자들 사이에 가운데로
# ex) 기존 문자열 개수 외에 앞 뒤로 '-' 추가
print(j.center(10,'-'))

# google, python 내장형