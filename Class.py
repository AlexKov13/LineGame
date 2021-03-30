"""class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometr = 0

    def description_name(self):
        desc = str(self.year) + ' ' + self.make + ' ' + self.model
        return  desc.title()

    def read_odometr(self):
        print("--- "+str(self.odometr)+" km")

    def update_odometr(self, km):
        if km >= self.odometr:
            self.odometr = km
        else:
            print("Eror")

myCar = Car('audi', 'a4', 2019)
print(myCar.description_name())
myCar.update_odometr(11)
myCar.update_odometr(1)
myCar.read_odometr()"""

class Player():
    def __init__(self, hp, strong, defence, speed):
        self.hp = hp
        self.strong = strong
        self.defence = defence
        self.speed = speed

    def view_stats(self):
        print("HP --- "+str(self.hp))
        print("Strong - "+str(self.strong))
        print("Defence - "+str(self.defence))
        print("Speed - "+str(self.speed))

    def increment_hp(self, hp):
        self.hp += hp
        print("HP --- "+str(self.hp))

    def decrement_hp(self, hp):
        self.hp -= hp
        if self.hp < 0:
            self.player_death()
        else:
            print("HP --- "+str(self.hp))
            print("SASI 4LEN")

    def update_strong(self, strong):
        self.strong += strong
        print("Strong - "+str(self.strong))

    def update_defence(self, defence):
        self.defence += defence
        print("Defence - "+str(self.defence))

    def update_speed(self, speed):
        self.speed += speed
        print("Speed - "+str(self.speed))

    def player_death(self):
        print("Sorry, but you death!")

class Warrior(Player):
    def __init__(self, hp, strong, defence, speed, attack):
        super().__init__(hp, strong, defence, speed)
        self.attack = attack

    def sword_attack(self):
        print("-"+str(self.attack)+" hp")

    def view_stats(self):
        print("HP --- " + str(self.hp))
        print("Strong - " + str(self.strong))
        print("Defence - " + str(self.defence))
        print("Speed - " + str(self.speed))
        print("Attack - "+str(self.attack))

class Wizard(Player):
    def __init__(self, hp, strong, defence, speed, magical):
        super().__init__(hp, strong, defence, speed)
        self.magical = magical

    def magical_attack(self):
        print("-"+str(self.magical)+" hp")

    def view_stats_wizard(self):
        self.view_stats()
        print("Magic - "+str(self.magical))

PlayerWarrior = Warrior(100, 75, 80, 70, 55)
PlayerWarrior.sword_attack()
PlayerWarrior.view_stats()
PlayerWizard = Wizard(100, 40, 50 , 90, 125)
PlayerWizard.magical_attack()
PlayerWizard.view_stats_wizard()

#Player1 = Player(100, 56, 39, 88)
#Player1.view_stats()
#Player1.decrement_hp(15)
#Player1.increment_hp(35)
#Player1.update_speed(12)
#Player1.update_strong(21)
#Player1.update_defence(23)
#Player1.decrement_hp(200)


