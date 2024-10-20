import time

class Player():

    def __init__(self, x, y):
        self.coords = (x, y)

rows = 5
cols = 5
player = Player(1, 2)


def drawCoors(player: Player):
    for i in range(rows):
        for j in range(cols):
            if player.coords == (i, j):
                print('x', end=" ")
            else:
                print(f"{i}{j}", end=" ")
        print()


def changeCoords():
    x = 0
    y = 0
    while(True):
        player.coords = (x, y)
        drawCoors(player=player)
        time.sleep(2)
        y += 1


changeCoords()