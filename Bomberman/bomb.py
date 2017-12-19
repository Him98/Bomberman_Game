import time

from wall import wall


class Bomb(object):
    # create_time for storing time of creation of bomb,
    # posup and posleft for the position of bomb,
    # obs keeps the count of tiles destroyed,
    # enemy keeps the count of number of enemies killed,
    # noOfBombs keeps the count of bombs present with bomberman.
    def __init__(self):
        self.create_time = 0
        self.posup = 0
        self.posleft = 0
        self.obs = 0
        self.__enemy = 0
        self.__noOfBombs = 1

    # dropBomb() for dropping the bomb
    def dropBomb(self, up, left):
        if (self.__noOfBombs > 0):
            self.create_time = time.time()
            self.posup = up
            self.posleft = left
            wall.wall[self.posup][self.posleft] = '2'
            self.__noOfBombs -= 1

    # timeUpdate() for updating the timer of the bomb
    def timeUpdate(self, enemy, enemyt, bomberman):
        current_time = int(time.time() - self.create_time)
        if (current_time >= 2):
            ans = self.explode(enemy, enemyt, bomberman)
            if (ans == 1):
                return 1
            else:
                return -1
        else:
            wall.wall[self.posup][self.posleft] = 1 - current_time
            return 0

    # reinitial() for re - initialising the bombs
    def reinitial(self):
        self.create_time = 0
        self.posup = 0
        self.posleft = 0
        self.obs = 0
        self.__enemy = 0
        self.__noOfBombs = 1

    # sendEnemy() for getting the number of enemies killed
    def sendEnemy(self):
        return self.__enemy

    # NoBombs() for getting the number of bombs present with bomberman
    def NoBombs(self):
        return self.__noOfBombs

    # sendScore() for getting the score generated by explosion of one bomb
    def sendScore(self):
        return self.obs * 20 + self.__enemy * 100

    # explode() for causing the explosion
    def explode(self, enemy, enemyt, bomberman):
        if (wall.wall[self.posup - 1][self.posleft] != 'X'):
            if (wall.wall[self.posup - 1][self.posleft] == '/'):
                self.obs += 1
            if (wall.wall[self.posup - 1][self.posleft] == 'B'):
                return self.die()
            if (wall.wall[self.posup - 1][self.posleft] == 'E'):
                self.__enemy += 1
                if (enemy.up == self.posup - 1 and enemy.left == self.posleft):
                    enemy.kill()
                else:
                    enemyt.kill()
            wall.wall[self.posup - 1][self.posleft] = '^'
        if (wall.wall[self.posup][self.posleft - 1] != 'X'):
            if (wall.wall[self.posup][self.posleft - 1] == '/'):
                self.obs += 1
            if (wall.wall[self.posup][self.posleft - 1] == 'B'):
                return self.die()
            if (wall.wall[self.posup][self.posleft - 1] == 'E'):
                self.__enemy += 1
                if (enemy.up == self.posup and enemy.left == self.posleft - 1):
                    enemy.kill()
                else:
                    enemyt.kill()
            wall.wall[self.posup][self.posleft - 1] = '^'
        if (wall.wall[self.posup][self.posleft + 1] != 'X'):
            if (wall.wall[self.posup][self.posleft + 1] == '/'):
                self.obs += 1
            if (wall.wall[self.posup][self.posleft + 1] == 'B'):
                return self.die()
            if (wall.wall[self.posup][self.posleft + 1] == 'E'):
                self.__enemy += 1
                if (enemy.up == self.posup and enemy.left == self.posleft + 1):
                    enemy.kill()
                else:
                    enemyt.kill()
            wall.wall[self.posup][self.posleft + 1] = '^'
        if (wall.wall[self.posup + 1][self.posleft] != 'X'):
            if (wall.wall[self.posup + 1][self.posleft] == '/'):
                self.obs += 1
            if (wall.wall[self.posup + 1][self.posleft] == 'B'):
                return self.die()
            if (wall.wall[self.posup + 1][self.posleft] == 'E'):
                self.__enemy += 1
                if (enemy.up == self.posup + 1 and enemy.left == self.posleft):
                    enemy.kill()
                else:
                    enemyt.kill()
            wall.wall[self.posup + 1][self.posleft] = '^'
        if (bomberman.up == self.posup and self.posleft == bomberman.left):
            return self.die()
        wall.wall[self.posup][self.posleft] = '^'
        return 1

    # cleaning() for clearing the explosion
    def cleaning(self):
        if (wall.wall[self.posup - 1][self.posleft] != 'X'):
            wall.wall[self.posup - 1][self.posleft] = ' '
        if (wall.wall[self.posup][self.posleft - 1] != 'X'):
            wall.wall[self.posup][self.posleft - 1] = ' '
        if (wall.wall[self.posup][self.posleft + 1] != 'X'):
            wall.wall[self.posup][self.posleft + 1] = ' '
        if (wall.wall[self.posup + 1][self.posleft] != 'X'):
            wall.wall[self.posup + 1][self.posleft] = ' '
        wall.wall[self.posup][self.posleft] = ' '
        self.__noOfBombs += 1

    # die() to kill the bomberman.
    def die(self):
        return 0


bomb = Bomb()