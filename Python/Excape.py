# \n 줄바꿈
print("백문이 불여일견 \n백견이 불여일타")


# /"
# 저는 "강민제"입니다.
# print("저는 "강민제"입니다.")
# print("저는 '강민제'입니다.")
# print('저는 "강민제"입니다.')
print("저는 \"강민제\"입니다.")


# \\ : 문장 내에서는 \
print("PS C:\\Users\\1101강민제\\Desktop\\Python WS\\Python_Study>")


# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")


# \b : 한 글자 삭제
print("Redd\bApple")


# \t : 탭
print("Red\tApple")


#######
url = "http://naver.com"
my = url.replace("http://", "")
my = my[:my.index(".")]
print(my)