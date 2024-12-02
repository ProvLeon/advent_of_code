"""
Advent of Code 2024 - Day 2 Part 2
This module analyzes numerical reports to determine if they are 'safe' with an optional dampener,
which allows removing one number to make an unsafe report safe.
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
    2. Consecutive differences must be between 1 and 3 (absolute value)
    3. Numbers must be consistently increasing or decreasing
    """
    # Check minimum length requirement
    if len(report) <= 1:
        return False

    # Calculate differences between consecutive numbers
    differences = []
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        differences.append(diff)

    # Check if all differences are within valid range (1-3)
    valid_range = all(1 <= abs(diff) <= 3 for diff in differences)
    if not valid_range:
        return False

    # Check if numbers are consistently increasing or decreasing
    is_increasing = all(diff > 0 for diff in differences)
    is_decreasing = all(diff < 0 for diff in differences)

    return is_increasing or is_decreasing


def is_safe_with_dampener(report: list) -> bool:
    """
    Check if a report is safe or can be made safe by removing one number.

    Args:
        report (list): List of integers to analyze

    Returns:
        bool: True if report is safe or can be made safe with dampener

    Note:
        Dampener allows removing one number to make an unsafe report safe
    """
    # First check if report is already safe without dampener
    if is_safe_report(report):
        return True

    # Try removing each number one at a time to see if it makes the report safe
    for i in range(len(report)):
        dampened_report = report[:i] + report[i + 1:]
        if is_safe_report(dampened_report):
            return True
    return False


def calculate_report_with_dampener(reports: list) -> int:
    """
    Count the number of reports that are safe or can be made safe with dampener.

    Args:
        reports (list): List of reports to analyze

    Returns:
        int: Count of safe reports (including those made safe with dampener)
    """
    safe_count = 0
    for report in reports:
        if is_safe_with_dampener(report):
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
                cleaned_line = [int(fig) for fig in line.split()]
                list_of_reports.append(cleaned_line)
        # Handle file input
        elif filename is not None:
            with open(filename, 'r') as file:
                for line in file:
                    cleaned_line = [int(fig) for fig in line.split()]
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
    test_input = """
    7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9
    """

    # Use actual input file instead of test input
    INPUT_FILE = "day2_input.txt"

    # Read reports from input file
    reports = read_input(filename=INPUT_FILE)

    # Verify input data was read successfully
    if not reports:
        return

    # Calculate and display results
    result = calculate_report_with_dampener(reports)
    print(f"Safe reports (with dampener): {result}")


if __name__ == '__main__':
    main()
