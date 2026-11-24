WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
FPS = 60

TILE_SIZE = 64
GRID_COLS = 16
GRID_ROWS = 12

CAR_ACCELERATION = 0.05
CAR_WIDTH = 30
CAR_HEIGHT = 50


class GameState:
    MENU = "menu"
    CIRCUIT_SELECT = "circuit_select"
    RACING = "racing"


# --- Couleurs UI ---
COLOR_BG = (15, 15, 25)
COLOR_TEXT = (240, 240, 240)
COLOR_ACCENT = (255, 200, 0)
COLOR_PANEL = (30, 30, 50)
COLOR_PANEL_BORDER = (60, 60, 100)

TILE_KINDS = {
    "R": "route",
    "V": "vide",
    "T": "terre",
    "H": "herbe",
    "G": "glace",
}

TILE_COLORS = {
    "route": (80, 80, 90),
    "herbe": (60, 140, 60),
    "terre": (150, 100, 50),
    "glace": (170, 220, 240),
    "vide": (15, 15, 15),
}

CIRCUIT_LAYOUTS = [
    {
        "name": "Circuit 1",
        "orientation": 90.0,
        "terrain": [
            "HHHHHHHHVVVVVVVV",
            "HHHHHHHHVVVVVVVV",
            "HHVVVVVVVRRRRRRV",
            "TTVVVVVVVRRRRRRV",
            "TTTTTTTTRRRVVGGV",
            "TTTTTTTTRRRVVGGV",
            "VVVVVVVVVVVVVGGV",
            "VVVVVTTTTTTTVGGV",
            "VVVVVTTTTTTTVGGV",
            "VVVVVTTVVVRRVGGV",
            "HHHHHHHVVVRRRGGV",
            "HHHHHHHVVVRRRGGV",
        ],
        "blocks": [
            "...C...S........",
            "...C...S......CC",
            "................",
            "CC.......CC.....",
            "...B.C..........",
            ".....C..........",
            "................",
            ".......C........",
            "......C..B......",
            ".........CC.....",
            "F...C...........",
            "F...C...........",
        ]
    },

    {
        "name": "Circuit 2",
        "orientation": 90.0,
        "terrain": [
            "RRRRRRRRVVVVVVVV",
            "RRRRRRRRVVVVVVVV",
            "RRVVVVVVVVVVVVVV",
            "RRVVVVVVVVVVVVVV",
            "RRVVRRRRRRRRRTTT",
            "RRVVRRRRRRRRRTTT",
            "GGVVVVVVVVVVVVTT",
            "GGVVVVVVVVVVVVTT",
            "GGVVVVVVVVVVVVTT",
            "GGVVVVVVVVVVVVHH",
            "GGGGTTTTTTTHHHHH",
            "GGGGTTTTTTTHHHHH",
        ],
        "blocks": [
            "..C....SF..C....",
            "..C....SF..C....",
            "..............CC",
            "................",
            "CC..............",
            "................",
            "..............CC",
            "................",
            "................",
            "......C....C....",
            "......C....C....",
            "................",
        ]
    },
]
