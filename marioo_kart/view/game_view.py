
# Kart-Engine v2.3

import pygame

from constants import (
    WINDOW_WIDTH,
    TILE_SIZE,
    CAR_WIDTH,
    CAR_HEIGHT,
    COLOR_BG,
    COLOR_TEXT,
    COLOR_ACCENT,
    COLOR_PANEL,
    COLOR_PANEL_BORDER,
    GameState
)

from model.game_model import GameModel
from model.car import Car


class GameView:
    """
    Gère l'affichage graphique du jeu.

    Dessine le menu, le circuit et les deux voitures
    à partir des données du modèle.
    """

    def __init__(self, screen: pygame.Surface) -> None:
        """
        Initialise les éléments graphiques.
        """
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 24)

        # Création de la surface du circuit
        self._tile_surface = self._build_tile_surface()

        # Cache des sprites des voitures selon leur couleur
        self._car_surfaces = {}

    def draw(self, model: GameModel) -> None:
        """
        Affiche le jeu selon son état actuel.
        """
        self.screen.fill(COLOR_BG)

        if model.state == GameState.MENU:
            self._draw_menu(model)

        elif model.state == GameState.RACING:
            self._draw_racing(model)

        pygame.display.flip()

    def _draw_menu(self, model: GameModel) -> None:
        """
        Dessine le menu principal.
        """
        cx = WINDOW_WIDTH // 2

        title_surf = self.font.render(
            "Jeu de course 2D", True, COLOR_ACCENT
        )

        self.screen.blit(
            title_surf,
            title_surf.get_rect(center=(cx, 160))
        )

        options = [
            ("JOUER (Enter)", GameState.RACING),
            ("QUITTER (Escape)", None)
        ]

        for i, (label, _) in enumerate(options):
            y = 320 + i * 80

            rect = pygame.Rect(cx - 140, y - 25, 280, 50)

            pygame.draw.rect(
                self.screen,
                COLOR_PANEL,
                rect,
                border_radius=8
            )

            pygame.draw.rect(
                self.screen,
                COLOR_PANEL_BORDER,
                rect,
                2,
                border_radius=8
            )

            text_surf = self.font.render(
                label,
                True,
                COLOR_ACCENT if i == 0 else COLOR_TEXT
            )

            self.screen.blit(
                text_surf,
                text_surf.get_rect(center=rect.center)
            )

    def _draw_racing(self, model: GameModel) -> None:
        """
        Dessine le circuit et les deux voitures.
        """
        if model.circuit is None:
            return

        # Affichage des cases du circuit
        for row_idx, row in enumerate(model.circuit.grid):
            for col_idx, tile in enumerate(row):

                self.screen.blit(
                    self._tile_surface,
                    (col_idx * TILE_SIZE, row_idx * TILE_SIZE)
                )

        # Affichage des deux voitures
        for car in (model.car1, model.car2):
            if car is not None:
                self._draw_car(car)

    def _draw_car(self, car: Car) -> None:
        """
        Dessine une voiture avec sa couleur
        et son orientation.
        """
        color = car.color

        # Créer le sprite uniquement si nécessaire
        if color not in self._car_surfaces:
            self._car_surfaces[color] = (
                self._build_car_surface(color)
            )

        sprite = self._car_surfaces[color]

        # Rotation selon l'orientation
        rotated = pygame.transform.rotate(
            sprite, -car.angle
        )

        # Centrage sur la position de la voiture
        rect = rotated.get_rect(
            center=(int(car.x), int(car.y))
        )

        self.screen.blit(rotated, rect)

    def _build_car_surface(
        self,
        color: tuple[int, int, int]
    ) -> pygame.Surface:
        """
        Crée le sprite rectangulaire d'une voiture.
        """
        surf = pygame.Surface(
            (CAR_WIDTH, CAR_HEIGHT),
            pygame.SRCALPHA
        )

        pygame.draw.rect(
            surf,
            color,
            surf.get_rect(),
            border_radius=5
        )

        return surf

    def _build_tile_surface(self) -> pygame.Surface:
        """
        Crée la représentation graphique
        d'une case du circuit.
        """
        surface = pygame.Surface(
            (TILE_SIZE, TILE_SIZE)
        )

        surface.fill((80, 80, 90))

        pygame.draw.rect(
            surface,
            (60, 60, 70),
            surface.get_rect(),
            2
        )

        return surface
