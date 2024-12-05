"""
Advent of Code 2024 - Day 4 Part 1
Find all occurrences of 'XMAS' in a word search puzzle, including diagonal, backwards, and overlapping.
"""

def find_xmas_occurrences(grid: list) -> int:
    """
    Find all occurrences of 'XMAS' in the grid.

    Args:
        grid (list): 2D list of characters representing the word search

    Returns:
        int: Number of times 'XMAS' appears
    """
    rows = len(grid)
    print(rows)
    cols = len(grid[0])
    print(cols)
    count = 0

    # Directions: right, down-right, down, down-left, left, up-left, up, up-right
    directions = [
        (0, 1),   # right
        (1, 1),   # down-right
        (1, 0),   # down
        (1, -1),  # down-left
        (0, -1),  # left
        (-1, -1), # up-left
        (-1, 0),  # up
        (-1, 1)   # up-right
    ]

    def check_pattern(row: int, col: int, dx: int, dy: int) -> bool:
        """
        Check if 'XMAS' pattern exists starting from given position in given direction.
        """
        pattern = "XMAS"
        for i, char in enumerate(pattern):
            new_row = row + i * dx
            new_col = col + i * dy
            if not (0 <= new_row < rows and 0 <= new_col < cols):
                return False
            if grid[new_row][new_col] != char:
                return False
        return True

    # Check each position as potential start of 'XMAS'
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 'X':  # Only check if starting with 'X'
                for dx, dy in directions:
                    if check_pattern(row, col, dx, dy):
                        count += 1

    return count

def read_input(filename: str) -> list:
    """
    Read and parse the word search grid from input file.

    Args:
        filename (str): Name of input file

    Returns:
        list: 2D list of characters representing the word search
    """
    try:
        with open(filename, 'r') as file:
            return [list(line.strip()) for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: Input file '{filename}' not found")
        return []

def main():
    """
    Main function to execute the program.
    """
    # Read input
    INPUT_FILE = "day4_input.txt"
    grid = read_input(INPUT_FILE)

    if not grid:
        return

    # Find XMAS occurrences
    result = find_xmas_occurrences(grid)
    print(f"Number of XMAS occurrences: {result}")

    # Debug information
    print(f"\nGrid dimensions: {len(grid)}x{len(grid[0])}")

    # Test with example from problem
    example = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX"
    ]
    example_grid = [list(line) for line in example]
    example_result = find_xmas_occurrences(example_grid)
    print(f"Example test result: {example_result}")  # Should be 18

if __name__ == '__main__':
    main()
