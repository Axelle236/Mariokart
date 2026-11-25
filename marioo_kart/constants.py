
# --- Paramètres de la fenêtre ---
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
FPS = 60

# --- Dimensions du circuit ---
TILE_SIZE = 64
GRID_COLS = 16
GRID_ROWS = 12

# --- Paramètres de déplacement ---
CAR_ACCELERATION = 0.05
CAR_TURN_SPEED = 3

# --- Dimensions des voitures ---
CAR_WIDTH = 30
CAR_HEIGHT = 50

CAR_GRIP = 0.08

CAR_MAX_SPEED = 6.0
CAR_MAX_REVERSE_SPEED = 2.0
CAR_FRICTION = 0.02

# --- Adhérence selon le terrain ---
TERRAIN_GRIP = {
    "road": 0.15,
    "dirt": 0.08,
    "grass": 0.04,
    "ice": 0.01,
    "sand": 0.06
}

TERRAIN_TRACTION = {
    "road": 1.0,
    "grass": 0.6,
    "dirt": 0.7,
    "ice": 0.2
}

TERRAIN_FRICTION = {
    "road": 0.02,
    "grass": 0.05,
    "dirt": 0.04,
    "ice": 0.005
}

AIR_FRICTION = 0.001

DRIFT_ANGLE_THRESHOLD = 15.0

TERRAIN_DRIFT_FRICTION = {
    "road": 0.04,
    "grass": 0.02,
    "dirt": 0.01,
    "ice": 0.002
}

CAR_BOOST_SPEED = 3.0
CAR_MAX_BOOST_SPEED = 9.0

# --- États du jeu ---
class GameState:
    MENU = "menu"
    CIRCUIT_SELECTION = "circuit_selection"
    RACING = "racing"


# --- Couleurs de l'interface ---
COLOR_BG = (15, 15, 25)
COLOR_TEXT = (240, 240, 240)
COLOR_ACCENT = (255, 200, 0)
COLOR_PANEL = (30, 30, 50)
COLOR_PANEL_BORDER = (60, 60, 100)
