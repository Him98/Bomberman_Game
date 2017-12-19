import random

from termcolor import cprint


class Wall(object):
    # length for storing the length of the board,
    # breadth for storing the breadth of the board,
    # tiles keeps the count of the number of tiles on the board,
    # wall is the 2D list for storing the whole board.
    def __init__(self):
        self.length = 20
        self.breadth = 15
        self.tiles = 0
        self.wall = []

    # reinitial() for re-initialising the board,
    def reinitial(self):
        self.tiles = 0
        self.wall = []

    # board() for making the outside boundary
    def board(self):
        for i in range(self.length):
            self.wall.append([])
            for j in range(self.breadth):
                if (i == 0 or i == self.length - 1):
                    self.wall[i].append('X')
                elif (j == 0 or j == self.breadth - 1):
                    self.wall[i].append('X')
                else:
                    self.wall[i].append(' ')

    # makeWall() for making the walls inside the board
    def makeWall(self):
        for i in range(1, self.length - 2):
            for j in range(1, self.breadth - 2):
                if (j % 2 == 0 and i % 2 == 0):
                    self.wall[i][j] = 'X'

    # makeTiles() for making the tiles which can be broken by bomberman
    def makeTiles(self, num):
        for i in range(num * 2):
            y = random.randint(2, self.length - 1)
            for j in range(num * 2):
                x = random.randint(2, self.breadth - 1)
                if (self.wall[y][x] != 'X'):
                    self.tiles += 1
                    self.wall[y][x] = '/'

    # printBoard() is the print function for printing the whole board
    def printBoard(self):
        for i in range(self.length):
            for k in range(2):
                for j in range(self.breadth):
                    if (str(self.wall[i][j]) == 'E'):
                        cprint(str(self.wall[i][j]) * 4, 'red', end="")
                    elif (str(self.wall[i][j]) == 'B'):
                        cprint(str(self.wall[i][j]) * 4, 'blue', end="")
                    elif (str(self.wall[i][j]) == '/'):
                        cprint(str(self.wall[i][j]) * 4, 'green', end="")
                    elif (str(self.wall[i][j]) == 'X'):
                        cprint(str(self.wall[i][j]) * 4, 'cyan', end="")
                    else:
                        cprint(str(self.wall[i][j]) * 4, 'white', end="")
                print("\r")


wall = Wall()
