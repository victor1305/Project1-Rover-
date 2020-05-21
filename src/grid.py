class Grid:
    def __init__(self, grid):
        self.__grid = grid
        self.noPrivadoGrid = grid

    def set(self, newGrid):
        if len(newGrid) < 9:
            self.__grid = newGrid

    def get(self):
        return self.__grid



