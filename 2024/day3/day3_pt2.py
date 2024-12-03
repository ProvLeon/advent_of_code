import re

def find_valid_instructions(text: str) -> list:
    """
    Find all valid instructions in the text.

    Args:
        text (str): Input text containing corrupted memory

    Returns:
        list: List of tuples containing valid instructions with their positions in this format (instruction, position, x, y)
    """
    # Pattern for valid multiplication: mul(X,Y) where X and Y are 1-3 digits
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

    # Pattern for valid instructions: do() and dont()
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'

    # Get all instructions with their respective positions in the text
    instructions = []

    # Find all matches
    # matches = re.findall(mul_pattern, text)

    # Find all multiplications
    for match in re.finditer(mul_pattern, text):
        x, y = map(int, match.groups())
        instructions.append(('mul', match.start(), x, y))

    # Find all do() instructions
    for match in re.finditer(do_pattern, text):
        instructions.append(('do', match.start()))

    # Find all don't() instructions
    for match in re.finditer(dont_pattern, text):
        instructions.append(('dont', match.start()))

    # print all matches
    # print(matches) # Uncomment to see all matches

    # Extract and convert numbers to integers
    # multiplications = []
    # for match in matches:
    #     x, y = int(match[0]), int(match[1])
    #     multiplications.append((x, y))
    instructions.sort(key=lambda x: x[1])
    # print(instructions)
    return instructions

def calculate_sum_of_enabled_multiplications(instructions: list) -> int:
    """
    Calculate the sum of all enabled multiplication results.

    Args:
        instructions (list): List of tuples containing instructions

    Returns:
        int: Sum of all enabled multiplication results
    """
    # Process instructions
    # Multiplications are enabled at start
    enabled = True
    total = 0

    for instruction in instructions:
        if instruction[0] == 'mul' and enabled:
            total += instruction[2] * instruction[3]
        elif instruction[0] == 'do':
            enabled = True
        elif instruction[0] == 'dont':
            enabled = False
    return total

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
    instructions = find_valid_instructions(content)
    total = calculate_sum_of_enabled_multiplications(instructions)
    print(total)


if __name__ == "__main__":
    main()
