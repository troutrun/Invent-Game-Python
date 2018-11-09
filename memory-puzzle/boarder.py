import random
import pygame

import config


def generate_revealed_boxes_data(val):
    revealed_boxes = []
    for i in range(config.BOARDWIDTH):
        revealed_boxes.append([val] * config.BOARDHEIGHT)
    return revealed_boxes


def get_randomized_board():
    # Get a list of every possible shape in every possible color.
    icons = []
    for color in config.ALLCOLORS:
        for shape in config.ALLSHAPES:
            icons.append((shape, color))

    # randomize the order of the icons list
    random.shuffle(icons)

    # calculate how many icons are needed
    num_icons_used = int(config.BOARDWIDTH * config.BOARDHEIGHT / 2)
    # make two of each
    icons = icons[:num_icons_used] * 2
    random.shuffle(icons)

    # Create the board data structure, with randomly placed icons.
    board = []
    for x in range(config.BOARDWIDTH):
        column = []
        for y in range(config.BOARDHEIGHT):
            column.append(icons[0])
            del icons[0] # remove the icons as we assign them
        board.append(column)
    return board


def split_into_groups_of(group_size, the_list):
    # splits a list into a list of lists, where the inner lists have at
    # most groupSize number of items.
    result = []
    for i in range(0, len(the_list), group_size):
        result.append(the_list[i:i + group_size])
    return result


def left_top_coords_of_box(boxx, boxy):
    # Convert board coordinates to pixel coordinates
    left = boxx * (config.BOXSIZE + config.GAPSIZE) + config.XMARGIN
    top = boxy * (config.BOXSIZE + config.GAPSIZE) + config.YMARGIN
    return (left, top)


def get_box_at_pixel(x, y):
    for boxx in range(config.BOARDWIDTH):
        for boxy in range(config.BOARDHEIGHT):
            left, top = left_top_coords_of_box(boxx, boxy)
            box_rect = pygame.Rect(left, top, config.BOXSIZE, config.BOXSIZE)
            if box_rect.collidepoint(x, y):
                return (boxx, boxy)
    return (None, None)


def get_shape_and_color(board, boxx, boxy):
    # shape value for x, y spot is stored in board[x][y][0]
    # color value for x, y spot is stored in board[x][y][1]
    return board[boxx][boxy][0], board[boxx][boxy][1]
