#cabinet = {3:"강민제", 100:"유시온"}
#print(cabinet[3])
#print(cabinet[100])

#print(cabinet.get(3))
#print(cabinet.get(5))
#print(cabinet.get(5, "사용가능"))
#print("hi")

# 대괄호로 없는값을 부르면 프로그램 종료
# .get 소괄호로 없는값 -> None 후 계속 실행 뒤에 값 주기 가능


#print(3 in cabinet)  #True
#print(5 in cabinet)  #False


cabinet = {"a-3":"강민제", "b-100":"유시온"}

print(cabinet["a-3"])
print(cabinet["b-100"])


# 추가
# 값 업데이트
print(cabinet)
cabinet["a-3"] = "나"
cabinet["c-20"] = "곽희상"

# 삭제
del cabinet["a-3"]
print(cabinet)


# key 들만 출력
print(cabinet.keys())


# value 들만 출력
print(cabinet.values())


# key,value 모두 출력
print(cabinet.items())


# 모두 삭제
cabinet.clear()
print(cabinet)