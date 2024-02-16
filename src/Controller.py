import pygame
import sys
from Game import Game


# Done: Put your names here (entire team)
# Sid Gion
# Declan Vail

class Controller:
    def __init__(self, game: Game, View):
        self.game = game
        self.View = View

    def get_and_handle_events(self):
        """
        [Describe what keys and/or mouse actions cause the game to ...]
        """
        events = pygame.event.get()
        self.exit_if_time_to_quit(events)
        pressed_keys = pygame.key.get_pressed()


        if self.key_was_pressed_on_this_cycle(pygame.K_SPACE, events):
            if self.View.game_mode == 'title_screen':
                self.View.game_mode = 'game_instructions'
            elif self.View.game_mode == 'game_instructions':
                self.View.game_mode = 'powerup_instructions'
            elif self.View.game_mode == 'powerup_instructions':
                self.View.game_mode = 'play_game'


        # Player 1 Controls
        if pressed_keys[pygame.K_w]:
            self.game.tank_p1.move("forward")
        if pressed_keys[pygame.K_s]:
            self.game.tank_p1.move("backward")
        if pressed_keys[pygame.K_a]:
            self.game.tank_p1.turn("left")
        if pressed_keys[pygame.K_d]:
            self.game.tank_p1.turn("right")
        if self.key_was_pressed_on_this_cycle(pygame.K_LSHIFT, events):
            self.game.tank_p1.shoot()


        # Player 2 Controls
        if pressed_keys[pygame.K_UP]:
            self.game.tank_p2.move("forward")
        if pressed_keys[pygame.K_DOWN]:
            self.game.tank_p2.move("backward")
        if pressed_keys[pygame.K_LEFT]:
            self.game.tank_p2.turn("left")
        if pressed_keys[pygame.K_RIGHT]:
            self.game.tank_p2.turn("right")
        if self.key_was_pressed_on_this_cycle(pygame.K_m, events):
            self.game.tank_p2.shoot()

    @staticmethod
    def exit_if_time_to_quit(events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()

    @staticmethod
    def key_was_pressed_on_this_cycle(key, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == key:
                return True
        return False
