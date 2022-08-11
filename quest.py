# Q. 코드 결괏값?
a = "Life is too short, you need python"

if "wife" in a: print("wife") # "wife"라는 단어가 있다면 출력
elif "python" in a and "you" not in a: print("python") # "python"과 "you"라는 단어가 포함되지 않았다면 출력
elif "shirt" not in a: print("shirt") # "shirt"라는 단어가 포함되지 않았다면 출력 o
elif "need" in a: print("need")
else: print("none")
# >> shirt


# Q. while문 사용해 1부터 1000까지의 자연수 중 3의 배수의 합 구하기
n = 0
i = 1
while i <= 1000:
    # print(n)
    # n = n + n
    if i % 3 == 0 :
        n += i
    i += 1
print(n)


# Q. while문 사용해 아래와 같이 *표시하는 프로그램 작성
# *
# **
# ***
# ****
# *****
s = '*'
nu = 1
while nu <= 5 :
    print(s*nu)
    nu += 1


# Q. for문 사용해 1부터 100까지 숫자 출력
for i in range(1,101):
    print(f'{i}')


# Q. 총 10명의 학생, for문 사용해 학급의 평균 점수 구하기
#   [70,60,55,75,95,90,80,80,85,100]
score = [70,60,55,75,95,90,80,80,85,100]
p1 = 0

for p in score :
    p1 += p
aver = p1/10
print(aver)


# Q. 아래 내용은 리스트 중에 홀수에만 2를 곱해 저장하는 코드
numbers = [1,2,3,4,5]
result1 = []
for n in numbers:
    if n % 2 == 1:
        result1.append(n*2)
# >> [2,6,10]

# 위 코드를 리스트 내포를 사용하여 표현하기
# 리스트 내포 [표현식 for 항목 in 반복가능객체 if 조건문]
numbers = [1,2,3,4,5]
result1 = [n * 2 for n in numbers if n % 2 == 1]
print(result1)