import json
import random

with open("D&D.json", "r") as f:
    data =json.load(f)

randIDRace = random.randint(0,4)

randIDClass = random.randint(0,9)

raceName = data['race'][randIDRace]['name']

className = data['class'][randIDClass]['name']

print(f"Race: {raceName} \nClass: {className}")