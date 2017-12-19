import os
import random
import time

from bomb import bomb
from getch import _Getch
from levels import levels, end, win
from person import Person
from wall import wall


class Bomberman(Person):
    # lives for storing how many lives are left,
    # dead for storing whether person is alive or not,
    # score stores the total score of person in a level,
    def __init__(self, up, left):
        Person.__init__(self, up, left)
        self.lives = 3
        self.dead = 0
        self.score = 0

    # reinitial() for re-initialising the bomberman
    def reinitial(self):
        self.up = 1
        self.left = 1

    # showMan() for showing the bomberman on the board, overriden method of Person
    def showMan(self):
        wall.wall[self.up][self.left] = 'B'

    # check() for checking whether positions of bomberman and enemy are same or not
    def check(self, enemy):
        if (self.up == enemy.up and self.left == enemy.left):
            self.dead = 1
            self.lives -= 1
            wall.wall[self.up][self.left] = ' '
            self.up = 1
            self.left = 1
            wall.wall[1][1] = 'B'


class Enemy(Person):
    # dead for storing whether person is alive or not
    def __init__(self, x, y):
        Person.__init__(self, x, y)
        self.dead = 0

    # randomMove() for generating a random number according to which the enemy moves
    def randomMove(self):
        if (self.dead != 1):
            x = random.randint(1, 4)
            return x
        return 0

    # showMan() for showing the enemy on the board, overriden method of Person
    def showMan(self):
        wall.wall[self.up][self.left] = 'E'

    # kill() for killing the enemy
    def kill(self):
        self.dead = 1
        wall.wall[self.up][self.left] = ' '

    # eneMove() for moving the enemy according to the randomMove() generated value
    def eneMove(self):
        z = self.randomMove()
        if (z == 1):
            self.moveOn()
            self.moveleft()
            self.showMan()
        if (z == 2):
            self.moveOn()
            self.moveright()
            self.showMan()
        if (z == 3):
            self.moveOn()
            self.movedown()
            self.showMan()
        if (z == 4):
            self.moveOn()
            self.moveup()
            self.showMan()


bomberman = Bomberman(1, 1)
totscore = 0
cnt = 0


# newStart() function is called whenever we need to start a new level.
# cnt is for keeping the count of the levels.

def newStart(level):
    print(levels[3 - level], "\n\n\n")
    time.sleep(1)
    bomberman.reinitial()
    wall.reinitial()
    bomb.reinitial()
    wall.board()
    wall.makeWall()
    enemy = Enemy(1, 5)
    enemy.showMan()
    enemyt = Enemy(11, 10)
    enemyt.showMan()
    bomberman.showMan()
    wall.makeTiles(level)
    wall.printBoard()

    bombs = 0
    g = 0
    f = 0
    # f and g are flags. g is required for the move just after placing the bomb.
    # f is required for cleaning the explosion.
    while (bomb.sendEnemy() < 2):
        if (enemy.dead != 1):
            enemy.eneMove()
        if (enemyt.dead != 1):
            enemyt.eneMove()
        y = _Getch()
        x = y()
        if (enemy.dead != 1):
            bomberman.check(enemy)
        if (enemyt.dead != 1):
            bomberman.check(enemyt)

        if (bomberman.lives == 0 and bomberman.dead == 1):
            print(end)
            break

        if (bombs > 0):
            r = bomb.timeUpdate(enemy, enemyt, bomberman)
            if (r == 1):
                print('\n\n\n')
                bombs -= 1
                wall.printBoard()
                f = -1
            # time.sleep(1)
            # wall.printBoard()

            if (r == -1):
                if (bomberman.lives == 0):
                    print(end)
                    break
                else:
                    wall.wall[bomberman.up][bomberman.left] = ' '
                    bomberman.lives -= 1
                    if (bomberman.lives == 0):
                        print(end)
                        break
                    bomberman.up = 1
                    bomberman.left = 1
                    bomberman.showMan()
            g -= 1

        if (x == 'a'):
            if (g != 1):
                bomberman.moveOn()
            bomberman.moveleft()
            bomberman.showMan()

        elif (x == 'w'):
            if (g != 1):
                bomberman.moveOn()
            bomberman.moveup()
            bomberman.showMan()

        elif (x == 's'):
            if (g != 1):
                bomberman.moveOn()
            bomberman.movedown()
            bomberman.showMan()

        elif (x == 'd'):
            if (g != 1):
                bomberman.moveOn()
            bomberman.moveright()
            bomberman.showMan()

        elif (x == 'b' and bomb.NoBombs() > 0):
            bomb.dropBomb(bomberman.up, bomberman.left)
            bombs += 1
            g = 2

        if (enemy.dead != 1):
            bomberman.check(enemy)
        if (enemyt.dead != 1):
            bomberman.check(enemyt)

        if (bomberman.lives == 0 and bomberman.dead == 1):
            print(end)
            break

        elif (x == 'q'):
            break

        os.system('clear')
        wall.printBoard()
        if (f == -1):
            bomb.cleaning()
            f = 0
        print ("Score is ", totscore + bomb.sendScore())
        print ("Lives left ", bomberman.lives)


while (cnt != 3):
    cnt += 1
    newStart(4 - cnt)
    if (bomb.sendEnemy() == 2):
        totscore += bomb.sendScore()
        continue
    else:
        break

if (cnt == 3 and bomb.sendEnemy() == 2):
    print(win)
