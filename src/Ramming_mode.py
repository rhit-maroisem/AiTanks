import time
import pygame

class Ramming_mode:
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
        self.tank_p1_original_image = self.tank_p1.image
        self.tank_p1_original_speed = self.tank_p1.speed
        self.tank_p2_original_image = self.tank_p2.image
        self.tank_p2_original_speed = self.tank_p2.speed

    def draw(self):
        self.screen.blit(self.image, (self.x - (self.image.get_width() // 2),
                                      self.y - (self.image.get_height() // 2)))

    def activate(self, tank):
        if tank == "tank_p1":
            self.tank_p1.ram_start_time = time.time()
            self.tank_p1_original_health = self.tank_p1.health
            self.tank_p1.ramming_mode_active = True
            self.tank_p1.image = pygame.image.load("../assets/RammingTankSprite_P1.png").convert_alpha()
            self.tank_p1.speed = self.tank_p1_original_speed * 1.5
            self.tank_p1.health = 32
        if tank == "tank_p2":
            self.tank_p2.ram_start_time = time.time()
            self.tank_p2_original_health = self.tank_p2.health
            self.tank_p2.ramming_mode_active = True
            self.tank_p2.image = pygame.image.load("../assets/RammingTankSprite_P2.png").convert_alpha()
            self.tank_p2.speed = self.tank_p2_original_speed * 1.5
            self.tank_p2.health = 32

    def deactivate(self, tank):
        if tank == "tank_p1":
            self.tank_p1.ram_start_time = None
            self.tank_p1.ramming_mode_active = False
            self.tank_p1.image = self.tank_p1_original_image
            self.tank_p1.speed = self.tank_p1_original_speed
            self.tank_p1.health = self.tank_p1_original_health - 2
        if tank == "tank_p2":
            self.tank_p2.ram_start_time = None
            self.tank_p2.ramming_mode_active = False
            self.tank_p2.image = self.tank_p2_original_image
            self.tank_p2.speed = self.tank_p2_original_speed
            self.tank_p2.health = self.tank_p2_original_health - 2