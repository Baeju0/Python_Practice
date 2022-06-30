# 문자열 처리

snack = '꿀꽈배기'
two = '2개'

juseyo = snack + two
# >> 꿀꽈배기 2개

# juseyo = juseyo + '주세요'
# >> 되지만 ↓ 이렇게 하는게 더

juseyo += '주세요'
# +=로 표현할 수 있음 juseyo 변수에 += 주세요를 더해주세요
# >> 꿀꽈배기2개주세요

# 숫자 자료형에서도 사용가능
num = 3

num = num + 2
num += 2
# >> 5 둘 다 같은 동작이므로 같은 값이 나옴

# += 뿐만 아니라 다른 연산도 가능
num -= 1
# >> 4

num *=2
# >> 8

num /= 4
# >> 2.0

#길이(length) 함수
snack = '꿀꽈배기'
print(len(snack))
# >>4

# 여러 줄 문자열이 필요할 경우
# ex)꿀꽈배기
# 너무
# 맛있어요

snack = '''꿀꽈배기
너무
맛있어요'''
# 처럼 문자 앞뒤로 따옴표(') 3개 감싸서 변수 선언 가능


# _commit -m 정정_2
