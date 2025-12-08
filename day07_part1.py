# Advent of Code 2025 Day 07 Part 1

input_file = "day07_input.txt"


def file_processing():

    # Read all lines into memory
    with open(input_file, "r") as file:
        all_lines = [line.strip() for line in file]

    # initialize variables
    previous_line = []
    counter_splits = 0

    for line_index in range(len(all_lines)):
        line = all_lines[line_index]
        characters = [char for char in line]

        # Figure out what the index is of the character we're using
        for index, character in enumerate(characters):
            if character == "S":
                # If the character is the start location (S), change it to a beam (|)
                characters[index] = "|"

            if character == ".":
                if previous_line and index < len(previous_line):
                    # Check to see if the character above is a beam (|) and if it is then replace the . with |
                    if previous_line[index] == "|":
                        characters[index] = "|"

            if character == "^":
                # Check to see if the character above is a beam (|)
                if previous_line and index < len(previous_line):
                    if previous_line[index] == "|":
                        # Change the characters to the right and left to beam (|)
                        if index > 0:
                            characters[index - 1] = "|"
                        if index < len(characters) - 1:
                            characters[index + 1] = "|"
                        counter_splits = counter_splits + 1

        # Save the working line to be the previous line for the next loop
        previous_line = characters

        # Update the line in all_lines for next iteration
        all_lines[line_index] = "".join(characters)

    return counter_splits


number_of_splits = file_processing()

print(f"Part 1: The number of beam splits performed is : {number_of_splits}")
