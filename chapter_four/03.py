omelet_ingredients = {"egg": 2, "mushroom": 5, "pepper": 1, "cheese": 1, "milk": 1}
fridge_contents = {"egg": 10, "mushroom": 20, "pepper": 3, "cheese": 2, "tomato": 4, "milk": 15}
have_ingredients = [False]

if fridge_contents['egg'] > omelet_ingredients['egg']:
    have_ingredients[0] = True

have_ingredients.append("egg")

print(have_ingredients)
