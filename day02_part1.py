# Advent of Code 2025 Day 02 Part 1

input_file = "day02_input.txt"

with open(input_file, "r") as file:
    original_data = file.read()

    # Split the input into ranges
    ranges = original_data.strip().split(",")

    # Expand the ranges into individual IDs
    invalid_ids = []
    for item in ranges:
        # Split the range into start and end numbers
        start_number, end_number = item.split("-")
        # Remove leading zeros from the start number
        start_number = start_number.lstrip("0")
        # Convert to integers
        start = int(start_number)
        end = int(end_number)

        for number in range(start, end + 1):

            number_str = str(number)
            length = len(number_str)

            # Check if the ID is made of a sequence of any number of digits repeated
            half_length = length // 2
            first_half = number_str[:half_length]
            second_half = number_str[half_length:]

            if first_half == second_half:
                invalid_ids.append(number)

    # Sum up the invalid IDs
    total_invalid_sum = sum(invalid_ids)

    print(f"Part 1: The sum of all invalid IDs is: {total_invalid_sum}")
