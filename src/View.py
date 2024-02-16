import pygame
from Game import Game


# Done: Put your names here (entire team)

# Sid Gion
# Declan Vail

class View:
    def __init__(self, screen: pygame.Surface, game: Game):
        self.screen = screen
        self.game = game
        pygame.display.set_caption("Super Tanks")
        self.game_mode = 'title_screen'
        self.intro_screen = pygame.display.set_mode((1650, 900))


    def draw_everything(self):
        if self.game_mode == 'title_screen':
            self.intro_screen.blit(pygame.image.load('../assets/TitleScreen.png'), (0, 0))

        elif self.game_mode == 'game_instructions':
            self.intro_screen.blit(pygame.image.load('../assets/Controls Instrustions.png'), (0, 0))

        elif self.game_mode == 'powerup_instructions':
            self.intro_screen.blit(pygame.image.load('../assets/PowerupInstructions.png'), (0, 0))

        else:
            self.game.draw_game()

        pygame.display.update()
