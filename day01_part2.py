# Advent of Code 2025 Day 01 Part 2

input_file = "day01_input.txt"

# initialize start positions
dial_location = 50
counter = 0

try:
    with open(input_file, "r") as file:
        for line in file:
            # get rid of the new line character
            line = line.strip()

            # split the line into the direction and number to spin
            direction = line[0]
            number = int(line[1:])

            if direction == "R":
                # for right, count how many times we pass or land on 0

                # starting position
                start_pos = dial_location
                end_pos = dial_location + number

                if end_pos > 0 and end_pos % 100 == 0:
                    # 0 is exactly on a multiple of 100
                    zero_crossings = end_pos // 100
                else:
                    # pass through 0 only
                    zero_crossings = end_pos // 100 - start_pos // 100

                counter = counter + zero_crossings

                # update dial location
                dial_location = end_pos % 100

            elif direction == "L":
                # for left, count how many times we pass or land on 0

                # starting position
                start_pos = dial_location
                end_pos = dial_location - number

                # for left, count how many times we pass or land on 0
                if end_pos < 0:
                    zero_crossings = (start_pos - 1) // 100 - (end_pos - 1) // 100
                    counter += zero_crossings
                elif end_pos == 0:
                    # land exactly on 0
                    counter = counter + 1

                # update dial location
                dial_location = end_pos % 100  # account for errors

except FileNotFoundError:
    print(f"Error: The file '{input_file}' seems to be missing.")
except Exception as e:
    print(f"Another random error occurred: {e}")

print("Part 2: The number of times the dial location loops 0 is " + str(counter))
