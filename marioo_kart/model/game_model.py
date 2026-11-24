from constants import GameState, GRID_ROWS, GRID_COLS, CIRCUIT_LAYOUTS
from model.car import Car
from model.circuit import Circuit


class GameModel:
    """
    Contient les données et l'état du jeu.

    Gère le circuit, la voiture et leur évolution
    pendant une course.
    """

    def __init__(self):
        self.state: str = GameState.MENU
        self.circuit: Circuit | None = None
        self.car: Car | None = None
        self.selected_index: int=0

    def load_circuit(self, index: int) -> None:
        layout=CIRCUIT_LAYOUTS[index]
        self.circuit = Circuit(layout["name"], layout["terrain"])
        self.spawn_car()

    def circuit_selection(self) -> list[str]:
        return[layout["name"] for layout in CIRCUIT_LAYOUTS]

    def select_next_circuit(self) -> None:
        self.selected_index = (self.selected_index + 1) % len(CIRCUIT_LAYOUTS)

    def select_previous_circuit(self) -> None:
        self.selected_index = (self.selected_index - 1) % len(CIRCUIT_LAYOUTS)

    def spawn_car(self) -> None:
        self.car = Car(7, 1)

    def update(self) -> None:
        if self.state != GameState.RACING or self.circuit is None:
            return
        self.car.update_position()

    def start_race(self) -> None:
        self.load_circuit(self.selected_index)
        self.state=GameState.RACING

    def handle_player_input(self, player_input: dict) -> None:
        if self.car is None:
            return
        if player_input['accelerate']:
            self.car.accelerate()