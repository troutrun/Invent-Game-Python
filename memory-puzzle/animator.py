import pygame
import random

import config
import drawer
import boarder


def reveal_boxes_animation(board, boxes_to_reveal):
    # Do the "box reveal" animation.
    for coverage in range(config.BOXSIZE, (-config.REVEALSPEED) - 1, -config.REVEALSPEED):
        drawer.drawBoxCovers(board, boxes_to_reveal, coverage)


def cover_boxes_animation(board, boxes_to_cover):
    # Do the "box cover" animation.
    for coverage in range(0, config.BOXSIZE + config.REVEALSPEED, config.REVEALSPEED):
        drawer.drawBoxCovers(board, boxes_to_cover, coverage)


def start_game_animation(board):
    # Randomly reveal the boxes 8 at a time.
    covered_boxes = boarder.generate_revealed_boxes_data(False)
    boxes = []
    for x in range(config.BOARDWIDTH):
        for y in range(config.BOARDHEIGHT):
            boxes.append((x, y))
    random.shuffle(boxes)
    box_groups = boarder.split_into_groups_of(8, boxes)

    drawer.draw_board(board, covered_boxes)
    for boxGroup in box_groups:
        reveal_boxes_animation(board, boxGroup)
        cover_boxes_animation(board, boxGroup)


def game_won_animation(board):
    # flash the background color when the player has won
    covered_boxes = boarder.generate_revealed_boxes_data(True)
    color1 = config.LIGHTBGCOLOR
    color2 = config.BGCOLOR

    for i in range(13):
        color1, color2 = color2, color1 # swap colors
        config.DISPLAYSURF.fill(color1)
        drawer.draw_board(board, covered_boxes)
        pygame.display.update()
        pygame.time.wait(300)


def has_won(revealed_boxes):
    # Returns True if all the boxes have been revealed, otherwise False
    for i in revealed_boxes:
        if False in i:
            # return False if any boxes are covered.
            return False
    return True
