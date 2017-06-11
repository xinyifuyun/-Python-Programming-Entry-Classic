class Fridge:
    """This class implements a fridge where ingredients can be added and removed individually, or in groups."""

    def __init__(self, items={}):
        if type(items) != type({}):
            raise TypeError("Fridge requires a dictionary but was given %s" % type(items))
        self.items = items
        return

    def __add_multi(self, food_name, quantity):
        if (not food_name in self.items):
            self.items[food_name] = 0

        self.items[food_name] = self.items[food_name] + quantity

    def add_one(self, food_name):
        if type(food_name) != type(""):
            raise TypeError("add_one requires a string, given a %s" % type(food_name))
        else:
            self.__add_multi(food_name, 1)

        return True

    def add_many(self, food_dict):
        if type(food_dict) != type({}):
            raise TypeError("add_many requires a dict, got a %s" % type(food_dict))

        for item in food_dict.keys():
            self.__add_multi(item, food_dict[item])

        return True

    def has(self, food_name, quantity=1):
        return self.has_various({food_name: quantity})

    def has_various(self, foods):
        try:
            for food in foods.keys():
                if self.items[food] < foods[food]:
                    return False

            return True
        except KeyError:
            return False


f = Fridge({'eggs': 6, 'milk': 4, 'cheese': 3})
print(f.items)
f.add_one('grape')
print(f.items)
f.add_many({'mushroom': 5, 'tomato': 3})
print(f.items)
if f.has('cheese', 2):
    print("It's time to make an omelet!")
# {'eggs': 6, 'milk': 4, 'cheese': 3}
# {'eggs': 6, 'milk': 4, 'cheese': 3, 'grape': 1}
# {'eggs': 6, 'milk': 4, 'cheese': 3, 'grape': 1, 'mushroom': 5, 'tomato': 3}
