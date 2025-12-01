input_file="../input/input.txt"
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
        number= int(line[1:])
        if direction=="R":
            counter+=number
        elif direction=="L":
            counter-=number
        counter = counter % 100

        if counter==0:
            zero_counter+=1
            print(f"Zero hit {zero_counter} times")

if __name__ == "__main__":
	main()
