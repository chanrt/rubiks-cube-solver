from interface import *
import config


def operation(op):

    front_face = cube[blue]
    top_face = cube[config.top_reference(blue)]

    configs = config.faces_orientation(blue)
    left_face = cube[configs[left]]
    right_face = cube[configs[right]]
    back_face = cube[configs[back]]
    down_face = cube[configs[down]]

    if op == "U":
        front_temp = front_face[0:9]
        replace_continuous_colors(front_face, right_face, 0, 3)
        replace_continuous_colors(right_face, back_face, 0, 3)
        replace_continuous_colors(back_face, left_face, 0, 3)
        replace_continuous_colors(left_face, front_temp, 0, 3)
        clockwise(top_face)

    elif op == "U'":
        front_temp = front_face[0:9]
        replace_continuous_colors(front_face, left_face, 0, 3)
        replace_continuous_colors(left_face, back_face, 0, 3)
        replace_continuous_colors(back_face, right_face, 0, 3)
        replace_continuous_colors(right_face, front_temp, 0, 3)
        counter_clockwise(top_face)

    elif op == "D":
        front_temp = front_face[0:9]
        replace_continuous_colors(front_face, left_face, 6, 9)
        replace_continuous_colors(left_face, back_face, 6, 9)
        replace_continuous_colors(back_face, right_face, 6, 9)
        replace_continuous_colors(right_face, front_temp, 6, 9)
        clockwise(down_face)

    elif op == "D'":
        front_temp = front_face[0:9]
        replace_continuous_colors(front_face, right_face, 6, 9)
        replace_continuous_colors(right_face, back_face, 6, 9)
        replace_continuous_colors(back_face, left_face, 6, 9)
        replace_continuous_colors(left_face, front_temp, 6, 9)
        counter_clockwise(down_face)

    elif op == "R":
        front_temp = front_face[0:9]
        replace_colors(front_face, down_face, [2, 5, 8])
        replace_colors_complex(down_face, back_face, [[0, 8], [3, 5], [6, 2]])
        replace_colors_complex(back_face, top_face, [[8, 0], [5, 3], [2, 6]])
        replace_colors(top_face, front_temp, [2, 5, 8])
        clockwise(right_face)

    elif op == "R'":
        front_temp = front_face[0:9]
        replace_colors(front_face, top_face, [2, 5, 8])
        replace_colors_complex(top_face, back_face, [[0, 8], [3, 5], [6, 2]])
        replace_colors_complex(back_face, down_face, [[8, 0], [5, 3], [2, 6]])
        replace_colors(down_face, front_temp, [2, 5, 8])
        counter_clockwise(right_face)

    elif op == "L":
        front_temp = front_face[0:9]
        replace_colors(front_face, top_face, [0, 3, 6])
        replace_colors_complex(top_face, back_face, [[2, 6], [5, 3], [8, 0]])
        replace_colors_complex(back_face, down_face, [[6, 2], [3, 5], [0, 8]])
        replace_colors(down_face, front_temp, [0, 3, 6])
        clockwise(left_face)

    elif op == "L'":
        front_temp = front_face[0:9]
        replace_colors(front_face, down_face, [0, 3, 6])
        replace_colors_complex(down_face, back_face, [[2, 6], [5, 3], [8, 0]])
        replace_colors_complex(back_face, top_face, [[6, 2], [3, 5], [0, 8]])
        replace_colors(top_face, front_temp, [0, 3, 6])
        counter_clockwise(left_face)

    elif op == "F":
        top_temp = top_face[0:9]
        replace_colors_complex(top_face, left_face, [[2, 8], [5, 7], [8, 6]])
        replace_colors_complex(left_face, down_face, [[0, 2], [1, 5], [2, 8]])
        replace_colors_complex(down_face, right_face, [[0, 2], [3, 1], [6, 0]])
        replace_colors_complex(right_face, top_temp, [[6, 0], [7, 3], [8, 6]])
        clockwise(front_face)

    elif op == "F'":
        top_temp = top_face[0:9]
        replace_colors_complex(top_face, right_face, [[0, 6], [3, 7], [6, 8]])
        replace_colors_complex(right_face, down_face, [[0, 6], [1, 3], [2, 0]])
        replace_colors_complex(down_face, left_face, [[2, 0], [5, 1], [8, 2]])
        replace_colors_complex(left_face, top_temp, [[6, 8], [7, 5], [8, 2]])
        counter_clockwise(front_face)

    elif op == "B":
        top_temp = top_face[0:9]
        replace_colors_complex(top_face, right_face, [[2, 0], [5, 1], [8, 2]])
        replace_colors_complex(right_face, down_face, [[6, 8], [7, 5], [8, 2]])
        replace_colors_complex(down_face, left_face, [[0, 6], [3, 7], [6, 8]])
        replace_colors_complex(left_face, top_temp, [[0, 6], [1, 3], [2, 0]])
        clockwise(back_face)

    elif op == "B'":
        top_temp = top_face[0:9]
        replace_colors_complex(top_face, right_face, [[2, 0], [5, 1], [8, 2]])
        replace_colors_complex(right_face, down_face, [[6, 8], [7, 5], [8, 2]])
        replace_colors_complex(down_face, left_face, [[0, 6], [3, 7], [6, 8]])
        replace_colors_complex(left_face, top_temp, [[0, 6], [1, 3], [2, 0]])
        counter_clockwise(back_face)

    elif op == "LF":
        lateral_flip(top_face)


def replace_colors_complex(target_face, source_face, point_maps):
    for point_map in point_maps:
        target_face[point_map[1]] = source_face[point_map[0]]


def replace_colors(target_face, source_face, points):
    for point in points:
        target_face[point] = source_face[point]


def replace_continuous_colors(target_face, source_face, start, stop):
    for num in range(start, stop):
        target_face[num] = source_face[num]


def clockwise(face):
    temp = face[0:9]
    face[0] = temp[6]
    face[1] = temp[3]
    face[2] = temp[0]
    face[3] = temp[7]
    face[4] = temp[4]
    face[5] = temp[1]
    face[6] = temp[8]
    face[7] = temp[5]
    face[8] = temp[2]


def counter_clockwise(face):
    temp = face[0:9]
    face[0] = temp[2]
    face[1] = temp[5]
    face[2] = temp[8]
    face[3] = temp[1]
    face[4] = temp[4]
    face[5] = temp[7]
    face[6] = temp[0]
    face[7] = temp[3]
    face[8] = temp[6]


def lateral_flip(face):
    temp = face[0:9]
    face[0] = temp[8]
    face[1] = temp[7]
    face[2] = temp[6]
    face[3] = temp[5]
    face[4] = temp[4]
    face[5] = temp[3]
    face[6] = temp[2]
    face[7] = temp[1]
    face[8] = temp[0]
