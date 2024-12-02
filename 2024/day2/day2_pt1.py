def is_safe_report(report):
    if len(report) <= 1:
        return False

    abs_differences, actual_differences = [], []

    for i in range(len(report) - 1):
        difference = report[i + 1] - report[i]
        abs_differences.append(abs(difference))
        actual_differences.append(difference)

    # valid_differences
    valid_range = all(1 <= diff <= 3 for diff in abs_differences)
    if not valid_range:
        return False

    # consitent_direction
    is_increasing = all(diff > 0 for diff in actual_differences)
    is_decreasing = all(diff < 0 for diff in actual_differences)

    return  is_increasing or is_decreasing



def calculate_safe_reports(reports):
    safe_count = 0
    for report in reports:
        if is_safe_report(report):
            safe_count += 1
    return safe_count


def read_input(filename=None, file=None):
    list_of_reports = []
    if filename is None and file is not None:
        for line in file.split('\n'):
            cleaned_line = [int(fig) for fig in line.strip().split()]
            list_of_reports.append(cleaned_line)
    elif filename is not None:
        with open(filename, 'r') as file:
            for line in file:
                cleaned_line = [int(fig) for fig in line.strip().split()]
                list_of_reports.append(cleaned_line)

    return list_of_reports

if __name__ == '__main__':
    file = """7 6 4 2 1
     1 2 7 8 9
     9 7 6 2 1
     1 3 2 4 5
     8 6 4 4 1
     1 3 6 7 9"""

    reports = read_input(filename="day2_input.txt")
    result = calculate_safe_reports(reports)
    print(f"Safe reports: {result}")
