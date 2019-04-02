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
countryList.append(Country("Amreica", 5))
countryList.append(Country("France", 5))
countryList.append(Country("Australia", 5))
countryList.append(Country("Switzerland", 5))
countryList.append(Country("China", 5))
countryList.append(Country("Scotland", 5))
countryList.append(Country("Portugal", 5))
countryList.append(Country("South Africa", 5))
countryList.append(Country("Argentina", 5))
countryList.append(Country("Mexico", 5))
countryList.append(Country("Nigeria", 5))
countryList.append(Country("India", 5))


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

    # weet nie hkm j n ifstatement het vir stats het as jy altyd
    # 0 as die age gan bgn meer nie
    # sou dink j moet n function hier maak wat as age change
    # dan kan jy weer die function run

    def get_stats(self):
        if self.age <= 6:
            self.health = 100
            self.happiness = random.randint(80, 100)
            self.intelligence = random.randint(40, 100)
            self.looks = random.randint(0, 100)

        elif self.age > 6 and self.age <= 9:
            self.health = random.randint(60, 90)
            self.happiness = random.randint(0, 80)
            self.intelligence = random.randint(10, 100)
            self.looks = random.randint(0, 100)

        elif self.age > 10:
            self.health = random.randint(5, 50)
            self.happiness = random.randint(0, 70)
            self.intelligence = random.randint(10, 100)
            self.looks = random.randint(0, 100)

    def SaveGame(self):
        # hier kan jy print nae n txt file met die values
        pass  # delete die pass as hierdie iets in het


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
        path = input("which path will you take? (1 or 2)")

    return path


def checkpath(path):
    print("")
