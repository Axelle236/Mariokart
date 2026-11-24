import pygame
from constants import TILE_SIZE


class RoadTile:
    """
    Représente une case du circuit.

    Fournit les informations et l'image nécessaires
    pour représenter cette case.
    """

    def __init__(self, col: int, row: int, kind: str):
        self.col = col
        self.row = row
        self.kind=kind
        