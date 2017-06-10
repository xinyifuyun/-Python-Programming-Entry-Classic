def in_fridge(some_fridge, desired_item):
    """This is a function to see if the fridge has a food.fridge has to be a dictionary defined outside of the function"""
    try:
        count = some_fridge[desired_item]
    except KeyError:
        count = 0
    except TypeError:
        count = 0

    return count


fridge = {'apples': 10, 'oranges': 3, 'milk': 2}
wanted_food = "oranges"
print(in_fridge(fridge, wanted_food))
print(in_fridge(4, wanted_food))
print(in_fridge({'cookies': 10, 'broccoli': 3, 'milk': 2}, 'cookies'))
