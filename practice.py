from unicodedata import name
from xmlrpc.client import boolean

print('python 시작하기!!!')

# 숫자 자료형
# print(1) 정수
# print(3.14) 실수

# 문자 자료형
# print('안녕!')
# print('hello world')
# print('0') 숫자여도 ''로 감싸게 된다면 문자 자료형

# boolean 자료형
# print(True)
# print(False)


# 변수
# 어떤 값을 저장하는 공간
# 변수 선언
# 변수 이름 = 값

# ex) 설날 세뱃돈!
# 봉투 = 변수 / 세뱃돈 = 값
# 변수 = 값
envelope1 = 10000 # 초등학생
envelope2 = 20000 # 고등학생
envelope3 = '파이팅!!!' #직장인^^

print(envelope1)
print(envelope2)
print(envelope3)

# 변수 이름 규칙
# 1. 문자 또는 _로 시작하기
# ex) name, _name

# 2. 문자, 숫자, _로 구성
# ex) name123, _name_456

# 3. 공백 안 됨, 특수문자 안 됨
# ex) na me, @_name__^^~

# 4. 대소문자 구분
# ex) name, Name, Name -> 다 다른 변수로 구분합니다!

# 5. 키워드(예약어) 사용 불가!!
# ex) True, False, for, while 등

# 6. 소문자 단어, _로 구분된 단어들(권장 사항!)
# ex) name,my_name,your_name 등 밑줄로 구분된 단어들의 조합으로 만드는 것이 좋음!