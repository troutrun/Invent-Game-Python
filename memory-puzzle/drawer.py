import pygame

import config
import boarder


def draw_icon(shape, color, boxx, boxy):
    # syntactic sugar
    quarter = int(config.BOXSIZE * 0.25)
    half = int(config.BOXSIZE * 0.5)

    # get pixel coords from board coords
    left, top = boarder.left_top_coords_of_box(boxx, boxy)

    # Draw the shapes
    if shape == config.DONUT:
        pygame.draw.circle(config.DISPLAYSURF, color, (left + half, top + half), half - 5)
        pygame.draw.circle(config.DISPLAYSURF, config.BGCOLOR, (left + half, top + half), quarter - 5)
    elif shape == config.SQUARE:
        pygame.draw.rect(config.DISPLAYSURF, color, (left + quarter, top + quarter, config.BOXSIZE - half, config.BOXSIZE - half))
    elif shape == config.DIAMOND:
        pygame.draw.polygon(config.DISPLAYSURF, color, ((left + half, top), (left + config.BOXSIZE - 1, top + half), (left + half, top + config.BOXSIZE - 1), (left, top + half)))
    elif shape == config.LINES:
        for i in range(0, config.BOXSIZE, 4):
            pygame.draw.line(config.DISPLAYSURF, color, (left, top + i), (left + i, top))
            pygame.draw.line(config.DISPLAYSURF, color, (left + i, top + config.BOXSIZE - 1), (left + config.BOXSIZE - 1, top + i))
    elif shape == config.OVAL:
        pygame.draw.ellipse(config.DISPLAYSURF, color, (left, top + quarter, config.BOXSIZE, half))


def draw_box_covers(board, boxes, coverage):
    # Draws boxes being covered/revealed. "boxes" is a list
    # of two-item lists, which have the x & y spot of the box.
    for box in boxes:
        left, top = boarder.left_top_coords_of_box(box[0], box[1])
        pygame.draw.rect(config.DISPLAYSURF, config.BGCOLOR, (left, top, config.BOXSIZE, config.BOXSIZE))
        shape, color = boarder.get_shape_and_color(board, box[0], box[1])
        draw_icon(shape, color, box[0], box[1])
        if coverage > 0: # only draw the cover if there is an coverage
            pygame.draw.rect(config.DISPLAYSURF, config.BOXCOLOR, (left, top, coverage, config.BOXSIZE))
    pygame.display.update()
    config.FPSCLOCK.tick(config.FPS)


def draw_board(board, revealed):
    # Draws all of the boxes in their covered or revealed state.
    for boxx in range(config.BOARDWIDTH):
        for boxy in range(config.BOARDHEIGHT):
            left, top = boarder.left_top_coords_of_box(boxx, boxy)
            if not revealed[boxx][boxy]:
                # Draw a covered box.
                pygame.draw.rect(config.DISPLAYSURF, config.BOXCOLOR, (left, top, config.BOXSIZE, config.BOXSIZE))
            else:
                # Draw the (revealed) icon.
                shape, color = boarder.get_shape_and_color(board, boxx, boxy)
                draw_icon(shape, color, boxx, boxy)


def draw_highlight_box(boxx, boxy):
    left, top = boarder.left_top_coords_of_box(boxx, boxy)
    pygame.draw.rect(config.DISPLAYSURF, config.HIGHLIGHTCOLOR, (left - 5, top - 5, config.BOXSIZE + 10, config.BOXSIZE + 10), 4)
