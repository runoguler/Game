

class Monster:

    def __init__(self, hp, power):
        self.hp = hp
        self.remaining_hp = hp
        self.power = power


    def printSelf(self):
        print("Hp    : {0:>10}".format(str(self.remaining_hp) + "/" + str(self.hp)))
        print("Power : {0:10d}".format(self.power))

    def attack(self, p):
        p.remaining_hp -= self.power
