# Legacy code from:
# https://pythonprogramming.net/displaying-images-pygame/?completed=/pygame-python-3-part-1-intro/


import pygame
import sys

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Racegame test.')

clock = pygame.time.Clock()
crashed = False


class Car:
    def __init__(self, init_x_pos, init_y_pos):
        self.car_img = pygame.image.load('car.png')
        self.car_pos = game_display.blit(
            self.car_img, (init_x_pos, init_y_pos))
        self.x_pos = init_x_pos
        self.y_pos = init_y_pos
        self.speed = 0

    def car_movement(self, event_type):
        # Method will run in the event loop in main. Input is event.type.
        if event_type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.speed -= 6
            if event.key == pygame.K_d:
                self.speed += 6
        if event_type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.speed = 0
            if event.key == pygame.K_d:
                self.speed = 0

        self.x_pos += self.speed

        if self.x_pos <= 0:
            self.x_pos = 0
            # Nedan behöver rättas till för att kompensera för bildens bredd
        if self.x_pos >= DISPLAY_WIDTH:
            self.x_pos = DISPLAY_WIDTH

    def draw_car(self):
        game_display.blit(
            self.car_img, (self.x_pos, self.y_pos))

    def crash(self):
        # Om bil kolliderar
        # crashed = True
        pass


car = Car((DISPLAY_WIDTH * 0.45), (DISPLAY_HEIGHT * 0.80))

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        car.car_movement(event.type)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_DOWN:
                pass
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_DOWN:
                pass

        print(event)

    game_display.fill(WHITE)
    car.draw_car()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
quit()
