# Advent of Code 2025 Day 03 Part 2

input_file = "day03_input.txt"

# Set up start values
total_output_joltage = 0

try:
    with open(input_file, "r") as file:
        for line in file:
            # Get rid of the new line character
            line = line.strip()
            numbers = [int(item) for item in line]

            # Find the maximum joltage from any 12 batteries (keeping order!)
            def get_max_k_digits(nums, k):
                result = []
                to_remove = len(nums) - k

                for num in nums:
                    # Remove smaller digits from result if we can afford to skip them
                    while result and result[-1] < num and to_remove > 0:
                        result.pop()
                        to_remove -= 1
                    result.append(num)

                # Return only first k digits
                return int("".join(map(str, result[:k])))

            max_joltage = get_max_k_digits(numbers, 12)

            # Use the maximum joltage for this bank
            bank_joltage = max_joltage
            print(bank_joltage)

            # Add bank joltage to total output joltage
            total_output_joltage = total_output_joltage + bank_joltage

# Account for errors
except FileNotFoundError:
    print(f"Error: The file '{input_file}' seems to be missing.")
except Exception as e:
    print(f"Another random error occurred: {e}")

print(f"Part 2: The sum of the total output joltage is: {total_output_joltage}")
