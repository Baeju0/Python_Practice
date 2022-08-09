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

result = 0
i = 1
while i <= 1000:
    if i % 3 == 0: # 3으로 나누어 떨어지는 수는 3의 배수
        result += i
    i += 1
print(result)

# Q. while문 사용해 아래와 같이 *표시하는 프로그램 작성
# *
# **
# ***
# ****
# *****


# Q. for문 사용해 1부터 100까지 숫자 출력