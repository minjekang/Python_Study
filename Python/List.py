# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
#subway1 = 10
#subway2 = 20
#subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "나", "너"]
print(subway)

# 몇 번째?
print(subway.index("나"))

# 추가
subway.append("형")
print(subway)

# 누나를 나와 유재석 사이에
subway.insert(1, "누나")
print(subway)

# 뒤에서 부터 삭제
print(subway.pop())
print(subway)

#print(subway.pop())
#print(subway)

#print(subway.pop())
#print(subway)


# 같은거 몇개
subway.append("나")
print(subway)
print(subway.count("나"))


# 정렬
num = [5,3,2,4,1]
num.sort()
print(num)

# 뒤집기
num.reverse()
print(num)


# 모두 삭제
num.clear()
print(num)


# 다양한 자료형
numm = [5,3,2,4,1]
mix = ["나", 20, True]
#print(mix)


# 리스트 확장
numm.extend(mix)
print(numm)