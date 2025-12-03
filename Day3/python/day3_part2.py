input_file="../input/input.txt"

def read_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        return [line.rstrip("\n") for line in lines]

def find_highest_digit(string, start_index, stop_index):
    #print(f"Finding highest digit in range {start_index} to {stop_index} of string: {string}")
    highest_digit = -1
    highest_digit_index = -1
    for i in range(start_index, stop_index):
        digit = int(string[i])
        if digit > highest_digit:
            highest_digit = digit
            highest_digit_index = i
    return highest_digit, highest_digit_index

def main():
    inputs = read_file(input_file)
    total_count = 0
    for input in inputs:
        min_index = 0
        combined_number = 0
        for digit in range(1,13):
            max_index = len(input) - (12-digit)
            highest_digit, highest_digit_index = find_highest_digit(input, min_index, max_index)
            min_index = highest_digit_index + 1
            combined_number += highest_digit * (10 ** (12 - digit))
            #print(f"Input: {input}, Digit Position: {digit}, Highest: {highest_digit} (Index {highest_digit_index}), Combined so far: {combined_number}")
        print(f"Final combined number for input {input}: {combined_number}")
        total_count += combined_number  

    print(f"Total combined count: {total_count}")


if __name__ == "__main__":
	main()
