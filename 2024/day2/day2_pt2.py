
def is_safe_report(report):
    if (len(report) <= 1):
        return False

    differences = []

    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        differences.append(diff)

    valid_range = all(1 <= abs(diff) <= 3 for diff in differences)
    if not valid_range:
        return False

    is_increasing = all(diff > 0 for diff in differences)
    is_decreasing = all(diff < 0 for diff in differences)

    return is_increasing or is_decreasing

def is_safe_with_dampener(report):
    if is_safe_report(report):
        return True

    for i in range(len(report)):
        dampened_report = report[:i] + report[i + 1:]
        if is_safe_report(dampened_report):
            return True
    return False

def calculate_report_with_dampener(reports):
    safe_count = 0
    for report in reports:
        if is_safe_with_dampener(report):
            safe_count += 1

    return safe_count

def read_input(filename=None, file=None):
    list_of_reports = []
    if filename is None and file is not None:
        for line in file.split('\n'):
            cleaned_line = [int(fig) for fig in line.split()]
            list_of_reports.append(cleaned_line)

    elif filename is not None:
        with open(filename, 'r') as filename:
            for line in filename:
                cleaned_line = [int(fig) for fig in line.split()]
                list_of_reports.append(cleaned_line)

    return list_of_reports

if __name__ == '__main__':
    file = """
    7 6 4 2 1
     1 2 7 8 9
     9 7 6 2 1
     1 3 2 4 5
     8 6 4 4 1
     1 3 6 7 9
     """

    reports = read_input(filename="day2_input.txt")
    # for report in reports:
    result = calculate_report_with_dampener(reports)
    print(result)
    # result = calculate_safe_reports(reports)
    # print(f"Safe reports: {result}")
