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


# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# 레이스 : 공중유닛, 비행기, 클로킹(상대에게 안보임)
# wraith = Unit("레이스", 80, 5)
# print("유닛 이름: {0}, 공격력: {1}".format(wraith.name, wraith.damage))

# # 마인드 컨트롤 : 상대 유닛을 내 것으로 만드는 것

# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))
# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage


    def attack(self,location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 메딕 : 의무병

# 파이어뱃 : 공격유닛, 화염방사기
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# 공격을 2번 받음
# firebat1.damaged(25)
# firebat1.damaged(25)

# 드랍쉽 : 공중유닛, 수송기. 마린 / 파이어뱃 등을 수송, 공격 X

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_spd):
        self.flying_spd = flying_spd

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_spd))
        
        

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_spd):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피드 : 0
        Flyable.__init__(self, flying_spd)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass


# 서프라이 디폿 : 건물, 1개 = 8유닛.
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()


# # 발키리 : 공중 공격 유닛, 한 번에 14발 미사일 발사
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# # 벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# # 배틀크루져 : 공중 유닛, 체력,공격력 좋음
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# #battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")