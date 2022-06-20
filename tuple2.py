# 튜플2

# 소괄호를 쓰고 ,로 구분된 값들을 넣는 방법으로 튜플 선언 가능
my_tuple = ('오예스','몽쉘','초코파이')
# 이러한 작업을 '패킹' 이라고 함

# 그러나 파이썬에서는 이것과 반대로
(pie1,pie2,pie3) = my_tuple
# my_tuple을 pie1, pie2, pie3 변수에 각각 저장
# 이것을 '언패킹'이라고 함
# pie1='오예스'
# pie2='몽쉘'
# pie3='초코파이'

# 언패킹에는 *을 이용할 수 있는데
# ex)
numbers = (1,2,3,4,5,6,7,8,9,10)
(one,two,*others) = numbers
# numbers의 개수와 변수의 개수가 안 맞음!?
# 하지만 *을 입력함으로써 numbers 중 첫 번째 값은 one 변수, 두 번째 값은 two 변수에 넣고
# 나머지는 모두 others에 들어가게 됨
# others는 여러 개의 값을 가지게 되지만 튜플이 아닌 !리스트 형태!로 됨

# 필요에 따라 별의 위치 변경 가능
(*others,nine,ten) = numbers
# nine에는 9, ten에는 10 들어가고, 나머지는 others에 들어감

(*others,nine,ten) = numbers