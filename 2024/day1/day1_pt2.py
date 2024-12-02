"""
Advent of Code 2024 - Day 1 Part 2
This module calculates a similarity score between two lists based on frequency matching.
"""

from collections import Counter

def calculate_similarity_score(left_list: list, right_list: list) -> int:
    """
    Calculate similarity score based on frequency matching between two lists.

    Args:
        left_list (list): First list of integers
        right_list (list): Second list of integers

    Returns:
        int: Total similarity score calculated by multiplying numbers with their frequencies

    Note:
        Score is calculated by multiplying each number in left_list with its frequency in right_list
    """
    # Count frequencies of numbers in right list
    right_frequencies = Counter(right_list)

    # Initialize total score
    total_score = 0

    # Calculate score by multiplying each number with its frequency
    for num in left_list:
        # Get frequency of current number (default 0 if not found)
        frequency = right_frequencies.get(num, 0)
        total_score += num * frequency

    return total_score


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

    # Print input lists for debugging
    print(f"Left list: {left_list}")
    print(f"Right list: {right_list}")

    # Calculate and display similarity score
    result = calculate_similarity_score(left_list, right_list)
    print(f"Similarity Score: {result}")


if __name__ == '__main__':
    main()
