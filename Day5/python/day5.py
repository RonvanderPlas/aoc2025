class partA:
    def solve(self, input_path: str) -> int:
        ranges = []
        inputs = []
        with open(input_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.rstrip("\n")
                if "-" in line:
                    parts = line.split("-")
                    ranges.append( (int(parts[0]), int(parts[1])) )
                elif line != "":
                    inputs.append(int(line))
        return self.count_invalid_inputs(ranges, inputs)

    def count_invalid_inputs(self, ranges, inputs):
        valid_count = 0
        for value in inputs:
            valid = False
            for low,high in ranges:
                #print(f"Checking if {value} is between {low} and {high}")
                if low <= value <= high:
                    valid = True
                    break
            if valid:
                valid_count += 1
        return valid_count

class partB:
    def solve(self, input_path: str) -> int:
        ranges = []
        inputs = []
        with open(input_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.rstrip("\n")
                if "-" in line:
                    parts = line.split("-")
                    ranges.append( (int(parts[0]), int(parts[1])) )
                elif line != "":
                    inputs.append(int(line))
        return self.count_invalid_inputs(ranges, inputs)

    def count_invalid_inputs(self, ranges, inputs):
        sorted_ranges = sorted(ranges, key=lambda x: x[0])
        filtered_ranges = []
        total_count = 0

        current_low, current_high = sorted_ranges[0]
        for new_low, new_high in sorted_ranges[1:]:
            #if the new low is within the current range, extend the current range if needed
            if new_low <= current_high and new_high >= current_high:
                current_high = new_high
                #print(f"Extended range to: {current_low}-{current_high}")
            
            #else, if the new low is outside the current range, save the current range and start a new one
            elif new_low > current_high:
                filtered_ranges.append((current_low, current_high))
                current_low, current_high = new_low, new_high
                #print(f"New range started: {current_low}-{current_high}")
        
        #append the last range
        filtered_ranges.append((current_low, current_high))
        
        for low, high in filtered_ranges:
            diff = high - low + 1
            total_count += diff
        return total_count
