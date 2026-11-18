import pygame
import math
from constants import (
    CAR_ACCELERATION, CAR_WIDTH, CAR_HEIGHT, TILE_SIZE
)


class Car:
    """
    Représente une voiture du jeu.

    Gère sa position, sa vitesse, son orientation
    et son apparence graphique.
    """

    def __init__(self, start_col: int, start_row: int):
        self.x = start_col * TILE_SIZE + TILE_SIZE // 2
        self.y = start_row * TILE_SIZE + TILE_SIZE // 2
        self.speed: float = 0.0
        self.angle: float = 0.0

    def accelerate(self) -> None:
        """
        Augmente la vitesse de la voiture.

        Ajoute la valeur CAR_ACCELERATION à la vitesse actuelle.
        """

        self.speed += CAR_ACCELERATION

    def brake(self) -> None:
        self.speed -= CAR_ACCELERATION

    def update_position(self) -> None:
        """
        Met à jour la position verticale de la voiture.

        Ajoute la vitesse actuelle à la coordonnée y.
        """
        
        self.y += self.speed
