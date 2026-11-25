import pygame
from constants import (
    WINDOW_WIDTH, WINDOW_HEIGHT, TILE_SIZE, CAR_WIDTH, CAR_HEIGHT,
    COLOR_BG, COLOR_TEXT, COLOR_ACCENT, COLOR_PANEL, COLOR_PANEL_BORDER,
    GameState
)
from model.game_model import GameModel
from model.road_tile import RoadTile
from terrains import TILE_KINDS, TILE_COLORS, CIRCUIT_LAYOUTS, BLOCK_COLORS



class GameView:
    """
    Gère l'affichage graphique du jeu.

    Dessine le menu, le circuit et la voiture
    selon les données fournies par le modèle.
    """

    def __init__(self, screen: pygame.Surface):
        """
        Initialise la vue du jeu.

        Paramètre :
            screen : surface Pygame utilisée pour l'affichage.
        """
        
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 24)
        self._car_surface=self._build_car_surface()

    def draw(self, model: GameModel) -> None:
        """
        Affiche le jeu selon son état actuel.
        
        Dessine le menu ou la course à partir du modèle,
        puis actualise l'écran.
        """
         
        self.screen.fill(COLOR_BG)
        if model.state == GameState.MENU:
            self._draw_menu()
        elif model.state == GameState.CIRCUIT_SELECT:
            self._draw_circuit_selection(model)
        elif model.state == GameState.RACING:
            self._draw_racing(model)
        pygame.display.flip()

    def _draw_title(self, text: str, y: int) -> None:
        surf = self.font.render(text, True, COLOR_ACCENT)
        x = WINDOW_WIDTH // 2 - surf.get_width() // 2
        self.screen.blit(surf, (x, y))

    def _draw_button(self, center_y: int, label: str, selected: bool) -> None:
        cx = WINDOW_WIDTH // 2
        rect = pygame.Rect(cx - 140, center_y - 25, 280, 50)
        pygame.draw.rect(self.screen, COLOR_PANEL, rect, border_radius=8)
        border_color = COLOR_ACCENT if selected else COLOR_PANEL_BORDER
        pygame.draw.rect(self.screen, border_color, rect, 3 if selected else 2, border_radius=8)
        text = self.font.render(label, True, COLOR_ACCENT if selected else COLOR_TEXT)
        self.screen.blit(text, text.get_rect(center=rect.center))

    def _draw_menu(self) -> None:
        self._draw_title("Course de voitures", 160)
        self._draw_button(320, "JOUER (Enter)", selected=True)
        self._draw_button(400, "QUITTER (Escape)", selected=False)

    def _draw_circuit_selection(self, model: GameModel) -> None:
        self._draw_title("Choisissez un circuit", 160)
        for i, layout in enumerate(CIRCUIT_LAYOUTS):
            self._draw_button(280 + i * 80, layout["name"], selected=(i == model.selected_index))

    def _draw_tile(self, tile: RoadTile) -> None:
        color = TILE_COLORS.get(tile.kind, (255, 0, 255))  
        rect = pygame.Rect(tile.col * TILE_SIZE, tile.row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(self.screen, color, rect)
        pygame.draw.rect(self.screen, (60, 60, 70), rect, 1)
        if tile.block is not None:
            inner = rect.inflate(-TILE_SIZE // 2, -TILE_SIZE // 2)
            pygame.draw.rect(self.screen, BLOCK_COLORS.get(tile.block, (255, 0, 255)), inner)

    def _draw_racing(self, model: GameModel) -> None:
        if model.circuit is None or model.car is None:
            return
        for row in model.circuit.grid:
            for tile in row:
                self._draw_tile(tile)

        car = model.car
        rotated = pygame.transform.rotate(self._car_surface, -car.angle)
        rect = rotated.get_rect(center=(int(car.x), int(car.y)))
        self.screen.blit(rotated, rect)

    def _build_car_surface(self) -> pygame.Surface:
        surf=pygame.Surface((CAR_WIDTH, CAR_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(surf, (255, 0, 0), surf.get_rect(), border_radius=5)
        return surf
