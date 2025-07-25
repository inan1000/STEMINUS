# 3. 업 다운 게임 만들기(어려움)
# 프로그램이 1부터 10 사이의 숫자 중 하나를 무작위로 정함.
# 사용자가 숫자를 입력하면, 컴퓨터가 다음과 같은 힌트를 줌:
#     정답보다 크면 "Down!"
#     정답보다 작으면 "Up!"
#     정답이면 "정답입니다!" if쓰기
# 사용자는 총 3번의 기회를 가짐. for문 3번반복복
# 정답을 맞히면 즉시 종료, 3번 모두 틀리면 정답 공개 후 종료. 
# 힌트 : input(), int(), for, if, random.randint()
# ex) 숫자를 입력하세요 : 7
#     "DOWN!"
#     숫자를 입력하세요 : 5
#     "UP!"
#     숫자를 입력하세요 : 6
#     "정답입니다!"
from random import*
print("업다운 게임 시작!")
number = int(randint(1,10))
for i in range(3):
    game = int(input("숫자를 입력하세요 :"))
    if game >= number:
        print("DOWN!")
    elif game <= number:
        print("UP!")
    elif game == number:
        break
else:
    print("아쉽네요 정답은 {0} 입니다!".format(str(number)))
#선배님 참고로 gpt어느정도 이용했습니다! break,3번 반복하게하는법법