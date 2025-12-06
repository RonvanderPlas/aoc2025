class partA:
    def read_file(self, input_path):
        stripped_lines = []
        with open(input_path, "r") as f:
            for line in f:
                stripped_lines.append(line.rstrip("\n").split())
        return stripped_lines
    
    def solve(self, input_path):
        inputs = self.read_file(input_path)
        formula = inputs.pop()
        total_count=0
        for i in range(len(formula)):
            if formula[i] == "*":
                new_count = 1
            else:
                new_count = 0
            numbers = [int(x[i]) for x in inputs]
            for number in numbers:
                if formula[i] == "*":
                    new_count *= number
                elif formula[i] == "+":
                    new_count += number
            total_count += new_count
        return total_count

class partB:
    def read_file(self, input_path):
        lines = []
        with open(input_path, "r") as f:
            for line in f:
                lines.append([char for char in line.rstrip("\n")])
        return lines

    def convert_digits_to_value(self, digits):
        value = 0
        for digit in digits:
            if digit.isdigit():
                value = value * 10 + int(digit)
        return value
    
    def calulate_new_count(self, current_values, operation):
        new_count = 0
        if operation == "+":
            for val in current_values:
                new_count += val
        elif operation == "*":
            new_count = 1
            for val in current_values:
                new_count *= val
        return new_count
    
    def solve(self, input_path):
        inputs = self.read_file(input_path)
        current_values = []
        total_count = 0
        for i in range(len(inputs[0])-1,-1,-1):
            vertical_slice = [row[i] for row in inputs[:-1]]
            value = self.convert_digits_to_value(vertical_slice)
            if value != 0:
                operation = inputs[-1][i]
                current_values.append(value)
                new_value = self.calulate_new_count(current_values, operation)
                #print(f"Current values: {current_values}, operation: {operation}, new value: {new_value}")
                if new_value != 0:
                    total_count += new_value
                    current_values = []
                    #print(f"New total count: {total_count}")
        return total_count
