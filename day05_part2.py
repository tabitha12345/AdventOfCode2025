# Advent of Code 2025 Day 05 Part 2

input_file = "day05_input.txt"

# initialize variables
fresh_ids = []
counter = 0

with open(input_file, "r") as file:
    original_data = file.read()

# Split the original data at the first occurrence of a blank line and remove whitespace
original_split = original_data.split("\n\n", 1)

# Get the fresh ranges
fresh_ranges_original = original_split[0].strip()

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

    # Remove duplicates and sort
    fresh_ids = sorted(set(fresh_ids))

    # Merge overlapping ranges
    merged = []
    for start, end in fresh_ids:
        if merged and start <= merged[-1][1] + 1:
            # Overlaps or adjacent - merge with previous range
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            # No overlap - add as new range
            merged.append((start, end))

    # Count total IDs in merged ranges
    counter = sum(end - start + 1 for start, end in merged)

print(f"Part 2: The number of possible fresh ingredients is : {counter}")
