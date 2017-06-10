def in_fridge():
    """This is a function to see if the fridge has a food.fridge has to be a dictionary defined outside of the function"""
    try:
        count = fridge[wanted_food]
    except KeyError:
        count = 0
    return count


fridge = {'apples': 10, 'oranges': 3, 'milk': 2}
wanted_food = 'apples'
print(in_fridge())
print("%s" % in_fridge.__doc__)

# wanted_food = 'oranges'
# print(in_fridge())
#
# wanted_food = 'milk'
# print(in_fridge())
#
#
# wanted_food = 'milk2'
# print(in_fridge())
