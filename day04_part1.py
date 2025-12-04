# Advent of Code 2025 Day 04 Part 1

input_file = "day04_input.txt"

# initialize counter:
total_number_of_rolls = 0

try:
    with open(input_file, "r") as file:
        previous_line = []

        line = file.readline().strip()

        while line:
            next_line = file.readline().strip()
            characters = [char for char in line]

            # Figure out what the index is of the character we're using
            for index, character in enumerate(characters):

                # If it's a roll (@), check characters around it
                if character == "@":
                    surrounding_rolls = 0

                    # Check character to the upper left if it's not the first character or first line
                    if previous_line and index != 0:
                        if previous_line[index - 1] == "@":
                            surrounding_rolls = surrounding_rolls + 1

                    # Check character to the upper center if it's not the first line
                    if previous_line:
                        if previous_line[index] == "@":
                            surrounding_rolls = surrounding_rolls + 1

                    # Check character to the upper right if it's not the last character or first line
                    if previous_line and index != len(characters) - 1:
                        if previous_line[index + 1] == "@":
                            surrounding_rolls = surrounding_rolls + 1

                    # Check character to the left if it's not the first character
                    if index != 0:
                        if characters[index - 1] == "@":
                            surrounding_rolls = surrounding_rolls + 1

                    # Check character to the right if it's not the last character
                    if index != len(characters) - 1:
                        if characters[index + 1] == "@":
                            surrounding_rolls = surrounding_rolls + 1

                    # Check character to the lower left if it's not the first character or last line
                    if next_line and index != 0:
                        if next_line[index - 1] == "@":
                            surrounding_rolls = surrounding_rolls + 1

                    # Check character to the lower center if it's not the last line
                    if next_line:
                        if next_line[index] == "@":
                            surrounding_rolls = surrounding_rolls + 1

                    # Check character to the lower right if it's not the last character or last line
                    if next_line and index != len(characters) - 1:
                        if next_line[index + 1] == "@":
                            surrounding_rolls = surrounding_rolls + 1

                    if surrounding_rolls < 4:
                        total_number_of_rolls = total_number_of_rolls + 1

            # Save the working line to be the previous line for the next loop
            previous_line = characters

            # Bump down to make the next line the working line
            line = next_line

# Account for errors
except FileNotFoundError:
    print(f"Error: The file '{input_file}' seems to be missing.")
except Exception as e:
    print(f"Another random error occurred: {e}")

print(f"Part 1: The number of rolls that can be accessed is: {total_number_of_rolls}")
