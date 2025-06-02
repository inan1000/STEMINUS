# 짝홀 구분
i = int(input("정수를 입력하시오 > "))
if i % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

# 별 피라'미드'
n = int(input("몇 줄짜리 피라미드를 출력할까요? > "))

for i in range(1, n + 1):
    print("*" * i)

#숫자맞추기 ㅎㅎ
import random

answer = random.randint(1, 10)  #

for attempt in range(3):
    guess = int(input("숫자를 맞혀보세요 (1~10): "))

    if guess == answer:
        print("정답입니다!")
        break
    elif guess > answer:
        print("Down!")
    else:
        print("Up!")
else:
    print(f"아쉽습니다. 정답은 {answer}였습니다.")
