import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.y = y
        self.x = x
        self.image = pygame.Surface((15, 15))
        self.image.fill((0, 128, 255))
        self.rect = self.image.get_rect()
        self.rect.left = self.x
        self.rect.top = self.y
        self.seconds_alive = None

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def player_movement(self):
        pass

    def level(self):
        pass

    def game_over(self):
        # If player collides with red square.
        pass


class Red_Square():
    pass


def visuals():
    pass


def main():
    # General setup
    pygame.init()
    game_clock_speed = 120

    # Display
    display_width = 1280
    display_height = 720
    display = pygame.display.set_mode((screen_width, screen_height))

    # Colors
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (125, 125, 125)

    player = Player()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    # Game Logic functions

    # Update visuals
    display.fill(background_color)

    pygame.time.Clock(game_clock_speed)
