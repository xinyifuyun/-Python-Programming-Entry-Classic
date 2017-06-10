fridge_contents = {"egg": 8, "mushroom": 20, "pepper": 3, "cheese": 2, "tomato": 4, "milk": 13}
try:
    if fridge_contents['orange juice'] > 3:
        print("Sure")
except KeyError as error:
    print("no juice %s " % error)
