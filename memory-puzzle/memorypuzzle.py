# Memory Puzzle
# By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license

# Modifications by Vang Xiong
# Separated configuration variables to separate file (configs.py)


import pygame
import sys
from pygame.locals import *

import config
import boarder
import animator
import drawer


assert (
    (config.BOARDWIDTH * config.BOARDHEIGHT) % 2 == 0,
    'Board needs to have an even number of boxes for pairs of matches.'
)

assert (
    len(config.ALLCOLORS) * len(config.ALLSHAPES) * 2 >= config.BOARDWIDTH * config.BOARDHEIGHT,
    "Board is too big for the number of shapes/colors defined."
)


def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((config.WINDOWWIDTH, config.WINDOWHEIGHT))

    mousex = 0 # used to store x coordinate of mouse event
    mousey = 0 # used to store y coordinate of mouse event
    pygame.display.set_caption('Memory Game')

    mainBoard = boarder.get_randomized_board()
    revealedBoxes = boarder.generate_revealed_boxes_data(False)

    # stores the (x, y) of the first box clicked.
    firstSelection = None

    DISPLAYSURF.fill(config.BGCOLOR)
    animator.start_game_animation(mainBoard)

    # main game loop
    while True:
        mouseClicked = False

        # drawing the window
        DISPLAYSURF.fill(config.BGCOLOR)
        drawer.draw_board(mainBoard, revealedBoxes)

        # event handling loop
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        boxx, boxy = boarder.get_box_at_pixel(mousex, mousey)
        if boxx != None and boxy != None:
            # The mouse is currently over a box.
            if not revealedBoxes[boxx][boxy]:
                drawer.draw_highlight_box(boxx, boxy)
            if not revealedBoxes[boxx][boxy] and mouseClicked:
                drawer.reveal_boxes_animation(mainBoard, [(boxx, boxy)])
                # set the box as "revealed"
                revealedBoxes[boxx][boxy] = True
                # the current box was the first box clicked
                if firstSelection == None:
                    firstSelection = (boxx, boxy)
                # the current box was the second box clicked
                # Check if there is a match between the two icons.
                else:
                    icon1shape, icon1color = boarder.get_shape_and_color(mainBoard, firstSelection[0], firstSelection[1])
                    icon2shape, icon2color = boarder.get_shape_and_color(mainBoard, boxx, boxy)

                    if icon1shape != icon2shape or icon1color != icon2color:
                        # Icons don't match. Re-cover up both selections.
                        pygame.time.wait(1000) # 1000 milliseconds = 1 sec
                        animator.cover_boxes_animation(mainBoard, [(firstSelection[0], firstSelection[1]), (boxx, boxy)])
                        revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                        revealedBoxes[boxx][boxy] = False
                    elif animator.has_won(revealedBoxes): # check if all pairs found
                        animator.game_won_animation(mainBoard)
                        pygame.time.wait(2000)

                        # Reset the board
                        mainBoard = boarder.get_randomized_board()
                        revealedBoxes = boarder.generate_revealed_boxes_data(False)

                        # Show the fully unrevealed board for a second.
                        drawer.draw_board(mainBoard, revealedBoxes)
                        pygame.display.update()
                        pygame.time.wait(1000)

                        # Replay the start game animation.
                        animator.start_game_animation(mainBoard)
                    firstSelection = None # reset firstSelection variable

        # Redraw the screen and wait a clock tick.
        pygame.display.update()
        FPSCLOCK.tick(config.FPS)


if __name__ == '__main__':
    main()
