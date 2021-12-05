import read_inputs as ri


def print_grid(grid):
    for row in grid:
        for node in row:
            print(node, end="\t")
        print()


def BFS(id):
    visited = []
    queue = []

    queue.append(id)

    while queue:
        currentNode = queue.pop(0)
        visited.append(currentNode)
        print(f"node: {currentNode}")

        # determine if at bottom right corner, "exit"
        if max_r*max_c - 1 == abs(currentNode):
            return visited

        print(f"nb: {edges[currentNode]}")
        for neighbor in edges[currentNode]:
            if neighbor not in visited:
                queue.append(neighbor)

    return visited


grid, max_r, max_c = ri.read_file_to_2dlist("./input.txt")

# print_grid(grid)
edges = ri.generate_edges_from_grid(grid)

visited = BFS(0)

# manually obtained from the file `sampleoutput.yml`
pathIDs = [0, 5, 29, 36, 43, 8, 22, 10, -38, -41, -13, -37, -45, -33, -25, -
           32, -11, -18, -39, 23, 25, 18, 4, 32, 39, 47, 7, -23, -21, -42, -24, 6, 48]

for nodeID in pathIDs:
    row = abs(nodeID) // max_r
    col = abs(nodeID) % max_c
    print(f"({row+1}, {col+1})", end=" ")
