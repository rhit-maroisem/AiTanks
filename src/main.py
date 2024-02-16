import pygame
from Game import Game
from Controller import Controller
from View import View


# Done: Put your names here (entire team)
# Sid Gion
# Declan Vail

#^ Original team
#new Ai work:
#Emile Marois

def main():
    pygame.init()
    screen = pygame.display.set_mode((1650, 900))  # Done: Choose your own size
    clock = pygame.time.Clock()
    game = Game(screen)  # the Model
    viewer = View(screen, game)  # the View
    controller = Controller(game, viewer)  # the Controller
    frame_rate = 60  # Done: Choose your own frame rate

    while True:
        clock.tick(frame_rate)
        controller.get_and_handle_events()
        game.run_one_cycle()
        viewer.draw_everything()  # Includes the pygame.display.update()
        if game.tank_p1.health <= 0:
            winner = "tank_p2"
            break
        if game.tank_p2.health <= 0:
            winner = "tank_p1"
            break

    while True:
        clock.tick(frame_rate)
        explosion = pygame.image.load("../assets/Explosion.png")
        if winner == "tank_p2":
            screen.blit(explosion, (game.tank_p1.x - explosion.get_width() // 2,
                                    game.tank_p1.y - explosion.get_height() // 2))
            screen.blit(pygame.image.load("../assets/GameOverP2.png"), (0, 0))
        if winner == "tank_p1":
            screen.blit(explosion, (game.tank_p2.x - explosion.get_width() // 2,
                                    game.tank_p2.y - explosion.get_height() // 2))
            screen.blit(pygame.image.load("../assets/GameOverP1.png"), (0, 0))
        pygame.display.update()

        events = pygame.event.get()
        controller.exit_if_time_to_quit(events)
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_r]:
            break

    main()
main()