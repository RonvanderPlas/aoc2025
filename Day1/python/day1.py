class partA:
    def solve(self, input_path):
        start_number = 50
        with open(input_path) as f:
            lines = [line.rstrip("\n") for line in f]
        counter = start_number
        zero_counter = 0
        for line in lines:
            direction = line[0]
            number = int(line[1:])
            if direction == "R":
                counter += number
            elif direction == "L":
                counter -= number
            counter = counter % 100
            if counter == 0:
                zero_counter += 1
        return zero_counter

class partB:
    def solve(self, input_path):
        start_number = 50
        with open(input_path) as f:
            lines = [line.rstrip("\n") for line in f]
        counter = start_number
        zero_counter = 0
        for line in lines:
            direction = line[0]
            line_number = int(line[1:])
            prev_counter = counter
            direction_int = 1 if direction == "R" else -1
            zero_counter += line_number // 100
            remainder = line_number % 100
            counter += direction_int * remainder
            if counter <= 0 and prev_counter != 0:
                zero_counter += 1
            elif counter >= 100:
                zero_counter += 1
            counter %= 100
        return zero_counter
