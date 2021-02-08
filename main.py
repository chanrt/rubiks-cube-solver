from interface import *
import validate
import operations
import pygame

pygame.init()
screen = pygame.display.set_mode([820, 610])
clock = pygame.time.Clock()
square_length = 66


def input_cube():
    print("For each face, enter the colors in the given order:")
    print("1,2,3, (next row) 4,5,6, (next row) 7,8,9")
    print("Example: (white face) yywgwobrw")

    for color in colors:

        # Perspective decider
        if color == "blue" or color == "green" or color == "orange" or color == "red":
            print("Perspective: {} on front and yellow on top".format(color))
        elif color == "yellow":
            print("Perspective: yellow on front and blue on top")
        elif color == "white":
            print("Perspective: white on front and blue on top")

        while True:
            raw_input = input("Enter colors: ")

            # String checks
            if len(raw_input) != 9:
                print("Each face should contain exactly nine colors")
            elif raw_input[4] != color[0]:
                print("Please enter the colors on the {} face".format(color))
            elif validate.invalid_colors(raw_input):
                print("Please enter only valid colors: (b,g,y,o,r,w)")
            else:
                raw_face = []
                for letter in raw_input:
                    raw_face.append(letter)
                break

        cube.append(raw_face)

    print(cube)

    if validate.valid_cube():
        cube_state.append("L")
        in_focus.append(blue)
        operations.operation("LF", blue)

        show_cube()
        convert_to_num()
    else:
        exit()


def render_cube():
    running = True

    while running:
        screen.fill(pygame.Color("black"))
        clock.tick(10)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_u]:
            if keys_pressed[pygame.K_RSHIFT] or keys_pressed[pygame.K_LSHIFT]:
                operations.operation("U'", white)
            else:
                operations.operation("U", white)

        if keys_pressed[pygame.K_d]:
            if keys_pressed[pygame.K_RSHIFT] or keys_pressed[pygame.K_LSHIFT]:
                operations.operation("D'", white)
            else:
                operations.operation("D", white)

        if keys_pressed[pygame.K_r]:
            if keys_pressed[pygame.K_RSHIFT] or keys_pressed[pygame.K_LSHIFT]:
                operations.operation("R'", white)
            else:
                operations.operation("R", white)

        if keys_pressed[pygame.K_l]:
            if keys_pressed[pygame.K_RSHIFT] or keys_pressed[pygame.K_LSHIFT]:
                operations.operation("L'", white)
            else:
                operations.operation("L", white)

        if keys_pressed[pygame.K_f]:
            if keys_pressed[pygame.K_RSHIFT] or keys_pressed[pygame.K_LSHIFT]:
                operations.operation("F'", white)
            else:
                operations.operation("F", white)

        for face_num in range(0, 6):
            face = cube[face_num]

            if face[4] == orange or face[4] == blue or face[4] == red or face[4] == green:
                y_offset = 205
            elif face[4] == yellow:
                y_offset = 0
            else:
                y_offset = 410

            if face[4] == yellow or face[4] == blue or face[4] == white:
                x_offset = 205
            elif face[4] == orange:
                x_offset = 0
            elif face[4] == red:
                x_offset = 410
            else:
                x_offset = 615

            for color in range(0, 9):
                if color == 0 or color == 3 or color == 6:
                    x = 0
                elif color == 1 or color == 4 or color == 7:
                    x = square_length + 2
                else:
                    x = 2 * square_length + 4

                if -1 < color < 3:
                    y = 0
                elif 2 < color < 6:
                    y = square_length + 2
                else:
                    y = 2 * square_length + 4

                pygame.draw.rect(screen, get_color(face[color]),
                                 [x_offset + x, y_offset + y, square_length, square_length])

        pygame.display.flip()


if __name__ == "__main__":
    input_cube()
    render_cube()
    pygame.quit()
