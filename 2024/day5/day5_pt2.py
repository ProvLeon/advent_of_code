"""
Advent of Code 2024 - Day 5 Part 2
Fix incorrectly ordered sequences and find middle numbers.
"""

from collections import defaultdict

def build_dependency_graph(rules: list) -> dict:
    """
    Build a directed graph of page dependencies.

    Args:
        rules (list): List of rules in format "X|Y"

    Returns:
        dict: Graph where key is page number and value is set of pages that must come after it
    """
    graph = defaultdict(set)

    for rule in rules:
        before, after = map(int, rule.strip().split('|'))
        graph[before].add(after)

    return graph

def topological_sort(pages: list, graph: dict) -> list:
    """
    Sort pages according to dependencies using topological sort.

    Args:
        pages (list): List of pages to sort
        graph (dict): Dependency graph

    Returns:
        list: Sorted list of pages
    """
    # Create graph with only relevant pages and dependencies
    relevant_graph = defaultdict(set)
    pages_set = set(pages)

    for page in pages:
        if page in graph:
            # Only include dependencies between pages in this sequence
            relevant_graph[page] = {p for p in graph[page] if p in pages_set}

    # Calculate in-degree for each page
    in_degree = defaultdict(int)
    for deps in relevant_graph.values():
        for page in deps:
            in_degree[page] += 1

    # Initialize queue with pages that have no dependencies
    queue = [p for p in pages if in_degree[p] == 0]
    result = []

    # Process queue
    while queue:
        page = queue.pop(0)
        result.append(page)

        # Update dependencies
        for dep in relevant_graph[page]:
            in_degree[dep] -= 1
            if in_degree[dep] == 0:
                queue.append(dep)

    # If not all pages are included, there's a cycle
    if len(result) != len(pages):
        return []

    return result

def is_valid_order(pages: list, graph: dict) -> bool:
    """
    Check if a sequence of pages is in valid order.

    Args:
        pages (list): List of page numbers
        graph (dict): Dependency graph

    Returns:
        bool: True if order is valid, False otherwise
    """
    pages_set = set(pages)

    for i, page in enumerate(pages):
        if page in graph:
            for following in graph[page]:
                if following in pages_set:
                    following_idx = pages.index(following)
                    if following_idx < i:
                        return False

    return True

def get_middle_page(pages: list) -> int:
    """
    Get the middle page from a sequence.

    Args:
        pages (list): List of pages

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
        tuple: List of rules and list of sequences
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

    # Process invalid sequences
    total = 0
    invalid_count = 0

    for seq in sequences:
        if not is_valid_order(seq, graph):
            # Sort invalid sequence
            sorted_seq = topological_sort(seq, graph)
            if sorted_seq:
                middle = get_middle_page(sorted_seq)
                total += middle
                invalid_count += 1
                print(f"Invalid sequence: {seq}")
                print(f"Corrected to: {sorted_seq}")
                print(f"Middle page: {middle}\n")

    print(f"\nTotal invalid sequences: {invalid_count}")
    print(f"Sum of middle pages after correction: {total}")

if __name__ == '__main__':
    main()
