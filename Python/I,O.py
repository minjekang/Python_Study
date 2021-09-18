# # 빈자리는 빈, 오른쪽 정렬, 10자리 공간 확보
# print("{0: >10}".format(500))

# # 양수일땐 +, 음수일땐 -
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))

# # 왼쪽 정렬, 빈칸 _로
# print("{0:_<+10}".format(500))

# # 세 자리마다 ,찍기
# print("{0:,}".format(10000000000))

# # 세 자리마다 ,찍기  , + - 부호도 찍기
# print("{0:+,}".format(-10000000000))

# #세 자리마다 ,찍기  , + - 부호도 찍기 , 자릿수 확보 빈자리는 ^
# print("{0:^<+30,}".format(1000000000000))

# # 소수점 
# print("{0:f}".format(5/3))

# # 소수점 자리
# print("{0:.2f}".format(5/3))



# 파일 입출력
# s_file = open("score.txt", "w", encoding="utf8")
# print("수학: 0", file=s_file)
# print("영어: 50", file=s_file)
# s_file.close()


# s_file = open("score.txt", "a", encoding="utf8")
# s_file.write("과학: 80")
# s_file.write("\n코딩: 100")
# s_file.close()

# s_file = open("score.txt", "r", encoding="utf8")
# print(s_file.read())
# s_file.close()

# s_file = open("score.txt", "r", encoding="utf8")
# print(s_file.readline())  # 줄별로 읽기, 한 줄 읽고 커서 아래로
# print(s_file.readline()) 
# print(s_file.readline(), end="") 
# print(s_file.readline(), end="") 
# s_file.close()


# s_file = open("score.txt", "r", encoding="utf8")
# while True:
#     list = s_file.readline()
#     if not line:
#         break
#     print(line)
# s_file.close()

s_file = open("score.txt", "r", encoding="utf8")
lines = s_file.readlines() 
for line in lines:
    print(line, end="")
s_file.close()