import pygame
import sys


class Board:
    def __init__(self):
        self.board_list = [
            ["", "", ""],
            ["", "X", ""],
            ["", "", ""]
        ]

    def check_board_availability(self, row, column):

        if self.board_list[row][column] != "":
            print("Not available. Contains: {}".format(
                self.board_list[row][column]))
        else:
            print("Available for selection.")


def draw_display(game_display):

    game_display.fill(COLOR_BLACK)
    # Drawing vertical lines:
    pygame.draw.aaline(game_display, COLOR_WHITE,
                       (int(DISPLAY_WIDTH * 0.33), 0),
                       (int(DISPLAY_WIDTH * 0.33), DISPLAY_HEIGHT))
    pygame.draw.aaline(game_display, COLOR_WHITE,
                       (int(DISPLAY_WIDTH * 0.66), 0),
                       (int(DISPLAY_WIDTH * 0.66), DISPLAY_HEIGHT))
    # Drawing horizontal lines:
    pygame.draw.aaline(game_display, COLOR_WHITE,
                       (0, int(DISPLAY_HEIGHT * 0.33)),
                       (DISPLAY_WIDTH, int(DISPLAY_HEIGHT * 0.33)))
    pygame.draw.aaline(game_display, COLOR_WHITE,
                       (0, int(DISPLAY_HEIGHT * 0.66)),
                       (DISPLAY_WIDTH, int(DISPLAY_HEIGHT * 0.66)))


def sel_square_position(m_pos):
    # Gets the list adress for the board squares based on the mouseclick pos.
    if m_pos != [[None], [None]]:
        print("Sel x pos is {}, and sel y pos is {}.".format(
            m_pos[0], m_pos[1]))

        # Get which row in board list from mouse click y pos:
        if m_pos[1] < 100 and m_pos[1] >= 0:
            sel_row = 0
        elif m_pos[1] < 200:
            sel_row = 1
        elif m_pos[1] < 301:
            sel_row = 2

        # Get which position in row from mouse click x pos:
        if m_pos[0] < 100 and m_pos[1] >= 0:
            sel_pos_in_row = 0
        elif m_pos[0] < 200:
            sel_pos_in_row = 1
        elif m_pos[0] < 301:
            sel_pos_in_row = 2

        print("Sel_row is {}, and sel_rowpos is {}.".format(
            sel_row, sel_pos_in_row))

        return sel_row, sel_pos_in_row


def main():

    DISPLAY_WIDTH = 300
    DISPLAY_HEIGHT = 300
    FPS = 10

    COLOR_BLACK = (0, 0, 0)
    COLOR_GREY = (125, 125, 125)
    COLOR_WHITE = (255, 255, 255)

    game_display = pygame.display.set_mode((DISPLAY_WIDTH,
                                            DISPLAY_HEIGHT))
    pygame.display.set_caption('Tic-Tac-Toe')

    board = Board()

    # basic_font = pygame.font.Font('freesansbold.ttf', 32)

    while True:
        # Reset:
        sel_row = None
        sel_pos_in_row = None

        # Game start:

        for event in pygame.event.get():
            print(event.type)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # If mouse click on display surface:
            if event.type == 1025:
                sel_square_pos = sel_square_position(pygame.mouse.get_pos())

                print(sel_square_pos)
                print(sel_square_pos[0])
                print(sel_square_pos[1])

                board.check_board_availability(
                    sel_square_pos[0], sel_square_pos[1])

        # VISUALS

        draw_display(game_display)

        # pygame.display.flip()

        pygame.display.update()
        pygame.time.Clock().tick(FPS)

        # board.reset()


if __name__ == "__main__":
    main()
