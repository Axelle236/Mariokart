from constants import GameState, GRID_ROWS, GRID_COLS
from model.car import Car
from model.circuit import Circuit
from model.road_tile import RoadTile


class GameModel:
    """
    Contient les données et l'état du jeu.

    Gère le circuit, la voiture et leur évolution
    pendant une course.
    """

    def __init__(self):
        self.state: str = GameState.MENU
        self.circuit: Circuit | None = None
        self.car1: Car | None = None
        self.car2: Car | None = None

    
    def load_circuit(self) -> None:
        """
        Génère la grille du circuit et initialise les voitures.
        """
        grid = [
            [
                RoadTile(col=col_idx, row=row_idx)
                for col_idx in range(GRID_COLS)
            ]
            for row_idx in range(GRID_ROWS)
        ]

        self.circuit = Circuit(grid=grid)
        self.spawn_car()


    def spawn_car(self) -> None:
        """
        Place les deux voitures sur leurs cases de départ.
        """
        self.car1 = Car(7, 1, (255, 0, 0))
        self.car2 = Car(8, 1, (0, 0, 255))

    def update(self) -> None:
        """
        Met à jour les deux voitures pendant la course.

        Adapte leur adhérence, actualise leur position
        et vérifie les limites du circuit.
        """
        if self.state != GameState.RACING or self.circuit is None:
            return

        for car in (self.car1, self.car2):
            if car is not None:
                self.update_car_terrain(car)
                car.update_position()

                car.check_boundaries(
                self.circuit.pixel_width(),
                self.circuit.pixel_height())

    def update_car_terrain(self, car: Car) -> None:
        """
        Adapte l'adhérence de la voiture
        au terrain sur lequel elle se trouve.
        """
        
        if self.circuit is None:
            return

        tile = self.circuit.get_tile_at_pixel(
            car.x, car.y
        )

        if tile is not None:
            terrain = getattr(tile, "terrain", "road")
            car.set_terrain(terrain)