def steps_to_farthest_point(sketch):
    rows = len(sketch)
    cols = len(sketch[0])

    directions = {'-': [(0, 1), (0, -1)], '|': [(1, 0), (-1, 0)], 'L': [(-1, 0), (0, -1)], 'J': [(-1, 0), (0, 1)],
                  '7': [(1, 0), (0, -1)], 'F': [(1, 0), (0, 1)], '.': [], 'S': [(1, 0), (-1, 0), (0, 1), (0, -1)]}

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    # Function to perform DFS to identify the loop and calculate distances
    def dfs(x, y, visited, distance):
        visited[x][y] = True
        max_distance = distance

        for dx, dy in directions[sketch[x][y]]:
            nx, ny = x + dx, y + dy

            if is_valid(nx, ny) and not visited[nx][ny]:
                max_distance = max(max_distance, dfs(nx, ny, visited, distance + 1))

        return max_distance

    # Find the starting position 'S'
    start_x, start_y = None, None
    for i in range(rows):
        for j in range(cols):
            if sketch[i][j] == 'S':
                start_x, start_y = i, j
                break

    if start_x is not None and start_y is not None:
        # Initialize visited matrix
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        # Calculate distances using DFS
        max_distance = dfs(start_x, start_y, visited, 0)

        return max_distance

    return -1  # Invalid input or 'S' not found

# Read input from a local file
file_path = 'input.txt'  # Replace 'input.txt' with your file name
with open(file_path, 'r') as file:
    sketch = [line.strip() for line in file.readlines()]

result = steps_to_farthest_point(sketch)
if result != -1:
    print("Number of steps along the loop to farthest point:", result)
else:
    print("Invalid input or 'S' not found in the sketch.")
