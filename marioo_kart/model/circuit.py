from model.road_tile import RoadTile
from constants import TILE_SIZE, TILE_KINDS


class Circuit:

    def __init__(self, name:str, terrain_rows: list[str]):
        self.name=name
        width = len(terrain_rows[0])
        for line in terrain_rows:
            if len(line) != width:
                raise ValueError(f"'{name}' : toutes les lignes doivent avoir {width} caractères")
            
        self.grid = []
        for row, line in enumerate(terrain_rows):
            grid_row = []
            for col, char in enumerate(line):
                grid_row.append(RoadTile(col=col, row=row, kind=TILE_KINDS[char]))
            self.grid.append(grid_row) 
        self.rows = len(self.grid)
        self.cols = width
        
    def get_tile(self, col: int, row: int) -> RoadTile | None:
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.grid[row][col]
        return None

    def get_tile_at_pixel(self, px: float, py: float) -> RoadTile | None:
        col = int(px // TILE_SIZE)
        row = int(py // TILE_SIZE)
        return self.get_tile(col, row)

    def pixel_width(self) -> int:
        return self.cols * TILE_SIZE

    def pixel_height(self) -> int:
        return self.rows * TILE_SIZE
