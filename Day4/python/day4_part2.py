input_file="../input/input.txt"

adjecent_cells = [(-1, -1), (-1, 0), (-1, 1),
                       (0, -1),          (0, 1),
                       (1, -1),  (1, 0), (1, 1)]

def read_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        return [list(line.rstrip("\n")) for line in lines]
    
def print_grid(grid):
    for row in grid:
        print("".join(row))
    print("\n")

def count_adjecent_values(grid, x, y, target_value):
    count = 0
    width = len(grid[0])
    height = len(grid)
    for cell in adjecent_cells:
        adj_x = x + cell[0]
        adj_y = y + cell[1]
        if 0 <= adj_x < width and 0 <= adj_y < height:
            if grid[adj_y][adj_x] == target_value:
                count += 1
    return count

def main():
    grid = read_file(input_file)
    width = len(grid[0])
    height = len(grid)
    total_count = 0
    could_remove = True
    while could_remove:
        could_remove = False
        for y in range(height):
            for x in range(width):
                if grid[y][x] == '@':
                    adjecent_count = count_adjecent_values(grid, x, y, '@')
                    if adjecent_count < 4:
                        grid[y][x] = '.'
                        total_count += 1
                        could_remove = True
    print(f"Total possible '@' cells: {total_count}")


if __name__ == "__main__":
	main()
