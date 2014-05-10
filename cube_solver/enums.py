from enum import Enum


class Colour(Enum):
    White = 3
    Red = 4
    Blue = 0
    Yellow = 1
    Orange = 2
    Green = 5


class Edge(Enum):
    BOTTOM = ((2, 0), (2, 1), (2, 2))
    LEFT = ((0, 0), (1, 0), (2, 0))
    RIGHT = ((0, 2), (1, 2), (2, 2))
    TOP = ((0, 0), (0, 1), (0, 2))

    def __init__(self, *coordinates):
        self.coordinates = coordinates

    def __call__(self, ascending_indices=True):
        return (lambda i:
                self.coordinates[i] if ascending_indices else self.coordinates[2 - i])