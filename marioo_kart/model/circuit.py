from model.road_tile import RoadTile
from constants import TILE_SIZE
from terrains import TILE_KINDS, BLOCK_KINDS


class Circuit:

    def __init__(self, name:str, terrain_rows: list[str], block_rows: list[str]):
        width = len(terrain_rows[0])
        if len(block_rows) != len(terrain_rows):
            raise ValueError(f"'{name}' : les deux grilles doivent avoir le même nombre de lignes")
        for i in range(len(terrain_rows)):
            t_line = terrain_rows[i]
            b_line = block_rows[i]  
            if len(t_line) != width or len(b_line) != width:
                raise ValueError(f"'{name}' : toutes les lignes doivent avoir {width} caractères")
        self.name=name
        self.rows = len(terrain_rows)
        self.cols = width
        self.grid = []
        for row in range(self.rows):
            grid_row = []
            for col in range(self.cols):
                kind = TILE_KINDS[terrain_rows[row][col]]
                block = BLOCK_KINDS[block_rows[row][col]]
                grid_row.append(RoadTile(col=col, row=row, kind=kind, block=block))
            self.grid.append(grid_row)

    def find_tiles(self, block: str) -> list[RoadTile]:
        tiles = []
        for row in self.grid:
            for tile in row:
                if tile.block == block:
                    tiles.append(tile)
        return tiles
        
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
