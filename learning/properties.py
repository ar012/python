class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pipeapple_allowed(self):
        return False

pizza = Pizza(["cheese", "tomato"])
print(pizza.pipeapple_allowed)
pizza.pipeapple_allowed = True