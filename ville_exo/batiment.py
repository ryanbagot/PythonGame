class Building:
    def __init__(self, name, floor):
        self.name = name 
        self.floor = floor
    
    def get_name(self): 
        return self.name
    def get_floor(self): 
        return self.floor

class Immeuble(Building): 
    def __init__(self, name, floor):
        super().__init__(name, floor)
        self.balcony = 5

class Bank(Building):
    def __init__(self, name, floor, money):
        super().__init__(name, floor)
        self.money = money
    def get_money(self):
        return self.money

class Supermarket(Building): 
    def __init__(self, name, floor, food, drink):
        super().__init__(name, floor)
        self.food = food
        self.drink = drink
    def get_food(self):
        return self.food
    def get_drink(self): 
        return self.drink
