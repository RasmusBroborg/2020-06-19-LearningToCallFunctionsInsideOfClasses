import pygame
import sys

# EACH SQUARE 100x100
SCREENWIDTH = 100 * 3
SCREENHEIGHT = 100 * 3
# Update frequency
FPS = 10


"""
Game:

- Create board (list?) (class?)
    - init draw line at x 100px and x 200px
    - init Create zones
    - Init zone as empty (None?)
    - Init player (start?)

    - func to assign selected player

        - event mouse click px zone add value to zone
        - if player x:
            player = o
        - if player o:
            player = x

    - func to print which players turn it is:
        -

- Create reset_game (if player click area, reset game)

-

"""

def main():

    reset_game = False

    while not reset:

        for event in pygame.event.get():
            print(pygame.event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type ==
            #     reset_game = True

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
