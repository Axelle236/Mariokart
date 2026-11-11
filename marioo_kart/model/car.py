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
        self.sprite = self.build_sprite()

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

    def build_sprite(self) -> pygame.Surface:
        surf = pygame.Surface((CAR_WIDTH, CAR_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(surf, (255, 0, 0), (0, 0, CAR_WIDTH,
                         CAR_HEIGHT), border_radius=5)
        return surf

    def get_rotated_sprite(self) -> tuple[pygame.Surface, pygame.Rect]:
        """
        Récupère l'image de la voiture selon son orientation.

        Retourne la surface tournée et son rectangle
        centré sur la position actuelle de la voiture.
        """
        
        rotated = pygame.transform.rotate(self.sprite, -self.angle)
        rect = rotated.get_rect(center=(int(self.x), int(self.y)))
        return rotated, rect
