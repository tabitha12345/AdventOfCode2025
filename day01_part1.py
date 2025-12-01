# Advent of Code 2025 Day 01 Part 1

input_file = "day01_input.txt"

# initialize start positions
dial_location = 50
counter = 0

try:
    with open(input_file, 'r') as file:
        for line in file:
            # get rid of the new line character
            line = line.strip()
            # split the line into the direction and number to spin
            direction = line[0]
            number = int(line[1:])

            if direction == "R":
                # for right turns, add to the number, loop after 99
                dial_location = (dial_location + number) % 100
                if dial_location == 0:
                    # add to the counter if the result is 0
                    counter = counter + 1
            elif direction == "L":
                # for left turns, subtract from the number, loop after 0
                dial_location = (dial_location - number) % 100
                if dial_location == 0:
                    # add to the counter if the result is 0
                    counter = counter + 1

# account for errors
except FileNotFoundError:
    print(f"Error: The file '{input_file}' seems to be missing.")
except Exception as e:
    print(f"Another random error occurred: {e}")

print("Part 1: The number of times the dial location hits 0 is " + str(counter))

print(dial_location)