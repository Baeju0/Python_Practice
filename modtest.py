# 대화형 인터프리터와 달리 파이썬 파일에서 이전에 만들어 놓은 모듈 불러오기

import mod2
result = mod2.add(3, 4)
print(result)

# 정상적으로 실행되기 위해서는 modtest.py 파일과 mod2.py 파일이 동일한 경로에 있어야 됨

# 모듈을 저장한 경로로 이동하지 않고 모듈 불러와서 사용하기
# 경로에서 mkdir mymod (mymod 폴더 생성)
# move mod2.py mymod (mymod 폴더로 mod2.py 파일 이동)

# 1.sys.path.append(모듈을 저장한 디렉터리) 사용하기
# 경로에 python들어가서 import sys
# sys.path (파이썬 라이브러리가 설치되어 있는 디렉터리 보여주기)
# sys.path.append("C:/~~/mymod") 추가해주기

# 다시 sys.path를 통해 보면 mymod가 추가되어 있다!

# 실제 모듈을 불러와서 사용할 수 있는지 테스트
# import mod2
# print(mod2.add(3,4))
# >> 7

# ? 다시 시도하기