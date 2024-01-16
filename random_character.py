__author__ = "Timothy D.S. Fee"
__version__ = "0.1.0"


def main():
    import json
    import random
    import time

    with open("D&D.json", "r") as f:
        data = json.load(f)

    # Race
    rand_id_race = random.randint(0, 5)
    race_name = data['race'][rand_id_race]['name']

    # Class and Sub-Class
    rand_id_class = random.randint(0, 11)
    class_name = data['class'][rand_id_class]['name']
    sub_class = data['class'][rand_id_class]['sub-class']
    subclass_len = len(sub_class) - 1
    rand_id_subclass = random.randint(0, subclass_len)
    subclass_name = data['class'][rand_id_class]['sub-class'][rand_id_subclass]

    # Stats
    stat1 = random.randint(7, 18)
    stat2 = random.randint(7, 18)
    stat3 = random.randint(7, 18)
    stat4 = random.randint(7, 18)
    stat5 = random.randint(7, 18)
    stat6 = random.randint(7, 18)

    stat_values = [stat1, stat2, stat3, stat4, stat5, stat6]

    stats = {
        "Strength:": 0,
        "Dexterity:": 0,
        "Constitution:": 0,
        "Intelligence:": 0,
        "Wisdom:": 0,
        "Charisma:": 0
    }

    max_name_length = max(len(name) for name in stats.keys())

    # Printing results of random race, class and sub-class
    print(f"Race: {race_name} \nClass: {class_name}\nSub-Class: {subclass_name}")

    for x in range(0, 5):
        b = "Rolling stats" + "." * x
        print(b, end="\r")
        time.sleep(1)

    # Printing stats
    print(f"\nStat 1: {stat1}")
    print(f"Stat 2: {stat2}")
    print(f"Stat 3: {stat3}")
    print(f"Stat 4: {stat4}")
    print(f"Stat 5: {stat5}")
    print(f"Stat 6: {stat6}")

    print("Input stat values!")

    # Method to remove stat from list when it is selected
    def remove_number_from_list(number, my_list):
        if number in my_list:
            my_list.remove(number)
        else:
            print(f"Error: {number} is not in the list or has already been used. Please try again.")

    # Checking stat entries to make sure they have not been used and making sure they exist in the list
    for stat_name, initial_value in stats.items():
        while True:
            try:
                stat_value = int(input(f"{stat_name.capitalize()} "))
                if stat_value in stat_values:
                    remove_number_from_list(stat_value, stat_values)
                    stats[stat_name] = stat_value
                    break
                else:
                    print("Error: The entered number is either not in the list or has already been entered."
                          "\nPlease try again!")
            except ValueError:
                print("Error: Please enter a valid number.")

    name = input("Good job! Now give your character a name:\n")
    for x in range(0, 5):
        b = "Thank you! Generating character sheet" + "." * x
        print(b, end="\r")
        time.sleep(1)

    # Printing the character sheet
    print("\nCharacter Sheet")
    print(f"Name:             {name}")
    print(f"Race:             {race_name}")
    print(f"Class:            {class_name}")
    for stat_name, stat_value in stats.items():
        print(f"{stat_name.ljust(max_name_length)}     {stat_value}")

    print('''\n

           .ed"""" """$$$$be.
         -"           ^""**$$$e.
       ."                   '$$$c
      /                      "4$$b
     d  3                      $$$$
     $  *                   .$$$$$$
    .$  ^c           $$$$$e$$$$$$$$.
    d$L  4.         4$$$$$$$$$$$$$$b
    $$$$b ^ceeeee.  4$$ECL.F*$$$$$$$
    $$$$P d$$$$F $ $$$$$$$$$- $$$$$$
    3$$$F "$$$$b   $"$$$$$$$  $$$$*"
     $$P"  "$$b   .$ $$$$$...e$$
      *c    ..    $$ 3$$$$$$$$$$eF
        %ce""    $$$  $$$$$$$$$$*
         *$e.    *** d$$$$$"L$$
          $$$      4J$$$$$% $$$
         $"'$=e....$*$$**$cz$$"
         $  *=%4.$ L L$ P3$$$F
         $   "%*ebJLzb$e$$$$$b
          %..      4$$$$$$$$$$
           $$$e   z$$$$$$$$$$
            "*$c  "$$$$$$$P"
              """*$$$$$$$"

    ''')

if __name__ == "__main__":
    main()


'''
A few things I would like to add:
- Random spells if the class chosen is a spell caster
- Adding the stats to a list and having the user choose from that list so they can't just put whatever stat they want.
- Print a PDF with their information on it
'''
