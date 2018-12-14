p_input = 286051

elves = [0, 1]
recipes = [3, 7]

while True:
    new_recipe = recipes[elves[0]] + recipes[elves[1]]
    recipes.extend([int(d) for d in str(new_recipe)])

    elves[0] = (elves[0] + (recipes[elves[0]] + 1)) % len(recipes)
    elves[1] = (elves[1] + (recipes[elves[1]] + 1)) % len(recipes)

    try:
        if (recipes[-6] == 2 and
           recipes[-5] == 8 and
           recipes[-4] == 6 and
           recipes[-3] == 0 and
           recipes[-2] == 5 and
           recipes[-1] == 1):
            print(len(recipes) - 6)
            exit()

        if (recipes[-7] == 2 and
           recipes[-6] == 8 and
           recipes[-5] == 6 and
           recipes[-4] == 0 and
           recipes[-3] == 5 and
           recipes[-2] == 1):
            print(len(recipes) - 7)
            exit()
    except IndexError:
        pass
