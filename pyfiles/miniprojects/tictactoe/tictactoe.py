"""

Testing if I can create Tic-Tac-Toe in pygame using my current
knowledge of python/pygame, without following a guide / other
persons version of the game (no googling for Tic-Tac_Toe).

"""


import pygame
import sys

COLOR_BLACK = (0, 0, 0)
COLOR_GREY = (125, 125, 125)
COLOR_WHITE = (255, 255, 255)

DISPLAY_WIDTH = 300
DISPLAY_HEIGHT = 300
FPS = 10


def debug_board_status(board_list):
    print(board_list)


class Board:
    def __init__(self):
        self.board_list = [
            ["X", "X", "X"],
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

    def check_win(self):
        b_list = self.board_list
        player_winstring = self.current_player * 3

        # Check row matches current players string:
        if b_list[0][0] + b_list[0][1] + b_list[0][2] == player_winstring:
            return True

        # Check column win:

        # Check diagonal win

        if b_list[0] == 0:
            return True

        else:
            return False

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
            num_of_wins_player_o += 1
        if current_player == self.player_x:
            num_of_wins_player_x += 1


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


def main():

    game_display = pygame.display.set_mode((DISPLAY_WIDTH,
                                            DISPLAY_HEIGHT))
    pygame.display.set_caption('Tic-Tac-Toe')

    board = Board()

    board.next_round()

    debug_board_status(board.board_list)

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

                print("".format())

                if square_availability == True:

                    board.board_list[sel_square_pos[0]
                                     ][sel_square_pos[1]] = board.current_player

                    if board.check_win() == True:
                        board.player_win()
                        board.next_round()
                    else:
                        board.next_turn()

                debug_board_status(board.board_list)

                # VISUALS

        draw_display(game_display)

        # pygame.display.flip()

        pygame.display.update()
        pygame.time.Clock().tick(FPS)


if __name__ == "__main__":
    main()
