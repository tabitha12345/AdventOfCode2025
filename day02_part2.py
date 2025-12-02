# Advent of Code 2025 Day 02 Part 2

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

            # Check if the ID contains a sequence of any number of digits repeated
            for seq_length in range(1, length // 2 + 1):
                if length % seq_length == 0:
                    sequence = number_str[:seq_length]
                    repetitions = length // seq_length
                    if sequence * repetitions == number_str:
                        invalid_ids.append(number)

    # Sum up the invalid IDs
    total_invalid_sum = sum(invalid_ids)

    print(f"Part 2: The sum of all invalid IDs is: {total_invalid_sum}")
