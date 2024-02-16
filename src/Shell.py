import pygame

class Shell:
    def __init__(self, screen, x, y, dx, dy, radius, speed, health, damage):
        self.screen = screen
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.speed = speed
        self.health = health
        self.damage = damage
        self.hit_box = pygame.Rect(self.x - self.radius, self.y - self.radius,
                                  self.radius * 2, self.radius * 2)
        self.left_right_detector = pygame.Rect(self.x - self.radius, self.y - 2, self.radius * 2, 4)
        self.top_bottom_detector = pygame.Rect(self.x - 2, self.y + self.radius, 4, self.radius * 2)


    def move(self):
        self.x += self.dx * self.speed
        self.y -= self.dy * self.speed
        self.hit_box = pygame.Rect(self.x - self.radius, self.y - self.radius,
                                   self.radius * 2, self.radius * 2)
        self.left_right_detector = pygame.Rect(self.x - self.radius, self.y - 2, self.radius * 2, 4)
        self.top_bottom_detector = pygame.Rect(self.x - 2, self.y + self.radius, 4, self.radius * 2)
    def draw(self, color):
        # pygame.draw.rect(self.screen, (255, 0, 0), self.hit_box)
        if color == "blue":
            pygame.draw.circle(self.screen, (0, 0, 255), (self.x, self.y), self.radius)
        if color == "red":
            pygame.draw.circle(self.screen, (255, 0, 0), (self.x, self.y), self.radius)
