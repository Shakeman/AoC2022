
calories = 0
items = 0
max_calories = 0
list_items = []
list_calories = []
with open("Day1/input.txt") as fp:
    for line in fp:
        if line == '\n':
            if calories > max_calories:
                max_calories = calories
            list_calories.append(calories)
            list_items.append(items)
            calories = 0
            items = 0
        else:
            items += 1
            calories += int(line)
    list_calories.append(calories)
    list_items.append(items)
    print(max(list_calories))
