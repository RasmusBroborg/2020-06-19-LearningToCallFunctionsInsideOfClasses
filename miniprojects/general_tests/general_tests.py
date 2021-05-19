import pygame

DISPLAY_WIDTH = 100 * 3
DISPLAY_HEIGHT = 100 * 3
COLOR_WHITE = (255, 255, 255)

board_list = [
    ["X", "X", ""],
    ["", "O", "X"],
    ["", "", ""]
]

game_display = pygame.display.set_mode((DISPLAY_WIDTH,
                                        DISPLAY_HEIGHT))
# ------- FUNCTION BELOW -------

# Needs to iterate for each position in list:


def draw_symbols(display_surface, board_list):

    def draw_x(row, column):
        print('Drawing X')
        pygame.draw.aaline(display_surface, COLOR_WHITE,
                           (0, int(DISPLAY_HEIGHT * 0.66)),
                           (DISPLAY_WIDTH, int(DISPLAY_HEIGHT * 0.66)))

    def draw_o(row, column):
        print('Drawing O')
        pass

    for row_index in range(len(board_list)):
        for column_index in range(len(board_list[0])):

            symbol = board_list[row_index][column_index]

            print("Row #{} & Column #{} contains: {}".format(
                row_index, column_index, symbol))

            if board_list[row_index][column_index] == "X":
                draw_x(row_index, column_index)
            elif board_list[row_index][column_index] == "O":
                draw_o(row_index, column_index)


draw_symbols(game_display, board_list)

pygame.quit()


# draw_symbols(game_display, current_player, board_row, board_column)
