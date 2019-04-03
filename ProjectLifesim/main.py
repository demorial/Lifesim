import PersonClass
import random
import time
import CountryClass
import sys
# country = ["Amreica", "France", "Australia", "Switzerland", "China", "Scotland",
#           "Portugal", "South Africa", "Argentina", "Mexico", "Nigeria", "India", ]

countryList = []
countryList.append(CountryClass.Country("Amreica", 9))
countryList.append(CountryClass.Country("France", 6))
countryList.append(CountryClass.Country("Australia", 4))
countryList.append(CountryClass.Country("Switzerland", 4))
countryList.append(CountryClass.Country("China", 3))
countryList.append(CountryClass.Country("Scotland", 1))
countryList.append(CountryClass.Country("Portugal", 7))
countryList.append(CountryClass.Country("South Africa", 3))
countryList.append(CountryClass.Country("Argentina", 2))
countryList.append(CountryClass.Country("Mexico", 5))
countryList.append(CountryClass.Country("Nigeria", 2))
countryList.append(CountryClass.Country("India", 3))

names = ["Jacobus", "Ruan", "Dina", "Michael",
         "Brendan", "Shana", "Dirk", "Werner"]

concieved = ["an affair", "a planned pregnancy",
             "a scandal", "a Lab", "and put up for adoption", "a dumbster"]

age = 0

# sien get_stats() vir jou ou if statement
a = random.randint(0, len(concieved)-1)
b = random.randint(0, 7)
c = random.randint(0, len(countryList)-1)
print("Welcome you were born")
print("Your curcumstance of birth ")
print("Your name is:", names[b])
print("You are born in:", countryList[c].getCountry())
print("age :", age)
print()
if a == 5:
    print("unfortunately your parents did not love you enough and left you to die")
    print()
    sys.exit("game over")

else:
    print("your stats at birth are:")
    # playerX is die class so as jy nog functions onder die class maak kan j dit call met
    # playerX.Function()
    playerX = PersonClass.Person(names[b], age, countryList[c], concieved[a])
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
print("=================================")
print("health: ", playerX.health)
print("intelligence: ", playerX.intelligence)
print("Looks: ", playerX.looks)
print("happiness: ", playerX.happiness)


def checkpath(path):
    print("")
