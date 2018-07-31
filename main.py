import random as rd

from player import Player
from monster import Monster


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def monster_fight(p):
    print("You encountered a Monster!")
    m = Monster(abs(int(rd.gauss(p.level * 100, p.level * 100 / 2))),
                abs(int(rd.gauss(p.level * 10, p.level * 10 / 2))))
    m.printSelf()
    win = -1
    while True:
        print()
        i = input("Your move! Attack(1), Drink Potions(2), Try to Run(3), Check Stats(4): ")
        if is_int(i):
            i = int(i)
        else:
            continue
        if i == 1:
            last_hp = m.remaining_hp
            p.attack(m)
            print("You attacked! Monster's hp fell from ", last_hp, " to ", m.remaining_hp)
        elif i == 2:
            t = False
            j = 0
            while not t:
                print("You have ", p.potions, " potions.")
                if p.potions == 0:
                    break
                j = input("How many do you want to drink (20hp per 1): ")
                if is_int(j):
                    j = int(j)
                    t = p.drink_potion(j)
            if j == 0:
                continue
            print("You drank ", j, " potions! Your new hp is ", p.remaining_hp)
        elif i == 3:
            dev = p.luck - p.level
            if dev < abs(int(rd.gauss(0, dev))):
                print("You were able to run away!")
                break
            else:
                print("You failed to run away!")
        elif i == 4:
            p.printSelf()
            continue
        else:
            continue

        if (m.remaining_hp <= 0):
            win = 1
            break

        last_hp = p.remaining_hp
        m.attack(p)
        print("The monster attacked you! Your hp fell from ", last_hp, " to ", p.remaining_hp)

        if (p.remaining_hp <= 0):
            win = 0
            break

    if win == 1:
        p.get_experience(m)
        del m
    elif win == 0:
        print("You Lost! The game is over!")
        exit()


def find_potion(p):
    pots = abs(int(rd.gauss(0, p.level + p.luck + 1)))
    total_pots = p.potions + pots
    if pots == 0:
        print("Found a potion, but it was empty...")
    else:
        print("Found a potion! Number of Potions increased from ", p.potions, " to ", total_pots)
        p.potions = total_pots


def find_weapon(p):
    w = abs(int(rd.gauss(p.weapon_power, (p.level - p.luck + 1))))
    if p.weapon_power < w:
        print("Found a weapon! Weapon power increased from ", p.weapon_power, " to ", w)
        p.weapon_power = w
    else:
        print("Found a weapon! Unfortunately, it was worse than you already have...")


def main():
    p = Player("Runo")
    p.printSelf()

    # main loop
    while True:
        input("Press Enter to continue...")
        r = rd.randint(1, 3)
        if r == 1:
            monster_fight(p)
        elif r == 2:
            find_potion(p)
        elif r == 3:
            find_weapon(p)


if __name__ == '__main__': main()
