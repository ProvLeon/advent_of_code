"""
Advent of Code 2024 - Day 1 Part 1
This module calculates the total distance between corresponding pairs of numbers
from two lists after sorting them.
"""

def calculate_total_distance(left_list: list, right_list: list) -> int:
    """
    Calculate the total distance between corresponding elements of two sorted lists.

    Args:
        left_list (list): First list of integers
        right_list (list): Second list of integers

    Returns:
        int: Sum of absolute differences between corresponding elements

    Note:
        Lists are sorted before calculation to ensure proper pairing
    """
    # Sort both lists in ascending order
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)

    # Initialize total distance counter
    total_distance = 0

    # Iterate through both lists simultaneously and calculate differences
    for left, right in zip(left_sorted, right_sorted):
        total_distance += abs(left - right)

    return total_distance


def read_input(filename: str) -> tuple[list, list]:
    """
    Read input data from a file and parse into two separate lists.

    Args:
        filename (str): Path to the input file

    Returns:
        tuple[list, list]: Two lists containing the left and right values

    Note:
        Input file should contain two space-separated integers per line
    """
    left_list = []
    right_list = []

    try:
        with open(filename, 'r') as file:
            for line in file:
                # Split each line into two integers and append to respective lists
                left, right = map(int, line.strip().split())
                left_list.append(left)
                right_list.append(right)

    except FileNotFoundError:
        print(f"Error: Input file '{filename}' not found")
        return [], []
    except ValueError:
        print("Error: Invalid data format in input file")
        return [], []

    return left_list, right_list


def main():
    """
    Main function to execute the program.
    """
    INPUT_FILE = 'day1_input.txt'

    # Read input data
    left_list, right_list = read_input(INPUT_FILE)

    # Verify input data was read successfully
    if not left_list or not right_list:
        return

    # Calculate and display result
    result = calculate_total_distance(left_list, right_list)
    print(f"Total distance: {result}")


if __name__ == '__main__':
    main()
