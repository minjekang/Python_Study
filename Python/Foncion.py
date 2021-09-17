# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# #open_account()

# def deposit(blance, money):
#     print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(blance+money))
#     return blance + money

# def withdraw(blance, money):
#     if blance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(blance - money))
#         return blance - money
#     else:
#         print("출금이 완료되지 않았습니다.잔액은 {0}원 입니다.".format(blance))
#         return blance

# def withdraw_n(blance, money):
#     commission = 100
#     return commission, blance - money - commission

# blance = 0
# blance = deposit(blance, 1000)
# # blance = withdraw(blance, 2000)
# # blance = withdraw(blance, 500)
# commission, blance = withdraw_n(blance, 500)
# print("수수료는 {0} 원이며, 잔액은 {1}원입니다.".format(commission, blance))


# 기본값
# def profile(name, age, mainlang):
#     print("이름: {0}\t나이: {1}\t주 사용 언어: {2}"\
#         .format(name, age, mainlang))


# profile("강민제", 17, "Python")
# profile("유시온", 17, "Java")


# 같은 학교, 반, , 학년, 수업.
# def profile(name, age=17, mainlang="Python"):
#     print("이름: {0}\t나이: {1}\t주 사용 언어: {2}"\
#         .format(name, age, mainlang))


# profile("강민제")
# profile("유시온")


# 키워드값
# def profile(name, age, mainlang):
#     print(name, age, mainlang)

# profile(name="강민제", mainlang="Python", age=17)
# profile(mainlang="Java",age=17, name="유시온" )


# 가변 인자
# def profile(name, age, la1, la2, la3, la4, la5):
#     print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")
#     print(la1, la2, la3, la4, la5)

# def profile(name, age, *la):
#     print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")
#     for lang in la:
#         print("{0} ".format(lang), end="")
#     print()

# profile("강민제", 17, "Python", "Java", "c", "c++", "JS", "C#")
# profile("유시온", 17, "Kotlin", "Swift", "", "", "")


# 지역 / 전역 변수
# gun = 10

# def che(sold):
#     global gun
#     gun = gun-sold
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def che_ret(gun, sold):
#     gun -= sold
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총: {0}".format(gun))
# #che(2)
# gun = che_ret(gun, 2)
# print("전체 총: {0}".format(gun))
