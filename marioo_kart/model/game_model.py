# Kart-Engine v2.3

from constants import GameState, GRID_ROWS, GRID_COLS
from model.car import Car
from model.circuit import Circuit
from model.road_tile import RoadTile


class GameModel:
    """
    Contient les données et l'état du jeu.

    Gère le circuit, les deux voitures et leur évolution
    pendant une course.
    """

    def __init__(self) -> None:
        """
        Initialise les données du jeu.
        """
        self.state: str = GameState.MENU
        self.circuit: Circuit | None = None
        self.car1: Car | None = None
        self.car2: Car | None = None

    def load_circuit(self) -> None:
        """
        Génère la grille du circuit et initialise les voitures.
        """

        grid = []

        for row in range(GRID_ROWS):
            ligne = []

            for col in range(GRID_COLS):

                terrain = "road"

                if row < 2 or row > 9 or col < 2 or col > 13:
                    terrain = "grass"

                elif 4 <= row <= 6 and 5 <= col <= 9:
                    terrain = "ice"

                elif 7 <= row <= 8 and 4 <= col <= 11:
                    terrain = "dirt"

                case = RoadTile(col, row, terrain)
                ligne.append(case)

            grid.append(ligne)

        self.circuit = Circuit(grid=grid)
        self.spawn_car()

    def spawn_car(self) -> None:
        """
        Place les deux voitures sur leurs cases de départ.
        """
        self.car1 = Car(7, 1, (255, 0, 0))
        self.car2 = Car(8, 1, (0, 0, 255))

    def start_race(self) -> None:
        """
        Charge le circuit et démarre la course.
        """
        self.load_circuit()
        self.state = GameState.RACING

    def handle_player_input(
    self,
    car: Car | None,
    player_input: dict[str, bool]
) -> None:
        """
        Actualise les caractéristiques du terrain et
        applique les commandes d'un joueur à sa voiture.
        """
        if car is None:
            return

        # Actualisation du terrain
        self.update_car_terrain(car)

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

    def update_car_terrain(self, car: Car) -> None:
        """
        Adapte l'adhérence de la voiture au terrain.
        """
        if self.circuit is None:
            return

        tile = self.circuit.get_tile_at_pixel(
            car.x, car.y
        )

        if tile is not None:
            terrain = getattr(tile, "terrain", "road")
            car.set_terrain(terrain)

    def update(self) -> None:
        """
        Met à jour les deux voitures pendant la course.

        Adapte leur adhérence, calcule leur déplacement
        et vérifie les limites du circuit.
        """
        if self.state != GameState.RACING or self.circuit is None:
            return

        for car in (self.car1, self.car2):
            if car is not None:
                car.update_position()

                car.check_boundaries(
                    self.circuit.pixel_width(),
                    self.circuit.pixel_height()
                )