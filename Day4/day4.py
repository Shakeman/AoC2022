def count_fully_contained_pairs(pairs):
  count = 0
  for pair in pairs:
    first_range, second_range = pair.split(",")
    first_range_start, first_range_end = map(int, first_range.split("-"))
    second_range_start, second_range_end = map(int, second_range.split("-"))
    if (first_range_start <= second_range_start and first_range_end >= second_range_end) or (second_range_start <= first_range_start and second_range_end >= first_range_end):
      count += 1
  return count

def count_overlapping_pairs(pairs):
  count = 0
  for pair in pairs:
    first_range, second_range = pair.split(",")
    first_range_start, first_range_end = map(int, first_range.split("-"))
    second_range_start, second_range_end = map(int, second_range.split("-"))
    if (first_range_start <= second_range_end and first_range_end >= second_range_start) or (second_range_start <= first_range_end and second_range_end >= first_range_start):
      count += 1
  return count

# read input from file
with open("Day4/input.txt", "r") as input_file:
  input_data = input_file.read()

# split input into lines
lines = input_data.split("\n")

# remove empty lines
lines = [line for line in lines if line]

# count fully contained pairs
result = count_fully_contained_pairs(lines)
print(result)
result = count_overlapping_pairs(lines)
print(result)