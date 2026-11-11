import pygame
from constants import TILE_SIZE


class RoadTile:
    """
    Représente une case du circuit.

    Fournit les informations et l'image nécessaires
    pour représenter cette case.
    """

    def __init__(self, col: int, row: int):
        self.col = col
        self.row = row
        self.sprite: pygame.Surface | None = None

    def get_sprite(self, tile_size: int = TILE_SIZE) -> pygame.Surface:
        """
        Retourne l'image représentant une case de route.

        Crée la surface graphique lors du premier appel
        puis la réutilise pour les affichages suivants.
        """
        if self.sprite and self.sprite.get_width() == tile_size:
            return self.sprite
        surface = pygame.Surface((tile_size, tile_size))
        surface.fill((80, 80, 90))
        pygame.draw.rect(surface, (60, 60, 70), surface.get_rect(), 2)

        self.sprite = surface
        return self.sprite
