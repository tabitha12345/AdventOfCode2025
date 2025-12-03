# Advent of Code 2025 Day 03 Part 1

input_file = "day03_input.txt"

# Set up start values
total_output_joltage = 0

try:
    with open(input_file, "r") as file:
        for line in file:
            # Get rid of the new line character
            line = line.strip()
            numbers = [int(item) for item in line]

            # Find the maximum joltage from all possible pairs (maintain order!)
            max_joltage = 0
            for i in range(len(numbers)):
                for j in range(i + 1, len(numbers)):
                    # Create two-digit number from batteries at positions i and j
                    pair_joltage = numbers[i] * 10 + numbers[j]
                    max_joltage = max(max_joltage, pair_joltage)

            # Use the maximum joltage for this bank
            bank_joltage = max_joltage
            # Add bank joltage to total output joltage
            total_output_joltage = total_output_joltage + bank_joltage

# Account for errors
except FileNotFoundError:
    print(f"Error: The file '{input_file}' seems to be missing.")
except Exception as e:
    print(f"Another random error occurred: {e}")

print(f"Part 1: The sum of the total output joltage is: {total_output_joltage}")
