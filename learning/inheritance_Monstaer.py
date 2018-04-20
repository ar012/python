# The blueprint to create monsters
class Monster:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def attack(self):
        print("I am attacking...")

# Create subclasses of Monster class
class Fogthing(Monster):
    def make_sound(self):
        print('Grrrrrrrr\n')

    # Overriding the method: attack
    def attack(self):
        print("I am killing.....")

class Mournsnake(Monster):
    def make_sound(self):
        print('Hiiisssshhhh\n')

# Create some real monsters
fogthing = Fogthing("Fogthing", "Yellow")
fogthing.attack()
fogthing.make_sound()

mournsnake = Mournsnake("Mournsnake", "Red")
mournsnake.attack()
mournsnake.make_sound()
