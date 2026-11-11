import pygame
import sys
from constants import (
    WINDOW_WIDTH, WINDOW_HEIGHT, FPS,
    GameState
)
from model.game_model import GameModel
from view.game_view import GameView
from controller.input_handler import InputHandler


class GameController:
    """
    Contrôle le déroulement du jeu.

    Gère les événements du clavier, les actions du joueur,
    la mise à jour du modèle et l'affichage.
    """

    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.model = GameModel()
        self.view = GameView(self.screen)
        self.input_handler = InputHandler()
        self.running = True

    def run(self) -> None:
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
                print("Touche détectée:",pygame.key.name(event.key))
                self.handle_keydown(event.key)

    def handle_keydown(self, key: int) -> None:

        state = self.model.state

        if state == GameState.MENU:
            self.handle_menu_key(key)

    def handle_menu_key(self, key: int) -> None:
        if key == pygame.K_RETURN:
            self.model.load_circuit()
            self.model.state = GameState.RACING
        elif key == pygame.K_ESCAPE:
            self.quit()

    def update(self) -> None:
        """
        Met à jour les données du jeu pendant la course.
        
        Vérifie que la course est en cours et qu'un
        circuit est chargé avant de déplacer la voiture.
        
        """

        if self.model.state != GameState.RACING:
            return

        p1_input = self.input_handler.get_inputs()
        car = self.model.car
        self.apply_input(car, p1_input)
        self.model.update()

    def apply_input(self, car, player_input) -> None:
        """
        Applique les commandes du joueur à sa voiture.

        Paramètres :
        car : voiture à contrôler.
        player_input : dictionnaire contenant les actions
        du joueur (accélérer ou freiner).

        """
        
        if player_input['accelerate']:
            car.accelerate()

        if player_input["brake"]:
            car.brake()

    def render(self) -> None:
        """
        Actualise l'affichage du jeu.

        Transmet le modèle à la vue pour dessiner
        les éléments correspondant à l'état actuel.
        """
        self.view.draw(self.model)

    def quit(self) -> None:
        self.running = False
        pygame.quit()
        sys.exit()