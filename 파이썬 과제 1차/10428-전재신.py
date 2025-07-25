#1. 홀짝 수 판별기 

number1= int (input("숫자를 입력하세요"))
if number1 % 2 == 0:
    print("이 숫자는 짝수입니다!!")
else:
    print("이 숫자는 홀수네요!!")

#2. 별 피라미드 출력 프로그램

number2 = int(input("숫자를 입력하세요"))
for number3 in range(1, number2 + 1):
    print("*" * number3)

#3. 업 다운 게임

import random
answer = random.randint(1, 10)
for opportunity in range(1, 4):
    response = int(input("숫자를 입력하세요"))

    if response == answer:
        print("ㅎㅎ정답입니당")
        break
    elif answer > response:
        print("Up! 더 큰 숫자!!")

    else:
        print("Down! 더 작은 숫자로!!")
else:
    print(f"아쉬워요 정답은 {answer}였습니다ㅜ")
   
    #print 안에 f 넣는거랑 break랑 들여쓰기,for opportunity in range(1, 4):
    # 이런것들은 지피티의 도움을 약간 받았습니다