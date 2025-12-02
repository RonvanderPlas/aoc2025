input_file="../input/input.txt"

def read_file(filename):
    with open(filename, "r") as f:
        line= f.readline()
        full_ranges=line.split(',')
        split_range=[tuple(map(int, full_range.split('-'))) for full_range in full_ranges]
        return split_range

def determine_patter_within_range(pattern_length, low, high):
    invalid_counter = 0
    min_section_length = 1
    max_section_length = pattern_length // 2
    known_patterns = []

    for section_length in range(min_section_length, max_section_length + 1):
        starting_range = int(10 ** (section_length - 1))
        ending_range = int((10 ** section_length) - 1)
        print(f"Pattern length: {pattern_length}, Section Length: {section_length}, Low: {low}, High: {high}, Start Range: {starting_range}, End Range: {ending_range}")
        
        for i in range(starting_range, ending_range + 1):
            pattern = i
            for repeats in range(1, pattern_length // section_length):
                pattern = pattern*(10**(section_length)) + i
                #print(f"Generated pattern: {pattern}")
                if low <= pattern <= high:
                    print(f"Invalid pattern: {pattern}")
                    if(pattern not in known_patterns):
                        invalid_counter += pattern
                        known_patterns.append(pattern)
    return invalid_counter

def main():
    inputs = read_file(input_file)
    invalid_total = 0
    for input in inputs:
        low, high = input
        pattern_length = len(str(high))
        invalid_total += determine_patter_within_range(pattern_length, low, high)
    print(f"Total invalid patterns: {invalid_total}")

if __name__ == "__main__":
	main()
