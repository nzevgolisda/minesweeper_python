
import sys
import pygame
from Config import Config

from ctypes.wintypes import RGB




def run_game():
    #Initialize game and create a screen object.
    pygame.init()
    config = Config()
    screen = pygame.display.set_mode((config.screen_width, config.screen_height))
    #Start the main loop for the game.
    while True:
        #Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #Redraw the screen during each pass through the loop.
        screen.fill(config.bg_color)
        #Make the most recently drawn screen visible
        pygame.display.flip()
run_game()