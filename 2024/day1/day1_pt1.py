def calculate_total_distance(left_list, right_list):
    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)

    # Initialize total distance
    total_distance = 0

    # Calculate difference between corresponsing pairs
    for left, right in zip(left_sorted, right_sorted):
        total_distance += abs(left - right)

    return total_distance


def read_input(filename):
    left_list = []
    right_list = []

    with open(filename, 'r') as file:
        for line in file:
            left, right =  map(int, line.strip().split())
            left_list.append(left)
            right_list.append(right)
            # print(left, right)
    return left_list, right_list

if __name__ == '__main__':
    left_list, right_list = read_input('day1_input.txt')
    print(left_list,right_list)
    result = calculate_total_distance(left_list, right_list)
    print(f"Total distance: {result}")
