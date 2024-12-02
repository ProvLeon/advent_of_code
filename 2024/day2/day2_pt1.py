"""
Advent of Code 2024 - Day 2 Part 1
This module analyzes numerical reports to determine if they are 'safe' based on specific criteria.
"""

def is_safe_report(report: list) -> bool:
    """
    Check if a report is 'safe' based on consecutive differences and direction.

    Args:
        report (list): List of integers to analyze

    Returns:
        bool: True if report meets safety criteria, False otherwise

    Safety criteria:
    1. Report must have at least 2 numbers
    2. Consecutive differences must be between 1 and 3 (inclusive)
    3. Numbers must be consistently increasing or decreasing
    """
    # Check minimum length requirement
    if len(report) <= 1:
        return False

    # Initialize lists to store differences
    abs_differences = []    # For magnitude of differences
    actual_differences = [] # For direction of differences

    # Calculate differences between consecutive numbers
    for i in range(len(report) - 1):
        difference = report[i + 1] - report[i]
        abs_differences.append(abs(difference))
        actual_differences.append(difference)

    # Check if all differences are within valid range (1-3)
    valid_range = all(1 <= diff <= 3 for diff in abs_differences)
    if not valid_range:
        return False

    # Check if numbers are consistently increasing or decreasing
    is_increasing = all(diff > 0 for diff in actual_differences)
    is_decreasing = all(diff < 0 for diff in actual_differences)

    return is_increasing or is_decreasing


def calculate_safe_reports(reports: list) -> int:
    """
    Count the number of safe reports in a list of reports.

    Args:
        reports (list): List of reports to analyze

    Returns:
        int: Count of safe reports
    """
    safe_count = 0
    for report in reports:
        if is_safe_report(report):
            safe_count += 1
    return safe_count


def read_input(filename = None, file = None) -> list:
    """
    Read and parse input data either from a file or a string.

    Args:
        filename (str, optional): Path to input file
        file (str, optional): String containing input data

    Returns:
        list: List of reports, where each report is a list of integers

    Note:
        Either filename or file must be provided, not both
    """
    list_of_reports = []

    try:
        # Handle string input
        if filename is None and file is not None:
            for line in file.split('\n'):
                cleaned_line = [int(fig) for fig in line.strip().split()]
                list_of_reports.append(cleaned_line)
        # Handle file input
        elif filename is not None:
            with open(filename, 'r') as file:
                for line in file:
                    cleaned_line = [int(fig) for fig in line.strip().split()]
                    list_of_reports.append(cleaned_line)
    except ValueError:
        print("Error: Invalid data format in input")
        return []
    except FileNotFoundError:
        print(f"Error: Input file '{filename}' not found")
        return []

    return list_of_reports


def main():
    """
    Main function to execute the program.
    """
    # Sample input string for testing
    test_input = """7 6 4 2 1
     1 2 7 8 9
     9 7 6 2 1
     1 3 2 4 5
     8 6 4 4 1
     1 3 6 7 9"""

    # Use actual input file instead of test input
    INPUT_FILE = "day2_input.txt"

    # Read reports from input file
    reports = read_input(filename=INPUT_FILE)

    # Verify input data was read successfully
    if not reports:
        return

    # Calculate and display results
    result = calculate_safe_reports(reports)
    print(f"Safe reports: {result}")


if __name__ == '__main__':
    main()
