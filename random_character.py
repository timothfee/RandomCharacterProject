import json
import random
import time
import os

with open("D&D.json", "r") as f:
    data = json.load(f)

rand_id_race = random.randint(0, 4)

rand_id_class = random.randint(0, 11)

race_name = data['race'][rand_id_race]['name']

class_name = data['class'][rand_id_class]['name']

sub_class = data['class'][rand_id_class]['sub-class']

subclass_len = len(sub_class) - 1


rand_id_subclass = random.randint(0, subclass_len)

subclass_name = data['class'][rand_id_class]['sub-class'][rand_id_subclass]

stat1 = random.randint(7, 20)
stat2 = random.randint(7, 20)
stat3 = random.randint(7, 20)
stat4 = random.randint(7, 20)
stat5 = random.randint(7, 20)
stat6 = random.randint(7, 20)

stats = [stat1, stat2, stat3, stat4, stat5, stat6]

print(f"Race: {race_name} \nClass: {class_name}\nSub-Class: {subclass_name}")

for x in range(0, 5):
    b = "Rolling stats" + "." * x
    print(b, end="\r")
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
for x in range(0, 5):
    b = "Thank you! Generating character sheet" + "." * x
    print(b, end="\r")
    time.sleep(1)

print("\nCharacter Sheet")
print(f"Name:           {name}")
print(f"Race:           {race_name}")
print(f"Class:          {class_name}")
print(f"Strength:       {strength}")
print(f"Dexterity:      {dexterity}")
print(f"Constitution:   {constitution}")
print(f"Intelligence:   {intelligence}")
print(f"Wisdom:         {wisdom}")
print(f"Charisma:       {charisma}")

'''
A few things I would like to add:
- Random spells if the class chosen is a spell caster
- Adding the stats to a list and having the user choose from that list so they can't just put whatever stat they want.
- Print a PDF with their information on it
'''
