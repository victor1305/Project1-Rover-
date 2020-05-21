from .grid import Grid


class Rover:
    def __init__(self, name, direction, y, x):

        self.name = name
        self.accidentDetector = ""
        self.direction = direction
        self.y = y
        self.x = x
        self.travelLog = []

    def turnLeft(self):

        if self.direction == "N":
            self.direction = "W"

        elif self.direction == "W":
            self.direction = "S"

        elif self.direction == "S":
            self.direction = "E"

        else:
            self.direction = "N"

        print("TurnLeft was called!")


    def turnRight(self):

        if self.direction == "N":
            self.direction = "E"

        elif self.direction == "W":
            self.direction = "N"

        elif self.direction == "S":
            self.direction = "W"

        else:
            self.direction = "S"

        print("TurnRight was called!")

    def moveForward(self, grid: Grid):

        if self.direction == "N":
            if self.y == 0:
                print("You can't place Rover outside of the map!")

            else:
                self.y -= 1
                newPosition = {"y": self.y, "x": self.x}
                roverPosition = grid.noPrivadoGrid[self.y][self.x]

                if roverPosition != 0:
                    self.accidentDetector = "On"
                    errorMessage = "There is a {} on y = {} , x = {}".format(roverPosition, self.y, self.x)
                    print(errorMessage)
                    self.y += 1
                    return errorMessage

                else:
                    self.travelLog.append(newPosition)
                    print("moveForward was called, the current position is: y = ", self.y, ", x = ", self.x)

        elif self.direction == "W":
            if self.x == 0:
                print("You can't place Rover outside of the map!")

            else:
                self.x -= 1
                newPosition = {"y": self.y, "x": self.x}
                roverPosition = grid.noPrivadoGrid[self.y][self.x]

                if roverPosition != 0:
                    self.accidentDetector = "On"
                    errorMessage = "There is a {} on y = {} , x = {}".format(roverPosition, self.y, self.x)
                    print(errorMessage)
                    self.x += 1
                    return errorMessage

                else:
                    self.travelLog.append(newPosition)
                    print("moveForward was called, the current position is: y = ", self.y, ", x = ", self.x)

        elif self.direction == "S":
            if self.y == (len(grid.noPrivadoGrid) - 1):
                print("You can't place Rover outside of the map!")

            else:
                self.y += 1
                newPosition = {"y": self.y, "x": self.x}
                roverPosition = grid.noPrivadoGrid[self.y][self.x]

                if roverPosition != 0:
                    self.accidentDetector = "On"
                    errorMessage = "There is a {} on y = {} , x = {}".format(roverPosition, self.y, self.x)
                    print(errorMessage)
                    self.y -= 1
                    return errorMessage

                else:
                    self.travelLog.append(newPosition)
                    print("moveForward was called, the current position is: y = ", self.y, ", x = ", self.x)

        else:
            if self.x == (len(grid.noPrivadoGrid[self.y]) - 1):
                print("You can't place Rover outside of the map!")

            else:
                self.x += 1
                newPosition = {"y": self.y, "x": self.x}
                roverPosition = grid.noPrivadoGrid[self.y][self.x]

                if roverPosition != 0:
                    self.accidentDetector = "On"
                    errorMessage = "There is a {} on y = {} , x = {}".format(roverPosition, self.y, self.x)
                    print(errorMessage)
                    self.x -= 1
                    return errorMessage

                else:
                    self.travelLog.append(newPosition)
                    print("moveForward was called, the current position is: y = ", self.y, ", x = ", self.x)

    def moveBackward(self, grid: Grid):

        if self.direction == "N":
            if self.y == (len(grid.noPrivadoGrid) - 1):
                print("You can't place Rover outside of the map!")

            else:
                self.y += 1
                newPosition = {"y": self.y, "x": self.x}
                roverPosition = grid.noPrivadoGrid[self.y][self.x]

                if roverPosition != 0:
                    self.accidentDetector = "On"
                    errorMessage = "There is a {} on y = {} , x = {}".format(roverPosition, self.y, self.x)
                    print(errorMessage)
                    self.y -= 1
                    return errorMessage

                else:
                    self.travelLog.append(newPosition)
                    print("moveBackward was called, the current position is: y = ", self.y, ", x = ", self.x)

        elif self.direction == "W":
            if self.x == (len(grid.noPrivadoGrid[self.y]) - 1):
                print("You can't place Rover outside of the map!")

            else:
                self.x += 1
                newPosition = {"y": self.y, "x": self.x}
                roverPosition = grid.noPrivadoGrid[self.y][self.x]

                if roverPosition != 0:
                    self.accidentDetector = "On"
                    errorMessage = "There is a {} on y = {} , x = {}".format(roverPosition, self.y, self.x)
                    print(errorMessage)
                    self.x -= 1
                    return errorMessage

                else:
                    self.travelLog.append(newPosition)
                    print("moveBackward was called, the current position is: y = ", self.y, ", x = ", self.x)

        elif self.direction == "S":
            if self.y == 0:
                print("You can't place Rover outside of the map!")

            else:
                self.y -= 1
                newPosition = {"y": self.y, "x": self.x}
                roverPosition = grid.noPrivadoGrid[self.y][self.x]

                if roverPosition != 0:
                    self.accidentDetector = "On"
                    errorMessage = "There is a {} on y = {} , x = {}".format(roverPosition, self.y, self.x)
                    print(errorMessage)
                    self.y += 1
                    return errorMessage

                else:
                    self.travelLog.append(newPosition)
                    print("moveBackward was called, the current position is: y = ", self.y, ", x = ", self.x)

        else:
            if self.x == 0:
                print("You can't place Rover outside of the map!")

            else:
                self.x -= 1
                newPosition = {"y": self.y, "x": self.x}
                roverPosition = grid.noPrivadoGrid[self.y][self.x]

                if roverPosition != 0:
                    self.accidentDetector = "On"
                    errorMessage = "There is a {} on y = {} , x = {}".format(roverPosition, self.y, self.x)
                    print(errorMessage)
                    self.x += 1
                    return errorMessage

                else:
                    self.travelLog.append(newPosition)
                    print("moveBackward was called, the current position is: y = ", self.y, ", x = ", self.x)

    def commands(self, grid: Grid, orders: str):

        print(self.name + " ready to start!\n")
        self.accidentDetector = ""
        i = 0
        while i < len(orders) and self.accidentDetector != "On":

            if orders[i] == "l":
                Rover.turnLeft(self)

            elif orders[i] == "r":
                Rover.turnRight(self)

            elif orders[i] == "f":
                Rover.moveForward(self, grid)

            elif orders[i] == "b":
                Rover.moveBackward(self, grid)

            else:
                print("Insert a valid command")

            i += 1

        print("TravelLog of the ", self.name, ":")
        print(self.travelLog)
        print("\n****************************************************************************************************")
        print("\n\n")

        grid.noPrivadoGrid[self.y][self.x] = self.name



