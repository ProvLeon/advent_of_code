"""
Advent of Code 2024 - Day 3 Part 1
Find and calculate valid multiplication instructions in corrupted memory.
"""
import re

def find_valid_multiplications(text: str) -> list:
    """
    Find all valid multiplication instructions in the text.

    Args:
        text (str): Input text containing corrupted memory

    Returns:
        list: List of tuples containing valid multiplication pairs
    """
    # Pattern for valid multiplication: mul(X,Y) where X and Y are 1-3 digits
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

    # Find all matches
    matches = re.findall(pattern, text)
    # print all matches
    # print(matches) # Uncomment to see all matches

    # Extract and convert numbers to integers
    multiplications = []
    for match in matches:
        x, y = int(match[0]), int(match[1])
        multiplications.append((x, y))
    return multiplications

def calculate_total(multiplications: list) -> int:
    """
    Calculate the sum of all multiplication results.

    Args:
        multiplications (list): List of tuples containing number pairs

    Returns:
        int: Sum of all multiplication results
    """
    # total = 0
    # for x, y in multiplications:
    #     total += x * y
    # return total
    return sum(x * y for x, y in multiplications)


def read_input(filename):
    """
    Read the input file.

    Args:
        filename (str): Name of input file

    Returns:
        str: Content of input file
    """
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return ""


def main():
    """
    Main function to execute the program
    """
    # Read input file
    INPUT_FILE = "day3_input.txt"
    content = read_input(filename=INPUT_FILE)

    if not content:
        return

    # Find all valid multiplications
    multiplications = find_valid_multiplications(content)

    # Calculate  and print sum total of all valid multiplications (result)
    result = calculate_total(multiplications)
    print(f"Sum of all multiplication results: {result}")

    # for Debugging
    print(f"Found {len(multiplications)} valid multiplications")
    # Uncomment to see all valid multiplications
    # for x, y in multiplications:
    #     print(f"{x}, {y} = {x*y}")

if __name__ == '__main__':
    main()
