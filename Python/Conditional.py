############ if ###################

# weather = input("오늘 날씨는 어때요?")
# if weather == "비" or "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")


# temp = int(input("기온이 어때요?"))
# if 30 <= temp:
#     print("너무 더움")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨")
# elif 0 <= temp and temp < 10:
#     print("약간 추움")
# else:
#     print("너무 추움")

############ if ###################


############ for ###################

# print("대기번호: 1")
# print("대기번호: 2")
# print("대기번호: 3")
# print("대기번호: 4")

# for waiting_n in range(1, 6):
#     print("대기번호: {0}".format(waiting_n))

# starbucks = ["아이언맨", "토르", "그루트"]
# for customer in starbucks:
#     print("{0}님, 커피가 준비 되었습니다".format(customer))


############ for ###################


############ while ###################

# customer = "아이언맨"
# # index = 5
# # while index >=1:
# #     print("{0}, 커피 나왔습니다. {1}번 남았어요".format(customer, index))
# #     index -= 1
# #     if index == 0 :
# #         print("커피 폐기처분")
# index = 1
# while true:
#     print("{0}, 커피 나왔습니다. 호출 {1} 회".format(customer, index))
#     index += 1


# customer = "토르"
# person = "Unknown"

# while person != customer:
#     print("{0}, 커피 준비 완료.".format(customer))
#     person = input("이름이 뭔가요?")

############ while ###################




# absent = [2, 5] # 결석
# no_book = [7] # 책 없음
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0} 은 교무실로".format(student))
#         break
#     print("{0}, 책 읽어봐".format(student))



# 한줄 for#######################3
# student = [1, 2, 3, 4, 5]
# print(student)
# student = [i+100 for i in student]
# print(student)

# 이름 길이로 변환
student = ["Iron man", "Thor", "Groot"]
student = [len(i) for i in student]
print(student)

# 대문자로
student = ["Iron man", "Thor", "Groot"]
student = [i.upper() for i in student]
print(student)