from wall import wall


class Person(object):
    # up and left are for specifying positions of a person
    def __init__(self, up, left):
        self.up = up
        self.left = left

    # To move left
    def moveleft(self):
        if (wall.wall[self.up][self.left - 1] == ' ' or wall.wall[self.up][self.left - 1] == 'B'):
            self.left -= 1

    # To move right
    def moveright(self):
        if (wall.wall[self.up][self.left + 1] == ' ' or wall.wall[self.up][self.left + 1] == 'B'):
            self.left += 1

    # To move down
    def movedown(self):
        if (wall.wall[self.up + 1][self.left] == ' ' or wall.wall[self.up + 1][self.left] == 'B'):
            self.up += 1

    # To move up
    def moveup(self):
        if (wall.wall[self.up - 1][self.left] == ' ' or wall.wall[self.up - 1][self.left] == 'B'):
            self.up -= 1

    # Method to be overriden
    def showMan(self):
        pass

    # To clear the position after a person moves
    def moveOn(self):
        wall.wall[self.up][self.left] = ' '
