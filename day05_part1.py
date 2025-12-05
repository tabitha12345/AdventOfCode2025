# Advent of Code 2025 Day 05 Part 1

input_file = "day05_input.txt"

# initialize variables
fresh_ids = []
ingredient_ids = []
counter = 0

with open(input_file, "r") as file:
    original_data = file.read()

# Split the original data at the first occurrence of a blank line and remove whitespace
original_split = original_data.split("\n\n", 1)

# Get the fresh ranges and ids
fresh_ranges_original = original_split[0].strip()
ids_original = original_split[1].strip()

# Expand fresh_ranges_original into actual ranges split by new lines
ranges = fresh_ranges_original.split("\n")

for item in ranges:

    # Split the range into start and end values
    start_number, end_number = item.split("-")

    # Convert to integers
    start = int(start_number)
    end = int(end_number)

    # Store ranges as tuples instead of expanding
    fresh_ids.append((start, end))

# Make a list of ingredient ids
ingredient_ids = ids_original.split("\n")

# Count the number of ingredients that appear in fresh_ids
for ingredient in ingredient_ids:
    ingredient_num = int(ingredient)
    # Check if ingredient falls within any range
    for start, end in fresh_ids:
        if start <= ingredient_num <= end:
            counter = counter + 1
            break

print(f"Part 1: The number of fresh ingredients is : {counter}")
