input_file="../input/input_test.txt"
start_number=50
def read_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        return [line.rstrip("\n") for line in lines]

def main():
    lines = read_file(input_file)
    counter=start_number
    zero_counter=0
    for line in lines:
        direction=line[0]
        line_number= int(line[1:])
        prev_counter = counter
        if direction=="R":
            counter+=line_number
        elif direction=="L":
            counter-=line_number

        divided = counter // 100
        counter = counter % 100
        zero_counter += abs(divided)

        print(f"Prev: {prev_counter}, entry: {direction}{line_number} New:{counter}, Divided: {divided}, Total zeros: {zero_counter}")
    print(f"Total zero hits: {zero_counter}")

if __name__ == "__main__":
	main()
