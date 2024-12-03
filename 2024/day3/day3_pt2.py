

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


if __name__ == "__main__":
    main()
