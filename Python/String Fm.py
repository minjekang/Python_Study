# print("a"+"b")
# print("a","b")

# 1

print("나는 %d살입니다." % 20)
print("나는 %s를 좋아해요." % "YSO")
print("Apple 은 %c 로 시작해요" % "A")
# %s
print("나는 %s살입니다." % 20)
print("Apple 은 %s 로 시작해요" % "A")
print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))


# 2

print("나는 {}살입니다" .format(20))
print("나는 {}색과 {}색을 좋아해요" .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요" .format("파란", "빨간"))


# 3

print("나는 {age}살이며, {color}색을 좋아해요" .format(age = 20, color = "빨간"))


# 4

age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")