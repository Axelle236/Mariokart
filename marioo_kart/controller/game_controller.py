# Kart-Engine v2.3

import pygame
import sys

from constants import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    FPS,
    GameState
)

from model.car import Car
from model.game_model import GameModel
from view.game_view import GameView
from controller.input_handler import InputHandler


class GameController:
    """
    Contrôle le déroulement du jeu.

    Gère les événements du clavier, les actions des joueurs,
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

        Ferme le jeu si l'utilisateur quitte la fenêtre
        et transmet les touches pressées à handle_keydown().
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
        state = self.model.state

        if state == GameState.MENU:
            self.handle_menu_key(key)

    def handle_menu_key(self, key: int) -> None:
        """
        Gère les commandes du menu principal.

        Entrée : démarre la course.
        Échap : quitte le jeu.
        """
        if key == pygame.K_RETURN:
            self.model.load_circuit()
            self.model.state = GameState.RACING

        elif key == pygame.K_ESCAPE:
            self.quit()

    def update(self) -> None:
        """
        Récupère les commandes des deux joueurs
        et met à jour le modèle pendant la course.
        """
        if self.model.state != GameState.RACING:
            return

        p1_input, p2_input = self.input_handler.get_inputs()

        if self.model.car1 is not None:
            self.apply_input(self.model.car1, p1_input)

        if self.model.car2 is not None:
            self.apply_input(self.model.car2, p2_input)

        self.model.update()

    def apply_input(
        self,
        car: Car,
        player_input: dict[str, bool]
    ) -> None:
        """
        Applique les commandes du joueur à sa voiture.

        Paramètres :
        car : voiture à contrôler.
        player_input : dictionnaire des actions du joueur.
        """
        if player_input["accelerate"]:
            car.accelerate()

        if player_input["brake"]:
            car.brake()

        if not player_input["accelerate"] and not player_input["brake"]:
            car.decelerate()

        if player_input["left"]:
            car.turn_left()

        if player_input["right"]:
            car.turn_right()

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