# 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print (5+3)
print(2*8)
print(3*(3+1))


# 문자열
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)


# 참 / 거짓
print(5>10)
print(5<10)
print(True)
print(False)
print(not True)
print(not False)
print(not(5 > 10))



# 변수 
# 애완동물 소개
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_abult = age >= 3

print("우리집 강아지 이름은 연탄이")
print("연탄이는 4살, 산책을 좋아함.")
print("연탄이는 어른일까? True")

print("우리집 " + animal +" 이름은 "+name)
print(name+"는 "+str(age)+"살, "+hobby+"을 좋아함.")
print(name+"는 어른일까? "+str(is_abult)+"")

# '+' = ','
# ',' 쓸때는 str 필요없음
# ',' 쓰면 띄어쓰기 1칸


# 연산자
print(1+1)
print(3-2)
print(5*2)
print(10/2)

print(2**3)
print(5%3)
print(10%3)
print(5//3)
print(10//3)

print(10 > 3) #True
print(4 >= 7) #False
print(10 < 3)
print (5 <= 5) #True

print(3 == 3)


print(1 != 3)

print((3>0) and (3<5))
print((3>0) & (3<5))


print((3>0) or (3<5))
print((3>0) | (3<5))

print(2 + 3 * 4)
print((2+3)*4)



# 숫자 처리 함수

print(abs(-5)) #절댓값
print(pow(4,2)) #4^2
print(max(5,12))
print(min(5,12)) 
print(round(3.14)) #반올림

from math import *
print(floor(3.14)) #내림 3
print(ceil(3.14)) #올림 4
print(sqrt(16)) #제곱근 4


#String
sentence = '나는 민제'
print(sentence)
sentence2 = "나는 민제"
print(sentence2)
sentence3 = """
나는 민제
"""
print(sentence3)


#Slicing
j = "051023-3234567"

print("성별 : "+j[7])
print("연 : "+j[0:2]) # 0~2번째 전까지
print("월 : "+j[2:4]) # 2~4번째 전까지
print("일 : "+j[4:6]) # 4~6번째 전까지

print("생년월일 : "+j[:6]) #처음부터 6전까지
print("뒤 7자리 : "+j[7:]) #7부터 끝까지
print("뒤 7자리 : "+j[-7:]) #7부터 끝까지
