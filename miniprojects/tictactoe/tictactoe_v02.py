"""
Second attempt at creating Tic-Tac-Toe without following a guide or
googling solutions .

Testing the ability to run the game within a single class.

"""

import pygame
import sys

class Tictactoe:

    def __init__(self):

        pygame.init()

        # Attributes related to game logic:
        self.board_list = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

        self.round = 0
        self.turn = 0

        self.available_players = ("X", "O")
        self.current_player = "X"

        self.playerO_wins = 0
        self.playerX_wins = 0

        # Attributes related to screen:
        self.menu_bar_offset = 50
        self.game_rectangle_length = 150
        self.screen_width = self.game_rectangle_length * 3
        self.screen_height = self.game_rectangle_length * 3 + self.menu_bar_offset
        self.screen = pygame.display.set_mode((self.screen_width,
                                               self.screen_height))
        pygame.display.set_caption('Tic-Tac-Toe.')

        # Variables
        self.mouse_pos = None
        self.board_index = [None, None]

    def switch_player(self):
        # Method
        if self.current_player == self.available_players[0]:
            self.current_player = self.available_players[1]
        elif self.current_player == self.available_players[1]:
            self.current_player = self.available_players[0]
        print("Switching to player {}.".format(
            self.current_player))

    def next_turn(self):
        print("\nUpdating to next turn.")
        self.turn += 1
        print("""Incrementing turn count to {}.""".format(
            self.turn))

    def next_round(self):
        self.board_list = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]
        self.round += 1
        self.turn = 1
        print("""\n
Resetting board to empty string values.
Incrementing round count to {}. Resetting turn count to {}.\n""".format(self.round, self.turn))

    #'Check if' methods returns True/Fals

    def check_if_win(self):
        print("Checking if move resulted in win in nested functions:")
        ref_win_list = []

        # Nested methods returns True if win is found:
        def append_win_combination_to_win_list():
            for i in range(len(self.board_list)):
                ref_win_list.append(self.current_player)
            print("\n     Winning combination is {}.".format(ref_win_list))

        def check_rows_and_columns_for_win():
            print("\n     Checking rows and columns for win")
            for first_index in range(len(self.board_list)):

                row_list = []
                column_list = []

                for second_index in range(len(self.board_list)):
                    row_list.append(self.board_list[first_index][second_index])
                    column_list.append(
                        self.board_list[second_index][first_index])

                    if len(row_list) == len(ref_win_list):
                        print(
                            "     - Row #{} contains: {}".format(first_index, row_list))
                        print(
                            "     - Column #{} contains: {}".format(first_index, column_list))
                    if row_list == ref_win_list or column_list == ref_win_list:
                        print("     - Winning combination found. Returning True.")
                        return True
            print(
                "     No winning combinations found in rows or columns. Returning False.")
            return False

        def check_diagonals_for_win():
            print("\n     Checking diagonals for win:")

            diagonal_top_bot = []
            diagonal_bot_top = []

            for index in range(len(self.board_list)):
                diagonal_top_bot.append(
                    self.board_list[index][index])

                # -1 to compensate for index offset
                diagonal_bot_top.append(
                    self.board_list[len(self.board_list) - index - 1][index])

            print("     - Diagonal top to bot contains: {}.".format(diagonal_top_bot))
            print("     - Diagonal bot to top contains: {}.".format(diagonal_bot_top))

            if diagonal_top_bot == ref_win_list or diagonal_bot_top == ref_win_list:
                print("     - Winning combination found in diagonals. Returning True.")
                return True
            else:
                print(
                    "     No winning combinations found in diagonals. Returning False.\n")
                return False

        append_win_combination_to_win_list()
        if check_rows_and_columns_for_win() == True or check_diagonals_for_win() == True:
            print("     Nested functions found win. Parent function returns True.")
            return True

        print("     No wins found in nested functions. Parent function returns False.")
        return False

    def check_if_draw(self):
        print("Checking if draw...")
        if self.turn >= 9:
            print("It's a draw! Returning True.")
            return True
        print("No draw. Returning False.")
        return False

    def player_win(self):
        if self.current_player == self.available_players[0]:
            self.playerX_wins += 1
        elif self.current_player == self.available_players[1]:
            self.playerO_wins += 1

        print("""Player {} wins the round! Incrementing player win score.""".format(
            self.current_player))

    def check_if_mouseclick_on_board(self, event_type):
        if event_type == 1025:
            print("Checking if mouseclick is within the board bounds.")
            self.mouse_pos = pygame.mouse.get_pos()
            print("Mouseclick detected at x pos {}, and y pos {}.".format(
                self.mouse_pos[0], self.mouse_pos[1]))

            if self.mouse_pos[1] < self.menu_bar_offset:
                print("Position is outside of board bounds. Unvalid selection.\n")
                return False
            else:
                print("Position is within the board bounds. Returning True.")
                return True
        return False

    def convert_mouse_pos_to_board_index(self):
        print("Converting mouse pos to board index.")

        def assign_row_index():
            for i in range(len(self.board_list)):
                if self.mouse_pos[1] - self.menu_bar_offset <= self.game_rectangle_length * (i + 1):
                    print("Mouse y pos {} corresponds to row index {}.".format(
                        self.mouse_pos[1], i))
                    self.board_index[0] = i
                    break

        def assign_column_index():
            for i in range(len(self.board_list)):
                if self.mouse_pos[0] <= self.game_rectangle_length * (i + 1):
                    print("Mouse y pos {} corresponds to column index {}.".format(
                        self.mouse_pos[0], i))
                    self.board_index[1] = i
                    break

        assign_row_index()
        assign_column_index()

        print("Selected board index is now set to {}.".format(self.board_index))

    def check_if_board_index_is_available(self):
        print("Checking if board index is available or contains value...")
        if self.board_list[self.board_index[0]][self.board_index[1]] == "":
            print("Board position is available. Returning True.")
            return True
        else:
            print("Position is unavailable. Contains {}.".format(
                self.board_list[self.board_index[0]][self.board_index[1]]))
            return False

    def assign_current_player_to_board_index(self):
        self.board_list[self.board_index[0]
                        ][self.board_index[1]] = self.current_player
        print("Assigning player {} to board_list[{}][{}].".format(
            self.current_player, self.board_index[0], self.board_index[1]))

    def run_game(self):
        pygame.init()
        game_display = pygame.display.set_mode((self.screen_width,
                                                self.screen_height))
        pygame.display.set_caption('Tic-Tac-Toe.')

        # Starting first round:
        self.next_round()

        while True:
            # Game start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if self.check_if_mouseclick_on_board(event.type) == True:
                    self.convert_mouse_pos_to_board_index()

                    if self.check_if_board_index_is_available() == True:
                        self.assign_current_player_to_board_index()

                        if self.check_if_win() == True:
                            self.player_win()
                            self.next_round()
                            self.switch_player()

                        elif self.check_if_draw() == True:
                            self.next_round()
                            self.switch_player()

                        else:
                            self.next_turn()
                            self.switch_player()

            # pygame.display.flip()

            pygame.display.update()
            pygame.time.Clock().tick(10)


if __name__ == "__main__":

    tictactoe = Tictactoe()

    tictactoe.run_game()
