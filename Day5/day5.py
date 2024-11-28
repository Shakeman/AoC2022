# define a class for a stack of crates
class Stack:
  def __init__(self):
    self.crates = []

  def push(self, crate):
    self.crates.append(crate)

  def pop(self):
    return self.crates.pop()

# read input from file
with open("Day5/input.txt", "r") as input_file:
  input_data = input_file.read()

# split input into lines
lines = input_data.split("\n")

# remove empty lines
lines = [line for line in lines if line]

# count fully contained pairs
result = count_fully_contained_pairs(lines)
print(result)