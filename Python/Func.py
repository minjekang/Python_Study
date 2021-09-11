# ------------String Funcion------------

python = "Python is Amazing"

print(python.lower()) #소문자
print(python.upper()) #대문자
print(python.isupper()) 
print(len(python)) #길이 
print(python.replace("Python", "Java")) 


index = python.index("n") #"n"이 몇번째에 있는지
print(index)
index = python.index("n", index + 1) #두번째 n
print(index)


print(python.find("n"))
print(python.find("Java")) 
print(python.find("Java")) 
# find = "Java"가 없으면 -1반환
# index = "Java"가 없으면 프로그램 종료

print(python.count("n")) #"n"이 몇 번 나왔는지