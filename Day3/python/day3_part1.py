input_file="../input/input.txt"

def read_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        return [line.rstrip("\n") for line in lines]

def find_highest_digit(string, start_index, stop_index):
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
        highest_digit, highest_digit_index = find_highest_digit(input, 0, len(input)-1)
        second_highest_digit, second_highest_digit_index = find_highest_digit(input, highest_digit_index+1, len(input))
        combined_number = int(str(highest_digit) + str(second_highest_digit))
        total_count += combined_number
        print(f"Input: {input}, Highest: {highest_digit} (Index {highest_digit_index}), Second Highest: {second_highest_digit} (Index {second_highest_digit_index}), Combined: {combined_number}")
    print(f"Total combined count: {total_count}")


if __name__ == "__main__":
	main()
