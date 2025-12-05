class partA:
    def solve(self, input_path):
        adjecent_cells = [(-1, -1), (-1, 0), (-1, 1),
                          (0, -1),          (0, 1),
                          (1, -1),  (1, 0), (1, 1)]
        with open(input_path) as f:
            grid = [list(line.rstrip("\n")) for line in f]
        width = len(grid[0])
        height = len(grid)
        total_count = 0
        for y in range(height):
            for x in range(width):
                if grid[y][x] == '@':
                    adjecent_count = 0
                    for cell in adjecent_cells:
                        adj_x = x + cell[0]
                        adj_y = y + cell[1]
                        if 0 <= adj_x < width and 0 <= adj_y < height:
                            if grid[adj_y][adj_x] == '@':
                                adjecent_count += 1
                    if adjecent_count < 4:
                        total_count += 1
        return total_count

class partB:
    def solve(self, input_path):
        adjecent_cells = [(-1, -1), (-1, 0), (-1, 1),
                          (0, -1),          (0, 1),
                          (1, -1),  (1, 0), (1, 1)]
        with open(input_path) as f:
            grid = [list(line.rstrip("\n")) for line in f]
        width = len(grid[0])
        height = len(grid)
        total_count = 0
        could_remove = True
        while could_remove:
            could_remove = False
            for y in range(height):
                for x in range(width):
                    if grid[y][x] == '@':
                        adjecent_count = 0
                        for cell in adjecent_cells:
                            adj_x = x + cell[0]
                            adj_y = y + cell[1]
                            if 0 <= adj_x < width and 0 <= adj_y < height:
                                if grid[adj_y][adj_x] == '@':
                                    adjecent_count += 1
                        if adjecent_count < 4:
                            grid[y][x] = '.'
                            total_count += 1
                            could_remove = True
        return total_count
