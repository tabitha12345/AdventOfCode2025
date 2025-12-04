# Advent of Code 2025 Day 04 Part 2

input_file = "day04_input.txt"

def file_processing():

    # Read all lines into memory
    with open(input_file, "r") as file:
        all_lines = [line.strip() for line in file]

    # initialize variables
    total_number_of_rolls = 0
    changed = True
    previous_total_number_of_rolls = 0

    while changed:
        changed = False

        previous_line = []
        for line_index in range(len(all_lines)):
            line = all_lines[line_index]
            next_line = all_lines[line_index + 1] if line_index + 1 < len(all_lines) else ""

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

                    # If it can be removed, bump the counter and change the tracker to True so the loop will run again
                    if surrounding_rolls < 4:
                        total_number_of_rolls = total_number_of_rolls + 1
                        characters[index] = "."
                        changed = True  # Mark that we made a change

            # Save the working line to be the previous line for the next loop
            previous_line = characters

            # Update the line in all_lines for next iteration
            all_lines[line_index] = "".join(characters)

        if previous_total_number_of_rolls < total_number_of_rolls:
            changed = True
            previous_total_number_of_rolls = total_number_of_rolls

    return total_number_of_rolls

total_number_of_rolls = file_processing()

print(f"Part 2: The number of rolls that can be accessed is: {total_number_of_rolls}")
