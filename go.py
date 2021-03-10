import pygame
import numpy as np
pygame.init()

display_width = 600
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('GO')
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
grey = (200,140,70)
points = []
board_size = 9
board = np.zeros((10,10))
positions = []

def __init__():
    global positions

    temp = []
    for y in range(11):
        positions.append(temp)
        temp = []
        for x in range(11):
            temp.append((40+x*60, 40+y*60))
    positions = positions[1:]
    game_loop()

def draw_board():
    gameDisplay.fill(grey)

    for i in range(40, board_size*60, 60):
        pygame.draw.lines(gameDisplay, black, True, [(40, i), (580, i)], 5)
        pygame.draw.lines(gameDisplay, black, True, [(i, 40), (i, 580)], 5)

    pygame.draw.circle(gameDisplay, black, (160, 160), 10)
    pygame.draw.circle(gameDisplay, black, (460, 160), 10)
    pygame.draw.circle(gameDisplay, black, (160, 460), 10)
    pygame.draw.circle(gameDisplay, black, (460, 460), 10)
    pygame.draw.rect(gameDisplay, black, (40, 40, 540, 540), 10)

    pygame.display.update()

def update():
    # Add 2's to outside to make edges
    draw_board()
    for x in range(10):
        for y in range(10):
            if board[y][x] == -1.:  #change to -1
                pygame.draw.circle(gameDisplay, white, positions[x][y], 17) # can change to pos x,y if I want
            elif board[y][x] == 1.:
                pygame.draw.circle(gameDisplay, black, positions[x][y], 17)

    pygame.display.update()
def check_capture():
    for row in range(board_size):
        for value in range(board_size):
            for i in [-1,1]:

                # Normal case
                if (board[row][value] == i and board[row-1][value] == -i and board[row+1][value] == -i) and (board[row][value-1] == -i and board[row][value+1] == -i):
                    board[row][value] = 0
                    update()
                    # Still takes go on illegal move, perhaps remove the first argument in this if statement and add a check_if_valid function

                # Capturing Multiple
                # If its left is also filled

                if (board[row][value] == i and board[row-1][value] == i and board[row+1][value] == -i) and (board[row][value-1] == -i and board[row][value+1] == -i):

                    if (board[row-1][value] == i and # It is filled
                        board[row-2][value] == -i and # Its left is filled
                        # removed right
                        board[row-1][value - 1] == -i and # Its top is filled
                            board[row-1][value + 1] == -i): # Its bottom is filled

                        board[row-1][value] = 0
                        board[row][value] = 0
                        update()

    #print(row, value)
    print('\n\n', board)

def game_loop():
    gameExit = False
    turn = 1
    update()
    # Main Loop
    while not gameExit:
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                y = 0
                mouse = pygame.mouse.get_pos()
                for pos in positions:
                    y += 1
                    for x in range(10):
                        if (int(pos[x][0])-10 <= int(mouse[0]) <= int(pos[x][0])+10) and (int(pos[x][1])-10 <= int(mouse[1]) <= int(pos[x][1])+10) and (board[x][positions.index(pos)] == 0):
                            board[x][positions.index(pos)] = turn
                            turn = -turn
                            update()
                check_capture()

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    pygame.display.update()
    clock.tick(120)
__init__()
pygame.quit()
quit()
