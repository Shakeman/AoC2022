data = []
score_map = {"X": 1, "Y": 2, "Z": 3}
opponent_map = {"A": 1, "B": 2, "C": 3}
win_map = {"X": 0, "Y": 3, "Z": 6}
with open("Day2/input.txt") as fp:
    for line in fp:
        if line != "":
            data.append(line.split())


score = 0
for round in data:
    choice = round[1]
    score += score_map[choice]

    opponent = round[0]
    if score_map[choice] == opponent_map[opponent]:
        score += 3  # draw
    elif (choice == "Y" and opponent == "A") or (choice == "Z" and opponent == "B") or (choice == "X" and opponent == "C"):
        score += 6  # win
print("Total Score based on playing instructions is: " + str(score))

score = 0
for round in data:
    result = round[1]
    score += win_map[result]
    opponent = round[0]
    if result == "X": # lose
        score += ((opponent_map[opponent]+4)%3) + 1
    elif result == "Y": # draw
        score += opponent_map[opponent]
    elif result == "Z": # win
        score += (opponent_map[opponent]%3)+1 #shift 1 to 2, 2 to 3, 3 to 1
print("Total Score based on win/lose instruction is: " + str(score))