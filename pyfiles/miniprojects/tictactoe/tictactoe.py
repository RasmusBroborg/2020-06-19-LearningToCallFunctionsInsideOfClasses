import pygame
import sys

# EACH SQUARE 100x100
# Width has two extra rows of pixels to compensate for line draws.
# Height has extra 2 px for lines and extra 30 px for score bar at the top.
#GAMEBAR_WIDTH = 100
#GAMEBAR_HEIGHT = 30
DISPLAY_WIDTH = 300
DISPLAY_HEIGHT = 300  # + GAMEBAR_HEIGHT
# Update frequency. Lower to decrease risk of double click
FPS = 10

COLOR_BLACK = (0, 0, 0)
COLOR_GREY = (125, 125, 125)
COLOR_WHITE = (255, 255, 255)


"""
Game:

- Create board (list?) (class?)
    - init draw line at x 100px and x 200px
    - init Create zones
    - Init zone as empty (None?)
    - Init player (start?)

    - func to assign selected players
        - event mouse click px zone add value to zone

    - func to switch_player
        - if player x:
            player = o
        - if player o:
            player = x

    - func to print which players turn it is:
        -

- Create reset_game (if player click area, reset game)

-

"""


class Cell():
    def __init__(self, x, y, width, height):
        self.char_assignment = None
        self.positional_info = (self.x)


class Board:
    def __init__(self):
        self.lines = pygame.draw.aaline(
            game_display, COLOR_WHITE, 0, 50)
        self.player_o = "O"
        self.player_x = "X"
        self.player_x_score = 0
        self.player_o_score = 0
        self.round_count = 0
        self.turn = 1
        self.selected_player = player_x

        self.cell_0 = Cell()
        self.cell_1 = Cell()
        self.cell_2 = Cell()

        self.cell_3 = Cell()
        self.cell_4 = Cell()
        self.cell_5 = Cell()

        self.cell_6 = Cell()
        self.cell_7 = Cell()
        self.cell_8 = Cell()

        self.board_cells = [self.cell_0, self.cell_1, self.cell_2,
                            self.cell_3, self.cell_4, self.cell_5,
                            self.cell_6, self.cell_7, self.cell_8, ]

    # DENNA MÅSTE SES ÖVER! SKA STARTA OM SPELET??

    def player_win(self, selected_player):
        if selected_player == self.player_o:
            self.player_o_score += 1
        elif selected_player == self.player_x:
            self.player_x_score += 1

    def draw(self):
        pass
        # if self.turn

    def player_switch(self):
        if self.selected_player == player_x:
            self.selected_player = player_o
        elif self.selected_player == player_o:
            self.selected_player = player_x

    def upd_turn_count(self):
        self.turn += 1

    def display_score(self):
        pass

    def game_logic():
        pass


def main():

    game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption('Tic-Tac-Toe')

    reset_game = False

    # Board init
    board = Board

    #basic_font = pygame.font.Font('freesansbold.ttf', 32)

    while not reset_game:

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type ==
            #

        board.game_logic()

        pygame.display.update()
        pygame.time.Clock().tick(FPS)


if __name__ == "__main__":
    main()
