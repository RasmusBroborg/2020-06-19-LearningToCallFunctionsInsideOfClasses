"""

Testing if I can create Tic-Tac-Toe without following a guide or
googling solutions for

"""


import pygame
import sys

COLOR_BLACK = (0, 0, 0)
COLOR_GREY = (125, 125, 125)
COLOR_WHITE = (255, 255, 255)

DISPLAY_WIDTH = 300
DISPLAY_HEIGHT = 300
FPS = 10


def debug_board(board_list):
    print(board_list)


class Board:
    def __init__(self):
        self.board_list = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

        # Corresponds to the board list. Marks top corner of each
        # square on board.
        self.board_display_pos = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

        self.player_x = "X"
        self.player_o = "O"
        self.current_player = self.player_x

        self.num_of_wins_player_x = 0
        self.num_of_wins_player_o = 0

        self.round = 0
        self.turn = 1

        self.sel_row = None
        self.sel_column = None

    def check_board_availability(self, row, column):

        if self.board_list[row][column] != "":
            print("Not available. Contains: {}".format(
                self.board_list[row][column]))
            return False

        else:
            print("Available for selection.")
            return True

    def next_turn(self):

        print("Updating turn.")
        # Switching players:
        if self.current_player == self.player_x:
            self.current_player = self.player_o
        elif self.current_player == self.player_o:
            self.current_player = self.player_x
        elif self.current_player == None:
            self.current_player = self.player_x

        # Increment turn count:
        self.turn += 1

        # Inform player about turn:
        print("Turn #{}. Player {} turn:".format(
            self.turn, self.current_player))

    def next_round(self):
        # Resetting board
        self.board_list = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

        # Increment round and resetting turn count:
        self.round += 1
        self.turn = 1
        self.current_player = self.player_x

        print("Round {}.".format(
            self.round))

        print("Turn #{}. Player {} turn:".format(
            self.turn, self.current_player))

    def player_win(self, current_player):
        if current_player == self.player_o:
            self.num_of_wins_player_o += 1
        if current_player == self.player_x:
            self.num_of_wins_player_x += 1

        print("\nPlayer {} wins the round!\n".format(self.current_player))


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
        print("Mouse x pos is {}, and mouse y pos is {}.".format(
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

        print("Based on mouse input, Row is {} and Column is {}.".format(
            sel_row, sel_pos_in_row))

        return sel_row, sel_pos_in_row


def check_win(board, sel_player):
    """
    check_win()-func returns True if any of the nested functions return True
    """

    def get_winning_combination(board, sel_player):
        win_combo = []
        for i in range(len(board)):
            win_combo.append(sel_player)

        print('\nWinning combination is: {}\n'.format(win_combo))
        return win_combo

    def check_rows_for_win(board, winning_combo):
        for i in range(len(board)):

            print('Row #{} contains: {}'.format(i, board[i]))

            if board[i] == winning_combo:
                print("Horizontal win.")
                return True

    def check_columns_for_win(board, winning_combo):
        for i in range(len(board)):

            column = [board[0][i]] + \
                [board[1][i]] + [board[2][i]]

            print('Column #{} contains: {}'.format(i, column))

            if column == winning_combo:
                print("Vertical win.")
                return True

    def check_diagonals_for_win(board, winning_combo):

        # Diagonal top to bottom
        diagonal_top_to_bottom = []
        for i in range(len(board)):
            diagonal_top_to_bottom.insert(i, board[i][i])
        print('Diagonal top to bottom contains {}'.format(diagonal_top_to_bottom))

        # Diagonal bottom to top
        diagonal_bottom_to_top = []
        for i in range(len(board)):
            board_index = (len(board) - i - 1)

            diagonal_bottom_to_top.insert(
                i, board[i][board_index])
        print('Diagonal bottom to top contains {}'.format(diagonal_bottom_to_top))

        if diagonal_top_to_bottom == winning_combo or diagonal_bottom_to_top == winning_combo:
            print("Diagonal win.")
            return True

    # Running the nested functions

    winning_combination = get_winning_combination(board, sel_player)
    row_win = check_rows_for_win(board, winning_combination)
    column_win = check_columns_for_win(board, winning_combination)
    diagonal_win = check_diagonals_for_win(board, winning_combination)

    if row_win == True or column_win == True or diagonal_win == True:
        print("Debug: WIN!")
        return True


def main():

    game_display = pygame.display.set_mode((DISPLAY_WIDTH,
                                            DISPLAY_HEIGHT))
    pygame.display.set_caption('Tic-Tac-Toe')

    board = Board()

    board.next_round()

    debug_board(board.board_list)

    while True:
        # Reset:

        # Game start:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Checks if mouse click on display surface (pygame event code 1025):
            if event.type == 1025:
                sel_square_pos = sel_square_position(pygame.mouse.get_pos())

                print("sel_square_pos contains value:".format(sel_square_pos))

                square_availability = board.check_board_availability(
                    sel_square_pos[0], sel_square_pos[1])

                if square_availability == True:

                    # Assign current player to the square:
                    board.board_list[sel_square_pos[0]
                                     ][sel_square_pos[1]] = board.current_player

                    print(board.board_list)

                    win_check = check_win(
                        board.board_list, board.current_player)

                    if win_check == True:
                        board.player_win(board.current_player)
                        board.next_round()
                    else:
                        board.next_turn()

                debug_board(board.board_list)

                # VISUALS

        draw_display(game_display)

        # pygame.display.flip()

        pygame.display.update()
        pygame.time.Clock().tick(FPS)


if __name__ == "__main__":
    main()
