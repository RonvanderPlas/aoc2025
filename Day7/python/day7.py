class partA:
    def read_file(self, input_path):
        mapped_lines = []
        with open(input_path, "r") as f:
            all_lines = f.readlines()
            for line in all_lines:
                characters = [char for char in line.rstrip("\n")]
                mapped_lines.append(characters)
        return mapped_lines
    
    def print_input(self, lines):
        for line in lines:
            for char in line:
                print(char, end="")
            print()
    
    
    def solve(self, input_path):
        input_map = self.read_file(input_path)
        self.print_input(input_map)
        prev_line = input_map[0]
        split_count = 0
        for i in range(1,len(input_map)):
            new_line = input_map[i]
            for i in range(len(new_line)):
                if prev_line[i] == "S" or prev_line[i] == "|":
                    if new_line[i] == "^":
                        split_count += 1
                        if i - 1 >= 0:
                            new_line[i-1] = "|"
                        if i + 1 < len(new_line):
                            new_line[i+1] = "|"
                    else:
                        new_line[i] = "|"
            prev_line = new_line 
            # print("\nAfter processing line:") 
            # self.print_input(input_map)
        return split_count  

class partB:
    def read_file(self, input_path):
        mapped_lines = []
        with open(input_path, "r") as f:
            all_lines = f.readlines()
            for line in all_lines:
                characters = [char for char in line.rstrip("\n")]
                mapped_lines.append(characters)
        return mapped_lines
    
    def print_input(self, lines):
        for line in lines:
            for char in line:
                print(char, end="")
            print()
    
    def zero_map(self, input_map):
         return [[0 for _ in line] for line in input_map]
    
    def solve(self, input_path):
        input_map = self.read_file(input_path)
        value_map = self.zero_map(input_map)
        self.print_input(input_map)
        prev_line = input_map[0]
        prev_value_line = [1 for _ in prev_line]
        split_count = 0
        for y in range(1,len(input_map)):
            new_line = input_map[y]
            new_value_line = value_map[y]
            for x in range(len(new_line)):
                if prev_line[x] == "S" or prev_line[x] == "|":
                    if new_line[x] == "^":
                        if x - 1 >= 0:
                            new_line[x-1] = "|"
                            new_value_line[x-1] += prev_value_line[x]
                        if x + 1 < len(new_line):
                            new_line[x+1] = "|"
                            new_value_line[x+1] += prev_value_line[x]
                    else:
                        new_line[x] = "|"
                        new_value_line[x] += prev_value_line[x]
            prev_line = new_line 
            prev_value_line = new_value_line
        
        #count splits at the bottom
        for val in value_map[-1]:
            split_count += val
        return split_count  
