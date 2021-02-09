import operations
from interface import *


def toggle_color(keys_pressed):
    if keys_pressed[pygame.K_UP]:
        if in_focus[0] == blue or in_focus[0] == green or in_focus[0] == orange or in_focus[0] == red:
            in_focus[0] = yellow
        elif in_focus[0] == yellow:
            in_focus[0] = white
        elif in_focus[0] == white:
            in_focus[0] = blue

    elif keys_pressed[pygame.K_DOWN]:
        if in_focus[0] == blue or in_focus[0] == green or in_focus[0] == orange or in_focus[0] == red:
            in_focus[0] = white
        elif in_focus[0] == white:
            in_focus[0] = yellow
        elif in_focus[0] == yellow:
            in_focus[0] = blue

    elif keys_pressed[pygame.K_RIGHT]:
        if in_focus[0] == blue or in_focus[0] == yellow or in_focus[0] == white:
            in_focus[0] = red
        elif in_focus[0] == red:
            in_focus[0] = green
        elif in_focus[0] == green:
            in_focus[0] = orange
        elif in_focus[0] == orange:
            in_focus[0] = blue

    elif keys_pressed[pygame.K_LEFT]:
        if in_focus[0] == blue or in_focus[0] == yellow or in_focus[0] == white:
            in_focus[0] = orange
        elif in_focus[0] == orange:
            in_focus[0] = green
        elif in_focus[0] == green:
            in_focus[0] = red
        elif in_focus[0] == red:
            in_focus[0] = blue


def get_move(keys_pressed):
    if keys_pressed[pygame.K_u]:
        if keys_pressed[pygame.K_RSHIFT] or keys_pressed[pygame.K_LSHIFT]:
            operations.operation("U'")
        else:
            operations.operation("U")

    if keys_pressed[pygame.K_d]:
        if keys_pressed[pygame.K_RSHIFT] or keys_pressed[pygame.K_LSHIFT]:
            operations.operation("D'")
        else:
            operations.operation("D")

    if keys_pressed[pygame.K_r]:
        if keys_pressed[pygame.K_RSHIFT] or keys_pressed[pygame.K_LSHIFT]:
            operations.operation("R'")
        else:
            operations.operation("R")

    if keys_pressed[pygame.K_l]:
        if keys_pressed[pygame.K_RSHIFT] or keys_pressed[pygame.K_LSHIFT]:
            operations.operation("L'")
        else:
            operations.operation("L")

    if keys_pressed[pygame.K_f]:
        if keys_pressed[pygame.K_RSHIFT] or keys_pressed[pygame.K_LSHIFT]:
            operations.operation("F'")
        else:
            operations.operation("F")

    if keys_pressed[pygame.K_b]:
        if keys_pressed[pygame.K_RSHIFT] or keys_pressed[pygame.K_LSHIFT]:
            operations.operation("B'")
        else:
            operations.operation("B")
