import pygame

class Boucy_bullets:
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

    def draw(self):
        self.screen.blit(self.image, (self.x - (self.image.get_width() // 2),
                                      self.y - (self.image.get_height() // 2)))

    def activate(self, tank):
        if tank == "tank_p1":
            self.tank_p1.bouncy_bullets_active = True
        if tank == "tank_p2":
            self.tank_p2.bouncy_bullets_active = True

    def deactivate(self, tank):
        if tank == "tank_p1":
            self.tank_p1.bouncy_bullets_active = False
        if tank == "tank_p2":
            self.tank_p2.bouncy_bullets_active = False