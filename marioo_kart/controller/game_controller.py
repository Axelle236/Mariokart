
# Kart-Engine v2.3

import pygame
import sys

from constants import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    FPS,
    GameState
)

from model.game_model import GameModel
from view.game_view import GameView
from controller.input_handler import InputHandler


class GameController:
    """
    Contrôle le déroulement du jeu.

    Gère les événements du clavier, les commandes des joueurs,
    la mise à jour du modèle et l'affichage.
    """

    def __init__(self) -> None:
        """
        Initialise la fenêtre et les composants du jeu.
        """
        self.screen = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT),
            pygame.SCALED | pygame.RESIZABLE
        )

        self.clock = pygame.time.Clock()
        self.model = GameModel()
        self.view = GameView(self.screen)
        self.input_handler = InputHandler()
        self.running = True

    def run(self) -> None:
        """
        Exécute la boucle principale du jeu.
        """
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)

    def handle_events(self) -> None:
        """
        Traite les événements reçus par Pygame.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            elif event.type == pygame.KEYDOWN:
                self.handle_keydown(event.key)

    def handle_keydown(self, key: int) -> None:
        """
        Traite une touche selon l'état actuel du jeu.
        """
        if self.model.state == GameState.MENU:
            self.handle_menu_key(key)

    def handle_menu_key(self, key: int) -> None:
        """
        Gère les commandes du menu principal.

        Entrée : démarre la course.
        Échap : quitte le jeu.
        """
        if key == pygame.K_RETURN:
            self.model.start_race()

        elif key == pygame.K_ESCAPE:
            self.quit()

    def update(self) -> None:
        """
        Récupère les commandes des deux joueurs
        et les transmet au modèle.
        """
        if self.model.state != GameState.RACING:
            return

        # Récupération des commandes des deux joueurs
        p1_input, p2_input = self.input_handler.get_inputs()

        # Commandes de la première voiture
        self.model.handle_player_input(
            self.model.car1,
            p1_input
        )

        # Commandes de la deuxième voiture
        self.model.handle_player_input(
            self.model.car2,
            p2_input
        )

        # Actualisation des positions
        self.model.update()

    def render(self) -> None:
        """
        Transmet le modèle à la vue pour actualiser
        l'affichage du jeu.
        """
        self.view.draw(self.model)

    def quit(self) -> None:
        """
        Arrête la boucle principale et ferme Pygame.
        """
        self.running = False
        pygame.quit()
        sys.exit()
