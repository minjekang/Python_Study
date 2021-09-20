# # 마린 : 공격유닛, 군인, 총

# name = "마린"
# hp = 40
# damage = 5

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크 : 공격유닛, 탱크, 대포, 일반/시즈 모드

# t_name = "탱크"
# t_hp = 150
# t_damage = 35

# print("{} 유닛이 생성되었습니다.".format(t_name))
# print("체력 {0}, 공격력 {1}\n".format(t_hp, t_damage))

# t2_name = "탱크"
# t2_hp = 150
# t2_damage = 35

# print("{} 유닛이 생성되었습니다.".format(t2_name))
# print("체력 {0}, 공격력 {1}\n".format(t2_hp, t2_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

# attack(name, "1시", damage)
# attack(t_name, "1시", t_damage)
# attack(t2_name, "1시", t2_damage)


class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)