import random
import time


class Stats:
    def __init__(self, looks, health, happiness, intelligence):
        self.looks = looks
        self.health = health
        self.happiness = happiness
        self.intelligence = intelligence


class Person(Stats):
    def __init__(self, name, age, country, concieved, looks=0, health=0, happiness=0, intelligence=0):

        self.name = name
        self.age = age
        self.country = country
        self.concieved = concieved
        Stats.__init__(self, looks, health, happiness, intelligence)

    def get_stats(self):
        # ok so die was entlik n maklike fix al wat
        # ons moes doen is die country call en dan sy safety rank
        # self.country.saftyRank want as ons die object maak
        # eg playerX = Person(names[b], age, countryList[c], concieved[a])
        # gee ons vir hom country[c] wat n object van country is soos
        # Country("Nigeria", 2)/country(countryName,SafetyRank)
        # so ons gebruik safty rank instede van die orde van waar
        # die country in die array is
        if self.country.saftyRank <= 6:
            self.health = random.randint(5, 50)
            self.happiness = random.randint(0, 70)
            self.intelligence = random.randint(10, 100)
            self.looks = random.randint(0, 100)

        elif self.country.saftyRank > 6 and self.age <= 9:
            self.health = random.randint(60, 90)
            self.happiness = random.randint(0, 80)
            self.intelligence = random.randint(10, 100)
            self.looks = random.randint(0, 100)

        elif self.country.saftyRank > 10:
            self.health = random.randint(60, 90)
            self.happiness = random.randint(80, 100)
            self.intelligence = random.randint(40, 100)
            self.looks = random.randint(0, 100)

    def SaveGame(self):
        # hier kan jy print nae n txt file met die values
        pass  # delete die pass as hierdie iets in het

    def Firstpath(self, path):
        if path == '1':
            print("You age up")
            self.age += 1
            print("new age is : ", self.age)
            time.sleep(1)
            print("your new stats are: ")
            if self.country.saftyRank <= 6:
                self.health = self.health + random.randint(-2, 2)
                self.happiness = self.happiness + random.randint(-2, 2)
                self.intelligence = self.intelligence+random.randint(-2, 2)
                self.looks = self.looks + random.randint(-2, 2)

            elif self.country.saftyRank > 6 and self.age <= 9:
                self.health = self.health + random.randint(-2, 2)
                self.happiness = self.happiness + random.randint(-2, 2)
                self.intelligence = self.intelligence+random.randint(-2, 2)
                self.looks = self.looks+random.randint(-2, 2)

            elif self.country.saftyRank > 10:
                self.health = self.health + random.randint(-2, 2)
                self.happiness = self.happiness + random.randint(-2, 2)
                self.intelligence = self.intelligence+random.randint(-2, 2)
                self.looks = self.looks+random.randint(-2, 2)

        else:
            # ons pass net want as hy die path kies het j gese moet niks
            # change nie so as ons nnu die values print gan dit die sele bly
            pass
