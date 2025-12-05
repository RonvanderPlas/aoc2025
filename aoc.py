import argparse
import importlib
import os
import sys
import time

def main():
    parser = argparse.ArgumentParser(description="Run AoC puzzles with timing.")
    parser.add_argument("day", type=int, nargs="?", help="Day number (e.g., 1)")
    parser.add_argument("part", type=int, nargs="?", help="Part number (e.g., 1 or 2)")
    parser.add_argument("--file", type=str, default=None, help="Path to input file (overrides -t)")
    parser.add_argument("-t", "--test", action="store_true", help="Use test input file by default")
    parser.add_argument("--lang", type=str, default="python", choices=["python"], help="Language (default: python)")
    parser.add_argument("--new-day", type=int, help="Create a blank template for a new day")
    args = parser.parse_args()
    # Handle new day creation
    if args.new_day:
        dayN = args.new_day
        day_dir = f"Day{dayN}"
        python_dir = os.path.join(day_dir, "python")
        input_dir = os.path.join(day_dir, "input")
        os.makedirs(python_dir, exist_ok=True)
        os.makedirs(input_dir, exist_ok=True)
        # Create blank dayN.py
        py_file = os.path.join(python_dir, f"day{dayN}.py")
        if not os.path.exists(py_file):
            with open(py_file, "w") as f:
                f.write("class partA:\n    def solve(self, input_path):\n        pass\n\nclass partB:\n    def solve(self, input_path):\n        pass\n")
        # Create blank input files
        for fname in ["input.txt", "input_test.txt"]:
            fpath = os.path.join(input_dir, fname)
            if not os.path.exists(fpath):
                open(fpath, "w").close()
        print(f"Created template for Day {dayN} in {day_dir}/")
        sys.exit(0)

    day_dir = f"Day{args.day}/python"
    puzzle_file = f"day{args.day}.py"
    puzzle_path = os.path.join(day_dir, puzzle_file)

    if not os.path.exists(puzzle_path):
        print(f"Puzzle file not found: {puzzle_path}")
        sys.exit(1)

    # Dynamic import
    module_name = f"Day{args.day}.python.day{args.day}"
    try:
        puzzle_module = importlib.import_module(module_name)
    except Exception as e:
        print(f"Error importing module {module_name}: {e}")
        sys.exit(1)

    # Find Puzzle class
    if args.part == 1:
        puzzle_class = getattr(puzzle_module, "partA", None)
    elif args.part == 2:
        puzzle_class = getattr(puzzle_module, "partB", None)
    if puzzle_class is None:
        print(f"Puzzle class not found in {module_name}")
        sys.exit(1)

    # Determine input file
    if args.file:
        input_path = f"Day{args.day}/input/{args.file}"
    elif args.test:
        input_path = f"Day{args.day}/input/input_test.txt"
    else:
        input_path = f"Day{args.day}/input/input.txt"
    if not os.path.exists(input_path):
        print(f"Input file not found: {input_path}")
        sys.exit(1)

    # Run and time
    puzzle = puzzle_class()
    start = time.time()
    answer = puzzle.solve(input_path)
    end = time.time()

    print("\n" + "=" * 40)
    print(f"🎄 Advent of Code Runner 🎄")
    print("=" * 40)
    print(f"Day:        {args.day}")
    print(f"Part:       {args.part}")
    print(f"Input file: {input_path}")
    print(f"Execution:  {end - start:.6f} seconds")
    print(f"Answer:     {answer}")
    print("=" * 40 + "\n")

if __name__ == "__main__":
    main()
