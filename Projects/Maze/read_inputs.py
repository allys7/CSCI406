from typing import List
from node import Color, Direction, Node
import networkx as nx


def read_file_to_2dlist(file: str):
    with open(file, "r") as f:
        # get size of grid from first line
        line = f.readline()
        sizes = line.split()
        global max_r, max_c
        max_r, max_c = int(sizes[0]), int(sizes[1])
        global grid
        grid = [ [None]*max_c for _ in range(max_r)]

        while True:
            line = f.readline()

            # break when empty
            if not line:
                break

            r, c, color, circ, dir = line.split()

            r = int(r) - 1
            c = int(c) - 1

            if color == "B":
                color = Color.BLUE
            elif color == "R":
                color = Color.RED
            else:
                color = Color.NONE
            
            if circ == "C":
                circ = True
            else:
                circ = False

            if dir == "N":
                dir = Direction.N
            elif dir == "NE":
                dir = Direction.NE
            elif dir == "E":
                dir = Direction.E
            elif dir == "SE":
                dir = Direction.SE
            elif dir == "S":
                dir = Direction.S
            elif dir == "SW":
                dir = Direction.SW
            elif dir == "W":
                dir = Direction.W
            elif dir == "NW":
                dir = Direction.NW
            node = Node(dir=dir, circ=circ, color=color, pos=(r,c))
            grid[r][c] = node
        return grid

def in_bounds(row: int, col: int) -> bool:
    return (row < max_r and row >= 0) and (col < max_c and col >= 0)

def nodeID(row: int, col:int) -> int:
    return (max_r * row + col)

def generate_forward_edges(node: Node) -> None:
    startRow, startCol = node.row, node.col

    if (node.direction == Direction.N):
        deltaRow, deltaCol = -1,0
    elif (node.direction == Direction.NE):
        deltaRow, deltaCol = -1, 1
    elif (node.direction == Direction.E):
        deltaRow, deltaCol = 0, 1
    elif (node.direction == Direction.SE):
        deltaRow, deltaCol = 1, 1
    elif (node.direction == Direction.S):
        deltaRow, deltaCol = 1, 0
    elif (node.direction == Direction.SW):
        deltaRow, deltaCol = 1, -1
    elif (node.direction == Direction.W):
        deltaRow, deltaCol = 0, -1
    elif (node.direction == Direction.NW):
        deltaRow, deltaCol = -1, -1
    else:
        return

    currentRow, currentCol = startRow+deltaRow, startCol+deltaCol
    
    while(in_bounds(row=currentRow, col=currentCol)):
        temp_node = grid[currentRow][currentCol]
        if node.color != temp_node.color:
            id1 = nodeID(startRow, startCol)
            id2 = nodeID(currentRow, currentCol)
            G_forward.add_edge(id1, id2)
        currentRow += deltaRow
        currentCol += deltaCol
    return

def generate_backward_edges(node: Node) -> None:
    startRow, startCol = node.row, node.col

    if (node.direction == Direction.N):
        deltaRow, deltaCol = 1,0
    elif (node.direction == Direction.NE):
        deltaRow, deltaCol = 1, -1
    elif (node.direction == Direction.E):
        deltaRow, deltaCol = 0, -1
    elif (node.direction == Direction.SE):
        deltaRow, deltaCol = -1, -1
    elif (node.direction == Direction.S):
        deltaRow, deltaCol = -1, 0
    elif (node.direction == Direction.SW):
        deltaRow, deltaCol = -1, 1
    elif (node.direction == Direction.W):
        deltaRow, deltaCol = 0, 1
    elif (node.direction == Direction.NW):
        deltaRow, deltaCol = 1, 1
    else:
        return

    currentRow, currentCol = startRow+deltaRow, startCol+deltaCol
    
    while(in_bounds(row=currentRow, col=currentCol)):
        temp_node = grid[currentRow][currentCol]
        if node.color != temp_node.color:
            id1 = nodeID(startRow, startCol)
            id2 = nodeID(currentRow, currentCol)
            G_backward.add_edge(id1, id2)
        currentRow += deltaRow
        currentCol += deltaCol
    return

def generate_graph_from_grid(grid: List) -> nx.DiGraph:
    global G_forward, G_backward
    G_forward = nx.DiGraph()
    G_backward = nx.DiGraph()
    nodeID = 0

    # create nodes
    for row in grid:
        for node in row:
            G_forward.add_node(nodeID)
            G_backward.add_node(nodeID)
            nodeID += 1

    # create edges
    for row in grid:
        for node in row:
            generate_forward_edges(node)
            generate_backward_edges(node)
            # print(G.edges())

    return G_forward, G_backward
