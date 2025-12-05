class partA:
    def solve(self, input_path):
        with open(input_path) as f:
            lines = [line.rstrip("\n") for line in f]
        total_count = 0
        for input_str in lines:
            highest_digit = -1
            highest_digit_index = -1
            for i in range(len(input_str) - 1):
                digit = int(input_str[i])
                if digit > highest_digit:
                    highest_digit = digit
                    highest_digit_index = i
            second_highest_digit = -1
            for i in range(highest_digit_index + 1, len(input_str)):
                digit = int(input_str[i])
                if digit > second_highest_digit:
                    second_highest_digit = digit
            combined_number = int(str(highest_digit) + str(second_highest_digit))
            total_count += combined_number
        return total_count

class partB:
    def solve(self, input_path):
        with open(input_path) as f:
            lines = [line.rstrip("\n") for line in f]
        total_count = 0
        for input_str in lines:
            min_index = 0
            combined_number = 0
            for digit in range(1, 13):
                max_index = len(input_str) - (12 - digit)
                highest_digit = -1
                highest_digit_index = -1
                for i in range(min_index, max_index):
                    d = int(input_str[i])
                    if d > highest_digit:
                        highest_digit = d
                        highest_digit_index = i
                min_index = highest_digit_index + 1
                combined_number += highest_digit * (10 ** (12 - digit))
            total_count += combined_number
        return total_count
