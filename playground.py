import json
import random
import time
import os

with open("D&D.json", "r") as f:
    data =json.load(f)

clear = lambda: os.system('cls')

randIDRace = random.randint(0,4)

randIDClass = random.randint(0,9)

raceName = data['race'][randIDRace]['name']

className = data['class'][randIDClass]['name']

stat1 = random.randint(7,20)
stat2 = random.randint(7,20)
stat3 = random.randint(7,20)
stat4 = random.randint(7,20)
stat5 = random.randint(7,20)
stat6 = random.randint(7,20)

print(f"Race: {raceName} \nClass: {className}")

for x in range (0,5):  
    b = "Rolling stats" + "." * x
    print (b, end="\r")
    time.sleep(1)
print(f"\nStat 1: {stat1}")
print(f"Stat 2: {stat2}")
print(f"Stat 3: {stat3}")
print(f"Stat 4: {stat4}")
print(f"Stat 5: {stat5}")
print(f"Stat 6: {stat6}")
print("Input stats")
strength = input("Strength: ")
dexterity = input("Dexterity: ")
constitution = input("Constitution: ")
intelligence = input("Intelligence: ")
wisdom = input("Wisdom: ")
charisma = input("Charisma: ")
name = input("Good job! Now give your character a name:\n")
for x in range (0,5):  
    b = "Thank you! Generating character sheet" + "." * x
    print (b, end="\r")
    time.sleep(1)
clear()

print("\nCharacter Sheet")
print(f"Name: {name}")
print(f"Race: {raceName}")
print(f"Class: {className}")
print(f"Strength: {strength}")
print(f"Dexterity: {dexterity}")
print(f"Constitution: {constitution}")
print(f"Intelligence: {intelligence}")
print(f"Wisdom: {wisdom}")
print(f"Charisma: {charisma}")
