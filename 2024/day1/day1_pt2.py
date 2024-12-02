from collections import Counter

def calculate_similarity_score(left_list, right_list):
    right_frequencies = Counter(right_list)
    print(right_frequencies)

    total_score = 0
    for num in left_list:
        total_score += num * right_frequencies.get(num, 0)

    return total_score

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
    result = calculate_similarity_score(left_list, right_list)
    print(f"Similarity Score: {result}")
