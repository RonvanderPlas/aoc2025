input_file="../input/input.txt"   

def count_invalid_inputs(ranges, inputs):
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

def main():
    ranges = []
    inputs = []
    total_count = 0
    with open(input_file, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip("\n")
            if "-" in line:
                parts = line.split("-")
                ranges.append( (int(parts[0]), int(parts[1])) )
            elif line != "":
                inputs.append(int(line))
    total_count = count_invalid_inputs(ranges, inputs)
    print(f"Total invalid inputs: {total_count}")


if __name__ == "__main__":
	main()
