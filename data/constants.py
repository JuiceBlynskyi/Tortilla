import json
import pygame
pygame.init()


FULL_SCREEN = False

if FULL_SCREEN:
    SCREEN_WIDTH = round(pygame.display.Info().current_w)
    SCREEN_HEIGHT = round(pygame.display.Info().current_h)
else:
    SCREEN_WIDTH = round(pygame.display.Info().current_w * 0.75)
    SCREEN_HEIGHT = round(pygame.display.Info().current_h * 0.75)

# SCREEN_WIDTH = pygame.display.Info().current_w
# SCREEN_HEIGHT = pygame.display.Info().current_h

# Colors
BLACK = 0, 0, 0
WHITE = 255, 255, 255
BLUE = 33, 150, 243
LIGHT_BLUE = 0, 191, 255
PURPLE = 41, 15, 53
LIGHT_PURPLE = 113, 41, 139
GREY = 204, 204, 204

# Fonts
# FONT_BOLD = 'assets/fonts/OpenSans-SemiBold.ttf'
FONT_BOLD = 'assets/fonts/DisposableDroidBB.ttf'
FONT_REG = 'assets/fonts/OpenSans-Regular.ttf'
FONT_LIGHT = 'assets/fonts/OpenSans-Light.ttf'

# Texts
MENU_TEXT = pygame.font.Font(FONT_LIGHT, round(110 / 1080 * SCREEN_HEIGHT))
LARGE_TEXT = pygame.font.Font(FONT_REG, round(40 / 1080 * SCREEN_HEIGHT))
MEDIUM_TEXT = pygame.font.Font(FONT_LIGHT, round(35 / 1440 * SCREEN_HEIGHT))
# SMALL_TEXT = pygame.font.Font(FONT_BOLD, int(25 / 1440 * SCREEN_HEIGHT))
SMALL_TEXT = pygame.font.Font(FONT_BOLD, round(35 / 1080 * SCREEN_HEIGHT))
HUD_TEXT = pygame.font.Font(FONT_REG, round(40 / 1440 * SCREEN_HEIGHT))