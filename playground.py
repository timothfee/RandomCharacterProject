import json
import random
import time

with open("D&D.json", "r") as f:
    data =json.load(f)

randIDRace = random.randint(0,4)

randIDClass = random.randint(0,9)

raceName = data['race'][randIDRace]['name']

className = data['class'][randIDClass]['name']

strength = random.randint(7,20)
constitution = random.randint(7,20)
dexterity = random.randint(7,20)
intelligence = random.randint(7,20)
wisdom = random.randint(7,20)
charisma = random.randint(7,20)

print(f"Race: {raceName} \nClass: {className}")

print("Rolling your stats..")
time.sleep(2)
print(f"Strength: {strength}")
print(f"Constitution: {constitution}")
print(f"Dexterity: {dexterity}")
print(f"Intelligence: {intelligence}")
print(f"Wisdom: {wisdom}")
print(f"Charisma: {charisma}")
