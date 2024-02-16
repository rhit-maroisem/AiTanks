import pygame
import time

class Big_bullets:
    def __init__(self, screen: pygame.Surface, image, x, y, tank_p1, tank_p2):
        self.screen = screen
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.tank_p1 = tank_p1
        self.tank_p2 = tank_p2
        self.hit_box = pygame.Rect(self.x - (self.image.get_width() // 2),
                                   self.y - (self.image.get_height() // 2),
                                   self.image.get_width(),
                                   self.image.get_height())
        # Tank original state storage
        self.tank_p1_original_shell_state = {"radius": self.tank_p1.shell_radius,
                                             "speed": self.tank_p1.shell_speed,
                                             "health": self.tank_p1.shell_health,
                                             "damage": self.tank_p1.shell_damage}
        self.tank_p2_original_shell_state = {"radius": self.tank_p2.shell_radius,
                                             "speed": self.tank_p2.shell_speed,
                                             "health": self.tank_p2.shell_health,
                                             "damage": self.tank_p2.shell_damage}

    def draw(self):
        self.screen.blit(self.image, (self.x - (self.image.get_width() // 2),
                                      self.y - (self.image.get_height() // 2)))

    def activate(self, tank):
        if tank == "tank_p1":
            self.tank_p1.shell_radius = 12
            self.tank_p1.shell_speed = 5
            self.tank_p1.shell_health = 5
            self.tank_p1.shell_damage = 5
            self.tank_p1.big_shell_active = True
        if tank == "tank_p2":
            self.tank_p2.shell_radius = 12
            self.tank_p2.shell_speed = 5
            self.tank_p2.shell_health = 5
            self.tank_p2.shell_damage = 5
            self.tank_p2.big_shell_active = True

    def deactivate(self, tank):
        if tank == "tank_p1":
            self.tank_p1.shell_radius = self.tank_p1_original_shell_state["radius"]
            self.tank_p1.shell_speed = self.tank_p1_original_shell_state["speed"]
            self.tank_p1.shell_health = self.tank_p1_original_shell_state["health"]
            self.tank_p1.shell_damage = self.tank_p1_original_shell_state["damage"]
            self.tank_p1.big_shell_active = False
        if tank == "tank_p2":
            self.tank_p2.shell_radius = self.tank_p2_original_shell_state["radius"]
            self.tank_p2.shell_speed = self.tank_p2_original_shell_state["speed"]
            self.tank_p2.shell_health = self.tank_p2_original_shell_state["health"]
            self.tank_p2.shell_damage = self.tank_p2_original_shell_state["damage"]
            self.tank_p2.big_shell_active = False
