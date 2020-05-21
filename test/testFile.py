import unittest
from src.grid import Grid
from src.rover import Rover



class PruebasFunciones(unittest.TestCase):

    def test_turnLeft(self):
        rover1 = Rover("Rover-001", "N", 0, 0)
        Rover.turnLeft(rover1)
        self.assertEqual(rover1.direction, "W")

    def test_turnRight(self):
        rover1 = Rover("Rover-001", "N", 0, 0)
        Rover.turnRight(rover1)
        self.assertEqual(rover1.direction, "E")

    def test_moveForward(self):
        rover1 = Rover("Rover-001", "N", 5, 0)
        grid1 = Grid([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0]
        ])
        Rover.moveForward(rover1, grid1)
        self.assertEqual(rover1.y, 4)
        grid1.noPrivadoGrid[rover1.y][rover1.x] = 0

    def test_moveBackward(self):
        rover1 = Rover("Rover-001", "N", 5, 0)
        grid1 = Grid([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0],
            [0]
        ])
        Rover.moveBackward(rover1, grid1)
        self.assertEqual(rover1.y, 6)
        grid1.noPrivadoGrid[rover1.y][rover1.x] = 0

    def test_commands(self):
        rover1 = Rover("Rover-001", "N", 0, 0)
        grid1 = Grid([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0],
            [0]
        ])
        Rover.commands(rover1, grid1, "rffff")
        self.assertEqual(rover1.y, 0)
        self.assertEqual(rover1.x, 4)
        grid1.noPrivadoGrid[rover1.y][rover1.x] = 0

    def test_obstacle(self):
        rover1 = Rover("Rover-001", "N", 0, 0)
        grid1 = Grid([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, "rock", 0, 0, 0, 0, 0],
            [0, 0],
            [0]
        ])
        Rover.commands(rover1, grid1, "bbbbrf")
        self.assertEqual(rover1.y, 4)
        self.assertEqual(rover1.x, 0)
        grid1.noPrivadoGrid[rover1.y][rover1.x] = 0

    def test_error_message(self):
        rover4 = Rover("Rover-004", "E", 2, 4)
        grid2 = Grid([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, "rock", 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0],
            [0]
        ])
        result = Rover.moveForward(rover4, grid2)
        self.assertEqual(result, "There is a rock on y = 2 , x = 5")
        grid2.noPrivadoGrid[rover4.y][rover4.x] = 0

    def test_grid_top(self):
        rover1 = Rover("Rover-001", "N", 0, 0)
        grid1 = Grid([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0],
            [0]
        ])
        Rover.commands(rover1, grid1, "fffff")
        self.assertEqual(rover1.y, 0)
        self.assertEqual(rover1.x, 0)
        grid1.noPrivadoGrid[rover1.y][rover1.x] = 0

    def test_grid_right(self):
        rover1 = Rover("Rover-001", "N", 0, 0)
        grid1 = Grid([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0],
            [0]
        ])
        Rover.commands(rover1, grid1, "rfffffffffffffffffffffffffff")
        self.assertEqual(rover1.y, 0)
        self.assertEqual(rover1.x, 6)
        grid1.noPrivadoGrid[rover1.y][rover1.x] = 0

    def test_grid_bottom(self):
        rover1 = Rover("Rover-001", "N", 0, 0)
        grid1 = Grid([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0],
            [0]
        ])
        Rover.commands(rover1, grid1, "bbbbbbbbbb")
        self.assertEqual(rover1.y, 6)
        self.assertEqual(rover1.x, 0)
        grid1.noPrivadoGrid[rover1.y][rover1.x] = 0

    def test_grid_left(self):
        rover1 = Rover("Rover-001", "N", 0, 0)
        grid1 = Grid([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0],
            [0]
        ])
        Rover.commands(rover1, grid1, "lfff")
        self.assertEqual(rover1.y, 0)
        self.assertEqual(rover1.x, 0)
        grid1.noPrivadoGrid[rover1.y][rover1.x] = 0

    def test_grid(self):
        rover1 = Rover("Rover-001", "N", 0, 0)
        grid1 = Grid([
            [0, 0],
            [0, 0],
            ["Rover2", 0]
        ])
        grid2 = Grid([
            [0, "Rock"],
            [0, 0],
            ["Rover2", 0]
        ])

        # TODO ejecucion por Grid2 -> No se mueve a [0, 1]
        Rover.commands(rover1, grid2, "rf")

        self.assertEqual(rover1.y, 0)
        self.assertEqual(rover1.x, 0)

        # TODO Ejecucion por Grid 1 -> Si se mueve a [0, 1]
        Rover.commands(rover1, grid1, "rf")

        self.assertEqual(rover1.y, 1)
        self.assertEqual(rover1.x, 0)


if __name__ == "__main__":
    unittest.main()
