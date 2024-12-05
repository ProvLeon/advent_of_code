"""
Advent of Code 2024 - Day 4 Part 2
Find X-shaped patterns where each diagonal is 'MAS' (can be forwards or backwards).
Pattern should look like:
M.S
.A.
M.S
"""

def check_xmas_pattern(grid: list, row: int, col: int) -> bool:
    """
    Check if an X-shaped MAS pattern exists at the given position.
    Pattern:
    M.S
    .A.
    M.S
    """
    rows = len(grid)
    cols = len(grid[0])

    # Check boundaries
    if (row < 1 or row >= rows - 1 or
        col < 1 or col >= cols - 1):
        return False

    # Center must be 'A'
    if grid[row][col] != 'A':
        return False

    # Check all possible combinations of MAS patterns
    # For each diagonal: can be MAS or SAM

    # Get the characters for each diagonal
    top_left = grid[row-1][col-1]
    top_right = grid[row-1][col+1]
    bottom_left = grid[row+1][col-1]
    bottom_right = grid[row+1][col+1]

    # Each diagonal must form MAS or SAM
    valid_patterns = {
        ('M', 'S'),  # MAS from top to bottom
        ('S', 'M')   # SAM from top to bottom
    }

    # Check if either diagonal forms a valid pattern
    left_diagonal = (top_left, bottom_right)
    right_diagonal = (top_right, bottom_left)

    return (left_diagonal in valid_patterns and
            right_diagonal in valid_patterns)

def count_xmas_patterns(grid: list) -> int:
    """
    Count all valid X-MAS patterns in the grid.
    """
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Check each position as potential center of X
    for row in range(1, rows-1):
        for col in range(1, cols-1):
            if check_xmas_pattern(grid, row, col):
                count += 1

    return count

def read_input(filename: str) -> list:
    """
    Read and parse the word search grid from input file.
    """
    try:
        with open(filename, 'r') as file:
            return [list(line.strip()) for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: Input file '{filename}' not found")
        return []

def test_example():
    """
    Test with the example from the problem description.
    """
    example = [
        ".M.S......",
        "..A..MSMS.",
        ".M.S.MAA..",
        "..A.ASMSM.",
        ".M.S.M....",
        "..........",
        "S.S.S.S.S.",
        ".A.A.A.A..",
        "M.M.M.M.M.",
        ".........."
    ]
    grid = [list(line) for line in example]
    result = count_xmas_patterns(grid)
    print(f"Example test result: {result}")  # Should be 9
    return result == 9

def main():
    """
    Main function to execute the program.
    """
    # Test the example first
    if not test_example():
        print("Example test failed!")
        return

    # Process actual input
    INPUT_FILE = "day4_input.txt"
    grid = read_input(INPUT_FILE)

    if not grid:
        return

    result = count_xmas_patterns(grid)
    print(f"Number of X-MAS patterns: {result}")
    print(f"Grid dimensions: {len(grid)}x{len(grid[0])}")

if __name__ == '__main__':
    main()
