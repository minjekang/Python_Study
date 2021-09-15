# 집합 (set)
# 중복 안됨, 순서 없음

my_set = {1,2,3,3,3}
print(my_set)

java = {"강민제", "나", "너"}
python = set(["강민제", "유시온"])


# 교집합 (java와 python 모두 가능)
print(java & python)
print(java.intersection(python))

# 합집합 (java도 할 수 있거나 python 을 할수있는)
print(java | python)
print(java.union(python))

#  차집합 (java는 할 수 있거나 python 은 못하는)
print(java - python)
print(java.difference(python))

# python 추가
python.add("박명균")
print(python)

# java 삭제
java.remove("강민제")
print(java)