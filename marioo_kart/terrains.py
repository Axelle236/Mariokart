BOOST_FACTOR = 1.5

TERRAINS = {
    "route": {"traction": 1.0, "grip": 0.50, "drift_threshold": 25.0, "drift_friction": 0.50},
    "herbe": {"traction": 0.8, "grip": 0.40, "drift_threshold": 15.0, "drift_friction": 0.35},
    "terre": {"traction": 0.5, "grip": 0.30, "drift_threshold": 8.0,  "drift_friction": 0.25},
    "glace": {"traction": 0.3, "grip": 0.05, "drift_threshold": 3.0,  "drift_friction": 0.02},
    "vide":  {"traction": 0.0, "grip": 0.0,  "drift_threshold": 90.0, "drift_friction": 0.0},
}

TILE_KINDS = {
    "R": "route",
    "V": "vide",
    "T": "terre",
    "H": "herbe",
    "G": "glace",
}

BLOCK_KINDS = {
    ".": None,
    "S": "start",
    "F": "finish",
    "C": "checkpoint",
    "B": "boost",
}

TILE_COLORS = {
    "route": (80, 80, 90),
    "herbe": (60, 140, 60),
    "terre": (150, 100, 50),
    "glace": (170, 220, 240),
    "vide": (15, 15, 15),
}

BLOCK_COLORS = {
    "start": (80, 160, 80),
    "checkpoint": (200, 200, 60),
    "finish": (230, 230, 230),
    "boost": (255, 120, 0),
}

CIRCUIT_LAYOUTS = [
    {
        "name": "Circuit 1",
        "orientation": 90.0,
        "terrain": [
            "RRRRRRRRRVVVVVVV",
            "RRRRRRRRRVVVVVVV",
            "RRVVVVVRRVVVVVVV",
            "RRVVVVVRRVVVVVVV",
            "HHVVVVVTTVVVVVVV",
            "HHHHHHHTTTTTTTTT",
            "HHHHHHHTTTTTTTTT",
            "VVVVVVVTTVVVVVTT",
            "VVVVVVVTTVVVVVTT",
            "VVVVVVVGGVVVVVGG",
            "VVVVVVVGGGGGGGGG",
            "VVVVVVVGGGGGGGGG",
            
        ],
        "blocks": [
            "BB.....S........",
            ".......S........",
            ".......FF.......",
            "CC..............",
            "................",
            "..B.C.....B.....",
            "..B.C.....B.....",
            "................",
            "..............CC",
            "................",
            ".......BB..C....",
            "...........C....",
        ]
    },

    {
        "name": "Circuit 2",
        "orientation": 90.0,
        "terrain": [
            "HHHHHHHHHVVVVVVV",
            "HHHHHHHHHVVVVVVV",
            "HHVVVVVGGVVVVVVV",
            "HHVVVVVGGVVVVVVV",
            "HHVVVVVGGVVVVVVV",
            "RRVVVVVGGGGGGGGG",
            "RRVVVVVGGGGGGGGG",
            "RRVVVVVVVVVVVVGG",
            "RRVVVVVVVVVVVVTT",
            "RRVVVVVVVVVVVVTT",
            "RRTTTTTTTTTTTTTT",
            "RRTTTTTTTTTTTTTT",
        ],
        "blocks": [
            ".......S........",
            ".......S........",
            "BB.....FF.......",
            "................",
            "................",
            "CC............B.",
            "..............B.",
            "..............CC",
            "................",
            "................",
            "....B....C......",
            "....B....C......",
        ]
    },
]
