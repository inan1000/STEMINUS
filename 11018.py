#  별 피라미드 출력 프로그램
# 사용자로부터 입력받은 숫자만큼의 *로된 피라미드 만들기
# 힌트 : input(), int(), for
# ex)숫자를 입력하세요: 5
print("별 피라미드출력 프로그램")
a = input("숫자입력 하세요:")
a = int(a)
a = a+1
for star in range(1,a):
    print("*" *(star))