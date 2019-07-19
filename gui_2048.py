from source_code import *
import pygame
import sys


def play_game():
    """
    Runs the game for the user to play
    """
    pygame.init()
    pygame.display.set_mode((100,100))
    game_grid = TwentyFortyEight(4,4)
    print(game_grid.__str__())
    while pygame.key.get_focused():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game_grid.move(LEFT)
                    print(game_grid.__str__())
                elif event.key == pygame.K_RIGHT:
                    game_grid.move(RIGHT)
                    print(game_grid.__str__())
                elif event.key == pygame.K_UP:
                    game_grid.move(UP)
                    print(game_grid.__str__())
                elif event.key == pygame.K_DOWN:
                    game_grid.move(DOWN)
                    print(game_grid.__str__())
            if game_grid.check_if_lost == 1:
                print("You have lost.")
                sys.exit()
            if game_grid.check_if_won == 1:
                print("You have won!!!")
                sys.exit()


