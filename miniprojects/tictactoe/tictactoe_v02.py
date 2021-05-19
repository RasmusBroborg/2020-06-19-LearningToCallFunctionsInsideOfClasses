"""

Second attempt at creating Tic-Tac-Toe without following a guide or
googling solutions .

"""

import pygame
import sys

pygame.init()

class Tictactoe:

    # Display setup and initialization

    # Game variables initialization and calling of main method
    def __init__(self):

        # Colors

        self.COLOR_BLACK = (0, 0, 0)
        self.COLOR_WHITE = (255, 255, 255)

        # Display constants

        self.BOARD_WIDTH = 150 * 3
        self.BOARD_HEIGHT = 150 * 3
        self.MENU_BAR_WIDTH = self.BOARD_WIDTH
        self.MENU_BAR_HEIGHT = int(self.BOARD_HEIGHT * 0.20)
        self.DISPLAY_WIDTH = self.BOARD_WIDTH + self.MENU_BAR_WIDTH
        self.DISPLAY_HEIGHT = self.BOARD_HEIGHT + self.MENU_BAR_HEIGHT
        self.FPS = 10

        self.game_display = pygame.display.set_mode((self.DISPLAY_WIDTH,
                                                     self.DISPLAY_HEIGHT))
        pygame.display.set_caption('Tic-Tac-Toe.')

        # class variables

        self.board_list = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

        self.turn = 0
        self.round = 0
        self.available_players = ["X", "O"]
        self.current_player = "X"
        self.selected_row = None
        self.selected_column = None
        self.playerX_wins = 0
        self.playerO_wins = 0

        self.main()

    def check_mouse_click(self, event_type):
        if event_type == 1025:
            return True
        else:
            return False

    def convert_mouse_pos_to_board_index(self, m_pos):
        # m_pos short for mouse x/y positions

        print("Mouse x pos is {}, and mouse y pos is {}.".format(
            m_pos[0], m_pos[1]))

        # Get which row in board list from mouse click y pos:
        if m_pos[1] < 100 and m_pos[1] >= 0:
            row = 0
        elif m_pos[1] < 200:
            row = 1
        elif m_pos[1] < 301:
            row = 2

        # Get which position in row from mouse click x pos:
        if m_pos[0] < 100 and m_pos[1] >= 0:
            column = 0
        elif m_pos[0] < 200:
            column = 1
        elif m_pos[0] < 301:
            column = 2

        print("Based on mouse input, Row is {} and Column is {}.".format(
            row, column))

        self.selected_column = column
        self.selected_row = row

    def check_board_availability(self):
        if self.board_list[self.selected_row][self.selected_column] != "":
            return False
        else:
            return True

    def assign_current_player_to_board(self):
        self.board_list[self.selected_row][selected_column] = self.current_player

    def check_if_win(self):

        def get_winning_combination(board, sel_player):
            win_combo = []
            for i in range(len(board)):
                win_combo.append(sel_player)
            return win_combo

        def check_rows_for_win(board, winning_combo):
            for i in range(len(board)):
                if board[i] == winning_combo:
                    return True

        def check_columns_for_win(board, winning_combo):
            for i in range(len(board)):
                column = [board[0][i]] + \
                    [board[1][i]] + [board[2][i]]
                if column == winning_combo:
                    print("Vertical win.")
                    return True

        def check_diagonals_for_win(board, winning_combo):
            # Diagonal top to bottom
            diagonal_top_to_bottom = []
            for i in range(len(board)):
                diagonal_top_to_bottom.insert(i, board[i][i])

            # Diagonal bottom to top
            diagonal_bottom_to_top = []
            for i in range(len(board)):
                board_index = (len(board) - i - 1)
                diagonal_bottom_to_top.insert(
                    i, board[i][board_index])

            if diagonal_top_to_bottom == winning_combo or diagonal_bottom_to_top == winning_combo:
                print("Diagonal win.")
                return True
            else:
                return False

        winning_combination = get_winning_combination(
            self.board_list, self.current_player)
        row_win = check_rows_for_win(self.board_list, winning_combination)
        column_win = check_columns_for_win(
            self.board_list, winning_combination)
        diagonal_win = check_diagonals_for_win(
            self.board_list, winning_combination)

        if row_win == True or column_win == True or diagonal_win == True:
            return True

    def add_win_to_current_player(self):

        for player in self.available_players:
            if self.current_player == "X":
                self.playerX_wins += 1
            elif self.current_player == "Y":
                self.playerX_wins += 1

    def update_next_round(self):
        self.round += 1
        self.turn = 1

    def update_next_turn(self):
        self.turn += 1

    def draw_display(self):

        font = pygame.font.Font('freesansbold.ttf', 32)

        self.game_display.fill(self.COLOR_BLACK)

        # Drawing vertical lines:
        pygame.draw.aaline(self.game_display, self.COLOR_WHITE,
                           (int(self.BOARD_WIDTH * 0.33), 0),
                           (int(self.BOARD_WIDTH * 0.33), self.BOARD_HEIGHT))
        pygame.draw.aaline(self.game_display, self.COLOR_WHITE,
                           (int(self.BOARD_WIDTH * 0.66), 0),
                           (int(self.BOARD_WIDTH * 0.66), self.BOARD_HEIGHT))
        # Drawing horizontal lines:
        pygame.draw.aaline(self.game_display, self.COLOR_WHITE,
                           (0, int(self.BOARD_HEIGHT * 0.33)),
                           (self.BOARD_WIDTH, int(self.BOARD_HEIGHT * 0.33)))
        pygame.draw.aaline(self.game_display, self.COLOR_WHITE,
                           (0, int(self.BOARD_HEIGHT * 0.66)),
                           (self.BOARD_WIDTH, int(self.BOARD_HEIGHT * 0.66)))

        # Iterates through the board_list and draws the symbols on the visual
        # board:

        for row_index in range(len(self.board_list)):
            for column_index in range(len(self.board_list[0])):
                symbol = self.board_list[row_index][column_index]

                # Magic numbers represent the pixel offset
                x_pos = column_index * 100 + 50
                y_pos = row_index * 100 + 50

                symbol_text = font.render(
                    symbol, True, self.COLOR_WHITE, self.COLOR_BLACK)
                textRect = symbol_text.get_rect()
                textRect.center = (x_pos, y_pos)

                self.game_display.blit(symbol_text, textRect)

    def main(self):

        while True:

            # Game start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Game logic step by step:
                if self.check_mouse_click(event) == True:
                    self.convert_mouse_pos_to_board_index()

                    if self.check_board_availability() == True:
                        self.assign_current_player_to_board()

                        if self.check_if_win() == True:
                            self.add_win_to_current_player()
                            self.update_next_round()

                        elif self.turn >= 9:
                            self.update_next_round()

                        else:
                            self.update_next_turn()

                    debug_board(board.board_list)

            self.draw_display()
# VISUALS

            #draw_display(game_display, board.board_list)

            pygame.display.update()
            pygame.time.Clock().tick(self.FPS)


if __name__ == "__main__":
    Tictactoe()
