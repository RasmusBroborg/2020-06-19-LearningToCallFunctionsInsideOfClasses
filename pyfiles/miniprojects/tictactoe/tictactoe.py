import pygame
import sys

# EACH SQUARE 100x100
# Width has two extra rows of pixels to compensate for line draws.
# Height has extra 2 px for lines and extra 30 px for score bar at the top.
# GAMEBAR_WIDTH = 100
# GAMEBAR_HEIGHT = 30
DISPLAY_WIDTH = 300
DISPLAY_HEIGHT = 300
# Update frequency. Lower to decrease risk of double click
FPS = 10

COLOR_BLACK = (0, 0, 0)
COLOR_GREY = (125, 125, 125)
COLOR_WHITE = (255, 255, 255)


class Board:
    def __init__(self):
        self.player_o = "O"
        self.player_x = "X"
        self.player_x_score = 0
        self.player_o_score = 0
        self.round_count = 0
        self.turn = 0

        self.board_cells = ["", "", "",
                            "", "", "",
                            "", "", ""]

        # Turn variables:
        self.selected_player = self.player_x
        self.mouse_position = None
        self.selected_cell = None

    # DENNA MÅSTE SES ÖVER! SKA STARTA OM SPELET??

    def player_win(self, selected_player):
        if selected_player == self.player_o:
            self.player_o_score += 1
        elif selected_player == self.player_x:
            self.player_x_score += 1
    """
    # Too buggy, doesn't work.
    def draw(self):
        pygame.draw.aaline(
            game_display, COLOR_WHITE, 0, 50)
    """

    def player_switch(self):
        if self.selected_player == self.player_x:
            self.selected_player = self.player_o
        elif self.selected_player == self.player_o:
            self.selected_player = self.player_x

    def display_score(self):
        pass

    def get_cellindex_from_mouseclick_pos(self, xy):
        # board_cells[0]
        if xy[0] < DISPLAY_WIDTH / 3 * 1 and xy[1] < DISPLAY_HEIGHT / 3 * 1:
            self.selected_cell = 0
        elif xy[0] < DISPLAY_WIDTH / 3 * 1 and xy[1] < DISPLAY_HEIGHT / 3 * 2:
            self.selected_cell = 1
        elif xy[0] < DISPLAY_WIDTH / 3 * 1 and xy[1] < DISPLAY_HEIGHT / 3 * 3:
            self.selected_cell = 2

        elif xy[0] < DISPLAY_WIDTH / 3 * 2 and xy[1] < DISPLAY_HEIGHT / 3 * 1:
            self.selected_cell = 3
        elif xy[0] < DISPLAY_WIDTH / 3 * 2 and xy[1] < DISPLAY_HEIGHT / 3 * 2:
            self.selected_cell = 4
        elif xy[0] < DISPLAY_WIDTH / 3 * 2 and xy[1] < DISPLAY_HEIGHT / 3 * 3:
            self.selected_cell = 5

        elif xy[0] < DISPLAY_WIDTH / 3 * 3 and xy[1] < DISPLAY_HEIGHT / 3 * 1:
            self.selected_cell = 6
        elif xy[0] < DISPLAY_WIDTH / 3 * 3 and xy[1] < DISPLAY_HEIGHT / 3 * 2:
            self.selected_cell = 7
        elif xy[0] < DISPLAY_WIDTH / 3 * 3 and xy[1] < DISPLAY_HEIGHT / 3 * 3:
            self.selected_cell = 8

    def check_if_win(self):
        winner_string = self.selected_player * 3
        if (self.board_cells[0] + self.board_cells[1] + self.board_cells[2]) or (self.board_cells[3] + self.board_cells[4] + self.board_cells[5]) or (self.board_cells[6] + self.board_cells[7] + self.board_cells[8]) or (self.board_cells[0] + self.board_cells[3] + self.board_cells[6]) or (self.board_cells[1] + self.board_cells[4] + self.board_cells[7]) or (self.board_cells[2] + self.board_cells[5] + self.board_cells[8]) or (self.board_cells[0] + self.board_cells[4] + self.board_cells[8]) == (winner_string):
            print("Player {} wins!".format(self.selected_player))
        return True

    def upd_next_turn(self):
        self.turn += 1
        self.self.mouse_position = None
        self.selected_cell = None

    def game_logic(self):
        if self.selected_cell != None:
            self.board_cells[self.selected_cell] = self.selected_player
            print("IT WORKs!")
            self.check_if_win()

            self.player_switch()
            self.mouse_position = None
            self.selected_cell = None

        # Resetting turn variables

        """
        if player_selected_cell != None:
            if player_selected_cell[0] < (DISPLAY_WIDTH * 0.33)
        """

def main():

    game_display = pygame.display.set_mode((DISPLAY_WIDTH,
                                            DISPLAY_HEIGHT))
    pygame.display.set_caption('Tic-Tac-Toe')

    board = Board()

    # basic_font = pygame.font.Font('freesansbold.ttf', 32)

    while True:

        for event in pygame.event.get():
            print(event.type)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == 1025:
                board.mouseclick_pos = pygame.mouse.get_pos()
                board.get_cellindex_from_mouseclick_pos(board.mouseclick_pos)

        board.game_logic()
        # board.draw()

        pygame.display.update()
        pygame.time.Clock().tick(FPS)

        # board.reset()


if __name__ == "__main__":
    main()
