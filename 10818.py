# 1. 홀짝 판별기기

i = input("정수를 입력하시오 > ")
k = int(i) % 2
if (k == 0):
    print("짝수입니다.")
else:
    print("홀수입니다.")

#2. 별 피라미드 출력 프로그램

i = int(input("숫자를 입력하세요: "))

i = i + 1

for i in range(1, i):
    print("*" * i)

