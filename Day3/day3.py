data = []
with open("Day3/input.txt") as fp:
    for line in fp:
        if line != "":
            data.append(line)


# Define the function that calculates the priority of a character
def priority(c):
    if c.islower():
        return ord(c) - ord("a") + 1
    elif c.isupper():
        return ord(c) - ord("A") + 27

# Calculate the sum of the priorities of the item types that appear in both compartments of each rucksack
total = 0
for rucksack in data:
    # Calculate the priorities of the items in the first compartment
    first = set([priority(c) for c in rucksack[:len(rucksack) // 2]])

    # Calculate the priorities of the items in the second compartment
    second = set([priority(c) for c in rucksack[len(rucksack) // 2:]])

    # Calculate the priorities of the item types that appear in both compartments
    common = first.intersection(second)

    # Add the sum of the common priorities to the total
    total += sum(common)

# Print the result
print("The sum of the priorities of the item types that appear in both compartments of each rucksack is %d" % total)

# Calculate the sum of the priorities of the item types that correspond to the badges of each three-Elf group
total = 0
for i in range(0, len(data), 3):
    # Calculate the priorities of the items in the first rucksack
    first = set([priority(c) for c in data[i]])

    # Calculate the priorities of the items in the second rucksack
    second = set([priority(c) for c in data[i + 1]])

    # Calculate the priorities of the items in the third rucksack
    third = set([priority(c) for c in data[i + 2]])

    # Calculate the priorities of the item types that appear in all three rucksacks
    common = (first & second & third)
    common = filter(None, common)
    total += sum(common)

# Print the result
print("The sum of the priorities of the item types that correspond to the badges of each three-Elf group is %d" % total)