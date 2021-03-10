import pygame
import numpy as np
pygame.init()

display_width = (600)
display_height = (600)
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('GO')
clock = pygame.time.Clock()
black = (0,0,0)
brown = (153, 51, 0)
white = (255,255,255)
grey = (200,140,70)
points = []
board_size = 9
board = [
    [5, 3, 4, 6, 7, 4, 3, 5],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [5, 3, 4, 7, 6, 4, 3, 5],
]
positions = []

def __init__():
    # global positions
    #
    # temp = []
    # for y in range(11):
    #     positions.append(temp)
    #     temp = []
    #     for x in range(11):
    #         temp.append((40+x*60, 40+y*60))
    # positions = positions[1:]
    game_loop()

def draw_board():
    gameDisplay.fill(brown)
    for y in range(0, display_height, int(display_height/8)):
        for x in range(0, display_width, int(display_width/8)):
            if y % 2 == 0:
                x += display_width/16
            pygame.draw.rect(gameDisplay, black, (x * 2, y, 75, 75), 0)
        pygame.display.update()

def game_loop():
    draw_board()
    while True:
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    pygame.display.update()
    clock.tick(120)

class Piece():
    def __init__(self):
        pass

    def get_image(self):
        pass

    def move(self):
        pass


class Pawn(Piece):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load()

    def get_image(self):
        return self.image









if __name__ == '__main__':
    __init__()
    pygame.quit()
    quit()
