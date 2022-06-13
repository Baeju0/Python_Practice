# 문자열 포맷

python = '파이썬'
java = '자바'

# 둘 다 출력
print(python + ' ' + java)
# >> 파이썬 자바

# ,사용하면 자동 띄어쓰기
print(python, java)
# >> 파이썬 자바

# 다른 문장 속에 포함시키기?
# ex) '개발 언어에는 파이썬, 자바 등이 있습니다'
print('개발 언어에는 '+python+','+java+'등이 있습니다')
# 또는
print('개발 언어에는',python,',',java,'등이 있습니다')
# >> 개발 언어에는 파이썬,자바등이 있습니다

# + , '' 등 복잡해보임 => 문자열 포맷 이용!

# 1. {}+format
print('개발 언어에는 {},{}등이 있습니다'.format(python,java))
# >> 개발 언어에는 python,java등이 있습니다
# 중괄호를 써놓고 괄호에 출력하는 값을 입력, 입력한 순서대로 출력


# 2. {N}+format     N : 0,1,2,3…
print('개발 언어에는 {0},{1}등이 있습니다'.format(python,java))
# >> 개발 언어에는 python,java등이 있습니다
# format 속에 있는 값들이 중괄호 0, 중괄호1의 위치에 출력

# 1번 방식과 2번 방식의 차이점
# 중괄호 안의 순서를 숫자를 통해 정해줄 수 있음
# 2번 방식 ex)
print('개발 언어에는 {1},{0}등이 있습니다'.format(python,java))
# >> 개발 언어에는 java,python 등이 있습니다


# 3. f-string(python3.6↑)
print(f'개발 언어에는 {python},{java}등이 있습니다')
# >> 개발 언어에는 python,java등이 있습니다
# 문자열 내에서 중괄호 입력하고, 출력하고자 하는 변수의 값을 바로 정의할 수 있음
