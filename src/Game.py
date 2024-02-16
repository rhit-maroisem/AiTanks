import pygame
from Tank import Tank
from Shell import Shell
from Barriers import Barriers
from Powerup import Powerup
import time

# Done: Put your names here (entire team)
# Sid Gion
# Declan Vail

class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.barriers = Barriers(self.screen)
        self.tank_p1 = Tank(self.screen,
                            self.barriers.margin,
                            self.barriers.margin,
                            0,
                            "../assets/TankSprite_P1.png",
                            self.barriers.lines)
        self.tank_p2 = Tank(self.screen,
                            self.screen.get_width() - self.barriers.margin,
                            self.screen.get_height() - self.barriers.margin,
                            180,
                            "../assets/TankSprite_P2.png",
                            self.barriers.lines)
        self.powerup = Powerup(self.screen, self.barriers.margin, self.barriers.barrier_length,
                               self.tank_p1, self.tank_p2)
        self.tank_p1_powerup_activation_start_time = 0
        self.tank_p2_powerup_activation_start_time = 0
        self.powerup_duration = 15

    def draw_game(self):
        """ Ask all the objects in the game to draw themselves. """
        self.screen.blit(pygame.image.load("../assets/SandBackground2.jpeg"), (0, 0))
        self.barriers.draw()
        for powerup in self.powerup.powerups:
            powerup.draw()
        self.tank_p1.draw()
        self.tank_p2.draw()
        for k in range(len(self.tank_p1.shells)):
            self.tank_p1.shells[k].draw("blue")
        for j in range(len(self.tank_p2.shells)):
            self.tank_p2.shells[j].draw("red")


    def run_one_cycle(self):
        """ All objects that do something at each cycle: ask them to do it. """
        self.tank_p1.delete_shell()
        self.tank_p2.delete_shell()

        # Checks if tank collides with powerup and starts cooldown clock if needed
        if self.tank_p1.powerup_active == None:
            for index in range(len(self.powerup.powerups) - 1, -1, -1):
                if self.tank_p1.hit_box.colliderect(self.powerup.powerups[index].hit_box):
                    self.powerup.powerups[index].activate("tank_p1")
                    self.tank_p1.powerup_active = self.powerup.powerups[index]
                    del self.powerup.powerups[index]
                    self.tank_p1_powerup_activation_start_time = time.time()
        elif time.time() - self.tank_p1_powerup_activation_start_time > self.powerup_duration:
            self.tank_p1.powerup_active.deactivate("tank_p1")
            self.tank_p1.powerup_active = None


        if self.tank_p2.powerup_active == None:
            for index in range(len(self.powerup.powerups) - 1, -1, -1):
                if self.tank_p2.hit_box.colliderect(self.powerup.powerups[index].hit_box):
                    self.powerup.powerups[index].activate("tank_p2")
                    self.tank_p2.powerup_active = self.powerup.powerups[index]
                    del self.powerup.powerups[index]
                    self.tank_p2_powerup_activation_start_time = time.time()
        elif time.time() - self.tank_p2_powerup_activation_start_time > self.powerup_duration:
            self.tank_p2.powerup_active.deactivate("tank_p2")
            self.tank_p2.powerup_active = None

        # Moves tank shells
        for k in range(len(self.tank_p1.shells)):
            self.tank_p1.shells[k].move()
        for j in range(len(self.tank_p2.shells)):
            self.tank_p2.shells[j].move()

        # Checks if tanks bullets collide with tanks
        for i in range(len(self.tank_p2.shells) - 1, -1, -1):
            if self.tank_p1.hit_box.colliderect(self.tank_p2.shells[i].hit_box):
                self.tank_p1.health -= self.tank_p2.shell_damage
                del self.tank_p2.shells[i]
        for l in range(len(self.tank_p1.shells) - 1, -1, -1):
            if self.tank_p2.hit_box.colliderect(self.tank_p1.shells[l].hit_box):
                self.tank_p2.health -= self.tank_p1.shell_damage
                del self.tank_p1.shells[l]

        # Checks if bullets collide with bullets
        for m in range(len(self.tank_p2.shells) - 1, -1, -1):
            for n in range(len(self.tank_p1.shells) -1, -1, -1):
                if self.tank_p1.shells[n].hit_box.colliderect(self.tank_p2.shells[m].hit_box):
                    self.tank_p1.shells[n].health -= self.tank_p2.shells[m].damage
                    self.tank_p2.shells[m].health -= self.tank_p1.shells[n].damage
                    if self.tank_p1.shells[n].health <= 0:
                        del self.tank_p1.shells[n]
                    if self.tank_p2.shells[m].health <= 0:
                        del self.tank_p2.shells[m]
                    break

        # Turns Tank's Bullets to Bouncy Bullets if Powerup is active
        if self.tank_p1.bouncy_bullets_active:
            for index in range(len(self.tank_p1.shells) - 1, -1, -1):
                for barrier_line in self.barriers.lines:
                    if barrier_line.colliderect(self.tank_p1.shells[index].left_right_detector):
                        self.tank_p1.shells[index].dx = self.tank_p1.shells[index].dx * -1
                        break
                    if barrier_line.colliderect(self.tank_p1.shells[index].top_bottom_detector):
                        self.tank_p1.shells[index].dy = self.tank_p1.shells[index].dy * -1
                        break

        if self.tank_p2.bouncy_bullets_active:
            for index in range(len(self.tank_p2.shells) - 1, -1, -1):
                for barrier_line in self.barriers.lines:
                    if barrier_line.colliderect(self.tank_p2.shells[index].left_right_detector):
                        self.tank_p2.shells[index].dx = self.tank_p2.shells[index].dx * -1
                        break
                    if barrier_line.colliderect(self.tank_p2.shells[index].top_bottom_detector):
                        self.tank_p2.shells[index].dy = self.tank_p2.shells[index].dy * -1
                        break

        # Checks for Ramming collision
        if self.tank_p1.ramming_mode_active and self.tank_p2.ramming_mode_active:
            if self.tank_p1.hit_box.colliderect(self.tank_p2.hit_box):
                if self.tank_p1.ram_start_time >= self.tank_p2.ram_start_time:
                    self.tank_p2.health = 0
                else:
                    self.tank_p1.health = 0
        elif self.tank_p1.ramming_mode_active:
            if self.tank_p1.hit_box.colliderect(self.tank_p2.hit_box):
                self.tank_p2.health = 0
        elif self.tank_p2.ramming_mode_active:
            if self.tank_p2.hit_box.colliderect(self.tank_p1.hit_box):
                self.tank_p1.health = 0

        # Checks if other tank has rammer to power up other player's big shell
        if self.tank_p2.ramming_mode_active:
            self.tank_p1.other_tank_has_ram = True
        else:
            self.tank_p1.other_tank_has_ram = False
        if self.tank_p1.ramming_mode_active:
            self.tank_p2.other_tank_has_ram = True
        else:
            self.tank_p2.other_tank_has_ram = False


        # Checks if Tank is colliding with a tank
        if self.tank_p1.right_detector.colliderect(self.tank_p2.hit_box):
            self.tank_p1.x -= 2
        if self.tank_p1.left_detector.colliderect(self.tank_p2.hit_box):
            self.tank_p1.x += 2
        if self.tank_p1.top_detector.colliderect(self.tank_p2.hit_box):
            self.tank_p1.y += 2
        if self.tank_p1.bottom_detector.colliderect(self.tank_p2.hit_box):
            self.tank_p1.y -= 2
        if self.tank_p2.right_detector.colliderect(self.tank_p1.hit_box):
            self.tank_p2.x -= 2
        if self.tank_p2.left_detector.colliderect(self.tank_p1.hit_box):
            self.tank_p2.x += 2
        if self.tank_p2.top_detector.colliderect(self.tank_p1.hit_box):
            self.tank_p2.y += 2
        if self.tank_p2.bottom_detector.colliderect(self.tank_p1.hit_box):
            self.tank_p2.y -= 2

        # Updates Tank's Hitboxes
        self.tank_p1.update_hit_boxes()
        self.tank_p2.update_hit_boxes()

