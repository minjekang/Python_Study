import pickle

# pro_file = open("profile.pickle", "wb")
# profile = {"이름":"강민제", "나이":30, "취미":["축구", "요리", "배드민턴"]}
# print(profile)
# pickle.dump(profile, pro_file)
# pro_file.close()

# pro_file = open("profile.pickle", "rb")
# profile = pickle.load(pro_file)  # file에 있는 정보 profile에 불러오기
# print(profile)
# pro_file.close()


# with
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬 공부중")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())