class partA:
    def solve(self, input_path):
        with open(input_path) as f:
            line = f.readline()
        full_ranges = line.split(',')
        split_range = [tuple(map(int, full_range.split('-'))) for full_range in full_ranges]
        invalid_total = 0
        for low, high in split_range:
            pattern_length = max(len(str(low)), len(str(high)))
            section_length = pattern_length // 2
            starting_range = int(10 ** (section_length - 1))
            ending_range = int((10 ** section_length) - 1)
            for i in range(starting_range, ending_range + 1):
                pattern = (i * (10 ** section_length)) + i
                if low <= pattern <= high:
                    invalid_total += pattern
        return invalid_total

class partB:
    def solve(self, input_path):
        with open(input_path) as f:
            line = f.readline()
        full_ranges = line.split(',')
        split_range = [tuple(map(int, full_range.split('-'))) for full_range in full_ranges]
        invalid_total = 0
        for low, high in split_range:
            pattern_length = len(str(high))
            min_section_length = 1
            max_section_length = pattern_length // 2
            known_patterns = set()
            for section_length in range(min_section_length, max_section_length + 1):
                starting_range = int(10 ** (section_length - 1))
                ending_range = int((10 ** section_length) - 1)
                for i in range(starting_range, ending_range + 1):
                    pattern = i
                    for repeats in range(1, pattern_length // section_length):
                        pattern = pattern * (10 ** section_length) + i
                        if low <= pattern <= high and pattern not in known_patterns:
                            invalid_total += pattern
                            known_patterns.add(pattern)
        return invalid_total
