import pygame
import random
from Big_bullets import Big_bullets
from Ramming_mode import Ramming_mode
from Shield import Shield
from Bouncy_bullets import Boucy_bullets

class Powerup:
    def __init__(self, screen: pygame.Surface, margin, distance, tank_p1, tank_p2):
        self.screen = screen
        self.margin = margin
        self.distance = distance
        self.tank_p1 = tank_p1
        self.tank_p2 = tank_p2
        self.powerup_grid = []
        for k in range((self.screen.get_height() - (2 * self.margin)) // self.distance):
            sub_grid = []
            for j in range((self.screen.get_width() - (2 * self.margin)) // self.distance):
                if random.randint(1, 100) <= 7:
                    sub_grid.append(True)
                else:
                    sub_grid.append(False)
            self.powerup_grid.append(sub_grid)

        self.powerups = []
        for k in range(len(self.powerup_grid)):
            for j in range(len(self.powerup_grid[k])):
                if self.powerup_grid[k][j]:
                    rand_num = random.randint(1, 100)
                    if rand_num <= 25:
                        self.powerups.append(Big_bullets(self.screen, "../assets/BigBulletsPad.png",
                                                         (self.margin + (self.distance / 2)) + (self.distance * j),
                                                         (self.margin + (self.distance / 2)) + (self.distance * k),
                                                         self.tank_p1,
                                                         self.tank_p2))
                    elif rand_num <= 50:
                        self.powerups.append(Boucy_bullets(self.screen, "../assets/BouncyBullets.png",
                                                         (self.margin + (self.distance / 2)) + (self.distance * j),
                                                         (self.margin + (self.distance / 2)) + (self.distance * k),
                                                           self.tank_p1,
                                                           self.tank_p2))
                    elif rand_num <= 75:
                        self.powerups.append(Shield(self.screen, "../assets/ShieldPad.png",
                                                         (self.margin + (self.distance / 2)) + (self.distance * j),
                                                         (self.margin + (self.distance / 2)) + (self.distance * k),
                                                    self.tank_p1,
                                                    self.tank_p2))
                    else:
                        self.powerups.append(Ramming_mode(self.screen, "../assets/RammerPad.png",
                                                         (self.margin + (self.distance / 2)) + (self.distance * j),
                                                         (self.margin + (self.distance / 2)) + (self.distance * k),
                                                          self.tank_p1,
                                                          self.tank_p2))