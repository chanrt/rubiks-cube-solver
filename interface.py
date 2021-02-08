import pygame

# Cube
colors = ["blue", "green", "yellow", "orange", "red", "white"]
cube = []
cube_state = []
in_focus = []

# Colors
blue = 0
green = 1
yellow = 2
orange = 3
red = 4
white = 5

# Faces
left = 0
right = 1
back = 2
down = 3


def show_cube():
    for face_num in range(0, 6):
        print("{} face:".format(colors[face_num]))
        face = cube[face_num]

        for row in range(0, 3):
            print("{} {} {} ".format(face[3 * row], face[3 * row + 1], face[3 * row + 2]))


def color_letter(color):
    if color == blue:
        return 'b'
    elif color == green:
        return 'g'
    elif color == yellow:
        return 'y'
    elif color == orange:
        return 'o'
    elif color == red:
        return 'r'
    elif color == white:
        return 'w'


def color_enum(color):
    if color == 'b':
        return blue
    elif color == 'g':
        return green
    elif color == 'y':
        return yellow
    elif color == 'o':
        return orange
    elif color == 'r':
        return red
    elif color == 'w':
        return white
    else:
        return -1


def convert_to_letter():
    if cube_state[0] != "L":
        cube_state[0] = "L"
        for face in cube:
            for num in range(0, 9):
                face[num] = color_letter(face[num])


def convert_to_num():
    if cube_state[0] != "N":
        cube_state[0] = "N"
        for face in cube:
            for num in range(0, 9):
                face[num] = color_enum(face[num])


def piece_enum(num):
    if num == 4:
        return 0
    elif num == 1 or num == 3 or num == 5 or num == 7:
        return 1
    elif num == 0 or num == 2 or num == 6 or num == 8:
        return 2
    else:
        return -1


def get_color(color):
    if color == blue:
        return pygame.Color("blue")
    elif color == green:
        return pygame.Color("green")
    elif color == yellow:
        return pygame.Color("yellow")
    elif color == orange:
        return pygame.Color("orange")
    elif color == red:
        return pygame.Color("red")
    elif color == white:
        return pygame.Color("white")
    else:
        return pygame.Color("red")
