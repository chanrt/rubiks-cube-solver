from interface import *


def top_reference(front):
    if front == blue or front == green or front == orange or front == red:
        return yellow
    if front == yellow or white:
        return white


def faces_orientation(front):
    if front == blue:
        return [orange, red, green, white]
    elif front == green:
        return [red, orange, blue, white]
    elif front == yellow:
        return [red, orange, white, green]
    elif front == orange:
        return [green, blue, red, white]
    elif front == red:
        return [blue, green, orange, white]
    elif front == white:
        return [orange, red, yellow, green]
