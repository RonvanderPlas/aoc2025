input_file="../input/input.txt"   

def count_invalid_inputs(ranges, inputs):
    valid_ids = set()
    for low,high in ranges:
        for i in range(low, high + 1):
            valid_ids.add(i)
    return len(valid_ids)

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
