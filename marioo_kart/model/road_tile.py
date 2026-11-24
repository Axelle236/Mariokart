import pygame
from constants import TILE_SIZE


class RoadTile:
    """
    Représente une case du circuit.

    Chaque case possède une position et un type de terrain.
    """

    def __init__(
        self,
        col: int,
        row: int,
        terrain: str = "road"
    ) -> None:

        self.col = col
        self.row = row
        self.terrain = terrain