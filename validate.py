from interface import *


def invalid_colors(string):
    for char in string:
        if char == 'b' or char == 'g' or char == 'y' or char == 'o' or char == 'r' or char == 'w':
            return False
        else:
            return True


def valid_cube():
    # Dimension checks
    if len(cube) != 6:
        print("A cube is supposed to have 6 faces")
        return False

    centers = []
    edges = []
    corners = []

    for num in range(0, 6):
        centers.append(0)
        edges.append(0)
        corners.append(0)

    # Counting number of colors on the centers, edges and corners
    for face in cube:
        for num in range(0, 9):
            color_code = color_enum(face[num])

            if color_code != -1:
                piece_code = piece_enum(num)

                if piece_code == 0:
                    centers[color_code] += 1
                elif piece_code == 1:
                    edges[color_code] += 1
                elif piece_code == 2:
                    corners[color_code] += 1
                else:
                    print("Invalid piece encountered")
                    return False

            else:
                print("Invalid color encountered")
                return False

    # Checking number of colors on centers, edges and corners
    for num in range(0, 6):
        if centers[num] != 1:
            print("Invalid number of colors on the center")
            return False
        elif edges[num] != 4:
            print("Invalid number of colors on the edges")
            return False
        elif corners[num] != 4:
            print("Invalid number of colors on the corners")
    return True
