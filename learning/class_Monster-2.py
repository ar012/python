# The blueprint to create monsters
class Monster:
    def __init__(self, color, heads):
        self.color = color
        self.heads = heads

    def attack(self):
        print("Just attacked a Hero, Mu...hahahaha!!!")


# Create an instance/object/monster-charachter
mournsnake = Monster("Yellow", 4)

#Check if its cteated or not
print('I am a ' + str(mournsnake.heads) + ' headed monster. ')
# Make an attack by the new monster
mournsnake.attack()


# Class Atribute
print("\nClass Atribute:\n")

class Monster:
    identify = "negative character"

    def __init__(self, color, heads):
        self.color = color
        self.heads = heads

    def attack(self):
        print("Just attacked a Hero, Mu...hahaha!!!")

mournsnake = Monster("Yellow", 4)
tangleface = Monster("Red", 3)
print("I am a " + str(mournsnake.heads) + " headed " + mournsnake.identify)
print("I am a " + str(tangleface.heads) + " headed " + tangleface.identify)

# print(Monster.identify)
# print(mournsnake.identify)