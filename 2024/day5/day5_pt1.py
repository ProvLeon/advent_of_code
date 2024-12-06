"""
Advent of Code 2024 - Day 5 Part 1
Validate print orders and find middle page numbers of valid sequences.
"""

def build_dependency_graph(rules: list) -> dict:
    """
    Build a directed graph of page dependencies.

    Args:
        rules (list): List of rules in format "X|Y"

    Returns:
        dict: Graph where key is page number and value is set of pages that must come after it
    """
    graph = {}

    for rule in rules:
        before, after = map(int, rule.strip().split('|'))
        # Add pages to graph if not present
        if before not in graph:
            graph[before] = set()
        if after not in graph:
            graph[after] = set()
        # Add dependency
        graph[before].add(after)

    return graph

def is_valid_order(pages: list, graph: dict) -> bool:
    """
    Check if a sequence of pages is in valid order according to dependencies.

    Args:
        pages (list): List of page numbers in order
        graph (dict): Dependency graph

    Returns:
        bool: True if order is valid, False otherwise
    """
    # Convert pages to set for quick lookup
    pages_set = set(pages)

    # Check each pair of pages in sequence
    for i, page in enumerate(pages):
        if page in graph:
            # Get all pages that must come after current page
            must_follow = graph[page]
            # Check if any of these pages appear before current page
            for following in must_follow:
                if following in pages_set:  # Only check pages that exist in this sequence
                    following_idx = pages.index(following)
                    if following_idx < i:  # If a page that should follow appears before
                        return False

    return True

def get_middle_page(pages: list) -> int:
    """
    Get the middle page number from a sequence.

    Args:
        pages (list): List of page numbers

    Returns:
        int: Middle page number
    """
    return pages[len(pages) // 2]

def read_input(filename: str) -> tuple[list, list]:
    """
    Read and parse input file.

    Args:
        filename (str): Input file name

    Returns:
        tuple: List of rules and list of page sequences
    """
    rules = []
    sequences = []
    reading_rules = True

    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    reading_rules = False
                    continue

                if reading_rules:
                    rules.append(line)
                else:
                    sequences.append([int(x) for x in line.split(',')])
    except FileNotFoundError:
        print(f"Error: Input file '{filename}' not found")
        return [], []

    return rules, sequences

def main():
    """
    Main function to execute the program.
    """
    # Read input
    INPUT_FILE = "day5_input.txt"
    rules, sequences = read_input(INPUT_FILE)

    if not rules or not sequences:
        return

    # Build dependency graph
    graph = build_dependency_graph(rules)

    # Process sequences and sum middle pages of valid sequences
    total = 0
    valid_count = 0

    for seq in sequences:
        if is_valid_order(seq, graph):
            middle = get_middle_page(seq)
            total += middle
            valid_count += 1
            print(f"Valid sequence: {seq}, middle page: {middle}")

    print(f"\nTotal valid sequences: {valid_count}")
    print(f"Sum of middle pages: {total}")

if __name__ == '__main__':
    main()
