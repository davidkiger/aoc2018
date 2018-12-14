p_input = 286051

elves = [0, 1]
recipes = [3, 7]

while len(recipes) < p_input+10:
    new_recipe = recipes[elves[0]] + recipes[elves[1]]
    recipes.extend([int(d) for d in str(new_recipe)])

    elves[0] = (elves[0] + (recipes[elves[0]] + 1)) % len(recipes)
    elves[1] = (elves[1] + (recipes[elves[1]] + 1)) % len(recipes)

print(''.join(str(d) for d in recipes[p_input:p_input+10]))
