from enum import Enum
from typing import Tuple


class Direction(Enum):
    NONE = 0
    N = 1
    NE = 2
    E = 3
    SE = 4
    S = 5
    SW = 6
    W = 7
    NW = 8


class Color(Enum):
    NONE = 0
    RED = 1
    BLUE = 2


class Node:
    def __init__(self, dir: Direction, circ: bool, color: Color, pos: Tuple):
        self.direction = dir
        self.circled = circ
        self.row = pos[0]
        self.col = pos[1]
        self.color = color

    def __repr__(self) -> str:
        results = "[D: "
        if (self.direction == Direction.N):
            results += "N"
        elif (self.direction == Direction.NE):
            results += "NE"
        elif (self.direction == Direction.E):
            results += "E"
        elif (self.direction == Direction.SE):
            results += "SE"
        elif (self.direction == Direction.S):
            results += "S"
        elif (self.direction == Direction.SW):
            results += "SW"
        elif (self.direction == Direction.W):
            results += "W"
        elif (self.direction == Direction.NW):
            results += "NW"
        else:
            results += "__"

        results += ", C?: "
        if (self.circled):
            results += "Y"
        else:
            results += "N"

        results += ", Col: "
        if (self.color == Color.RED):
            results += "R"
        elif self.color == Color.BLUE:
            results += "B"
        else:
            results += "__"

        results += f", ({self.row}, {self.col})]"
        return results