# 1. 홀짝 판별기

i = input("정수를 입력하시오 > ")
k = int(i) % 2
if (k == 0):
    print("짝수입니다.")
else:
    print("홀수입니다.")

#2. 별 피라미드 출력 프로그램

i = int(input("숫자를 입력하세요: "))

for n in range(1, i +1):
    print("*" * n)

#3. 업 다운 게임 만들기

import random

answer = int(random.randint(1, 10))

print(answer)
for i in range(3):
    n = int(input("숫자를 입력하세요 > "))

    if n < answer:
        print("UP!")
    elif n > answer:
        print("DOWN!")
    else:
        print("정답입니다.")
        break

print("정답은 " + str(answer) + "입니다.")