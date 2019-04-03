import time
import random
# import numpy as np


class Country:
    # doen met die wat j wil net gedink as j
    # difficulty will change gebaseer op country
    def __init__(self, country, saftyRank):
        self.country = country
        self.saftyRank = saftyRank

    def getCountry(self):
        return self.country

    def getSaftyRank(self):
        return self.saftyRank
# country = ["Amreica", "France", "Australia", "Switzerland", "China", "Scotland",
#           "Portugal", "South Africa", "Argentina", "Mexico", "Nigeria", "India", ]


countryList = []
countryList.append(Country("Amreica", 9))
countryList.append(Country("France", 6))
countryList.append(Country("Australia", 4))
countryList.append(Country("Switzerland", 4))
countryList.append(Country("China", 3))
countryList.append(Country("Scotland", 1))
countryList.append(Country("Portugal", 7))
countryList.append(Country("South Africa", 3))
countryList.append(Country("Argentina", 2))
countryList.append(Country("Mexico", 5))
countryList.append(Country("Nigeria", 2))
countryList.append(Country("India", 3))


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
        #  die country in die array is
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


names = ["Jacobus", "Ruan", "Dina", "Michael",
         "Brendan", "Shana", "Dirk", "Werner"]

concieved = ["an affair", "a planned pregnancy",
             "a scandal", "a Lab", "and put up for adoption", "a cardboard box"]

age = 0

# sien get_stats() vir jou ou if statement
a = random.randint(0, len(concieved)-1)
b = random.randint(0, 7)
c = random.randint(0, len(countryList)-1)
print("Welcome you were born in ", concieved[a])
print("Your name is:", names[b])
print("You are born in:", countryList[c].getCountry())
print("age :", age)
print()
if a == 5:
    print("unfortunately your parents did not love you enough and left you to die")
    print()
    print("game over")
    pass
else:
    print("your stats at birth are:")
    # playerX is die class so as jy nog functions onder die class maak kan j dit call met
    # playerX.Function()
    playerX = Person(names[b], age, countryList[c], concieved[a])
    playerX.get_stats()
    print("health: ", playerX.health)
    print("intelligence: ", playerX.intelligence)
    print("Looks: ", playerX.looks)
    print("happiness: ", playerX.happiness)


def path():

    path = ""
    while path != "1" and path != "2":
        path = input("which path will you take 1 or 2: ")

    return path


pathValue = path()
playerX.Firstpath(pathValue)
print("health: ", playerX.health)
print("intelligence: ", playerX.intelligence)
print("Looks: ", playerX.looks)
print("happiness: ", playerX.happiness)


def checkpath(path):
    print("")
