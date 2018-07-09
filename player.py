import random as rd

class Player:

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.experience = 0
        self.hp = 100
        self.remaining_hp = 100
        self.strength = 10
        self.luck = 1
        self.weapon_power = 0
        self.potions = 10

    def printSelf(self):
        print("Name     : {0:>10}".format(self.name))
        print("Hp       : {0:>10}".format(str(self.remaining_hp) + "/" + str(self.hp)))
        print("Strength : {0:10d}".format(self.strength))
        print("Weapon   : {0:10d}".format(self.weapon_power))
        print("Potions  : {0:10d}".format(self.potions))
        print("Luck     : {0:10d}".format(self.luck))


    def attack(self, m):
        m.hp -= self.strength + self.weapon_power

    def drink_potion(self, num):
        if self.potions >= num:
            self.potions -= num
            self.remaining_hp += num * 20
            if self.remaining_hp > self.hp:
                self.remaining_hp = self.hp
            return True
        else:
            return False

    def get_experience(self, m):
        diff = (self.hp + self.strength + self.weapon_power) - (m.hp + m.power)
        diff_to_add = abs(int(rd.gauss(0, diff)))
        if diff > 0:
            exp = (25 - diff_to_add)
        elif diff < 0:
            exp = (25 - diff_to_add)
        else:
            exp = 25
        if exp < 10:
            exp = 10
        elif exp > 50:
            exp = 50
        self.experience += exp
        print("You've got ", exp, " experience! New experience points: ", self.experience)
        while self.experience >= 100:
            self.experience -= 100
            self.increase_level()

    def increase_level(self):
        self.hp += 100
        self.remaining_hp = self.hp
        self.strength += 10
        self.luck += 1
        self.level += 1
        print("Your level increased to ", self.level)
        while True:
            i = input("Which do you want to increase more? Hp(1) Strength(2) Luck(3): ")
            if i == 1:
                abs(int(rd.gauss(0, 50)))
                break
            elif i == 2:
                abs(int(rd.gauss(0, 5)))
                break
            elif i == 3:
                self.luck += 1
                break

        print("Congratulations!!!")
        self.printSelf()
