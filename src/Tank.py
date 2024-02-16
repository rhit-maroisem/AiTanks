import pygame
import math
from Shell import Shell


class Tank:
    def __init__(self, screen: pygame.Surface, x, y, angle, image, barrier_lines):
        self.x = x
        self.y = y
        self.health_initial = 7
        self.health = self.health_initial
        self.screen = screen
        self.image = pygame.image.load(image).convert_alpha()
        # self.image.set_colorkey((255, 255, 255))
        self.speed = 2
        self.angle = angle
        self.hit_circle_radius = self.image.get_width() // 2
        self.image_original_height = self.image.get_height()
        self.hit_box = pygame.Rect(self.x - (self.image_original_height // 2),
                                   self.y - (self.image_original_height // 2),
                                   self.image_original_height,
                                   self.image_original_height)
        self.shells = []
        self.shell_radius = 4
        self.shell_speed = 10
        self.shell_health = 1
        self.shell_damage = 1
        self.big_shell_active = False
        self.bouncy_bullets_active = False
        self.ramming_mode_active = False
        self.other_tank_has_ram = False
        self.ram_start_time = None
        self.big_shell_charge = 0
        self.barrier_lines = barrier_lines
        self.powerup_active = None
        self.detector_width = 6
        self.top_detector = pygame.Rect(self.x - (self.detector_width / 2),
                                        self.y - self.image.get_height() / 2,
                                        self.detector_width,
                                        self.image.get_height() / 2)
        self.bottom_detector = pygame.Rect(self.x - (self.detector_width / 2),
                                           self.y,
                                           self.detector_width,
                                           self.image.get_height() / 2)
        self.left_detector = pygame.Rect(self.x - self.image.get_height() / 2,
                                         self.y - (self.detector_width / 2),
                                         self.image.get_height() / 2,
                                         self.detector_width)
        self.right_detector = pygame.Rect(self.x,
                                          self.y - (self.detector_width / 2),
                                          self.image.get_height() / 2,
                                          self.detector_width)
        self.detectors = [self.top_detector, self.bottom_detector, self.left_detector, self.right_detector]
        self.bounding_box = pygame.Rect(self.hit_circle_radius,
                                        self.hit_circle_radius,
                                        self.screen.get_width() - (2 * self.hit_circle_radius),
                                        self.screen.get_height() - (2 * self.hit_circle_radius))
    def draw(self):

        # for detector in self.detectors:
        #     pygame.draw.rect(self.screen, (0, 0, 255), detector)
        if self.health <= self.health_initial:
            pygame.draw.rect(self.screen, (0, 0, 0), (self.x - self.hit_circle_radius - 4 - 2,
                                                      self.y - self.hit_circle_radius - 12 - 2,
                                                      (self.hit_circle_radius * 2) + 8 + 4,
                                                      4 + 4))
        else:
            pygame.draw.rect(self.screen, (151, 255, 255), (self.x - self.hit_circle_radius - 4 - 2,
                                                      self.y - self.hit_circle_radius - 12 - 2,
                                                      (self.hit_circle_radius * 2) + 8 + 4,
                                                      4 + 4))
        pygame.draw.rect(self.screen, (238, 44, 44), (self.x - self.hit_circle_radius - 4,
                                                      self.y - self.hit_circle_radius - 12,
                                                      (self.hit_circle_radius * 2) + 8,
                                                      4))
        if self.health <= self.health_initial:
            pygame.draw.rect(self.screen, (127, 255, 0), (self.x - self.hit_circle_radius - 4,
                             self.y - self.hit_circle_radius - 12,
                             (((self.hit_circle_radius * 2) + 8) / self.health_initial) * self.health,
                             4))
        else:
            pygame.draw.rect(self.screen, (127, 255, 0), (self.x - self.hit_circle_radius - 4,
                                                          self.y - self.hit_circle_radius - 12,
                                                          (self.hit_circle_radius * 2) + 8,
                                                          4))
            pygame.draw.circle(self.screen, (121, 205, 205), (self.x, self.y), self.hit_circle_radius + 5)
        if self.big_shell_active:
            pygame.draw.rect(self.screen, (0, 0, 0), (self.x - self.hit_circle_radius - 4 - 2,
                                                      self.y - self.hit_circle_radius - 24 - 2,
                                                      (self.hit_circle_radius * 2) + 8 + 4,
                                                      4 + 4))
            pygame.draw.rect(self.screen, (255, 215, 0), (self.x - self.hit_circle_radius - 4,
                                                          self.y - self.hit_circle_radius - 24,
                                                          (((self.hit_circle_radius * 2) + 8) // 3) * self.big_shell_charge,
                                                          4))

        rotated_image = pygame.transform.rotate(self.image, self.angle)
        self.screen.blit(rotated_image, (self.x - int(rotated_image.get_width() / 2),
                                         self.y - int(rotated_image.get_height() / 2)))


    def shoot(self):
        if self.ramming_mode_active == False:
            if self.big_shell_active:
                if self.other_tank_has_ram == False:
                    self.shell_damage = 5
                    if self.big_shell_charge >= 3:
                        self.shells.append(Shell(self.screen, self.x, self.y,
                                                 math.cos(math.radians(self.angle)), math.sin(math.radians(self.angle)),
                                                 self.shell_radius, self.shell_speed, self.shell_health, self.shell_damage))
                        self.big_shell_charge = 0
                    else:
                        self.big_shell_charge += 1
                else:
                    self.shell_damage = 10
                    if self.big_shell_charge >= 3:
                        self.shells.append(Shell(self.screen, self.x, self.y,
                                                 math.cos(math.radians(self.angle)), math.sin(math.radians(self.angle)),
                                                 self.shell_radius, self.shell_speed, self.shell_health,
                                                 self.shell_damage))
                        self.big_shell_charge = 0
                    else:
                        self.big_shell_charge += 1
            else:
                self.shells.append(Shell(self.screen, self.x, self.y,
                                     math.cos(math.radians(self.angle)), math.sin(math.radians(self.angle)),
                                     self.shell_radius, self.shell_speed, self.shell_health, self.shell_damage))

    def delete_shell(self):
        border_rect = pygame.Rect(0, 0, self.screen.get_width(), self.screen.get_height())
        for index in range(len(self.shells) - 1, -1, -1):
            if border_rect.colliderect(self.shells[index].hit_box) == False:
                del self.shells[index]

        if self.bouncy_bullets_active == False:
            for index in range(len(self.shells) - 1, -1, -1):
                for barrier_line in self.barrier_lines:
                    if barrier_line.colliderect(self.shells[index].hit_box):
                        del self.shells[index]
                        break

    def move(self, direction):
        if self.bounding_box.collidepoint(self.x, self.y):
            collisions = self.wall_collision()
            if collisions == []:
                if direction == "forward":
                    self.x += self.speed * math.cos(math.radians(self.angle))
                    self.y -= self.speed * math.sin(math.radians(self.angle))
                if direction == "backward":
                    self.x -= self.speed * math.cos(math.radians(self.angle))
                    self.y += self.speed * math.sin(math.radians(self.angle))
            else:
                for collision in collisions:
                    if collision == "right_collision":
                        self.x -= 1
                    elif collision == "left_collision":
                        self.x += 1
                    elif collision == "top_collision":
                        self.y += 1
                    else:
                        self.y -= 1
        else:
            if self.y + self.hit_circle_radius >= self.screen.get_height():
                self.y = self.screen.get_height() - self.hit_circle_radius - 1
            if self.y - self.hit_circle_radius <= 0:
                self.y = self.hit_circle_radius + 1
            if self.x + self.hit_circle_radius >= self.screen.get_width():
                self.x = self.screen.get_width() - self.hit_circle_radius - 1
            if self.x - self.hit_circle_radius <= 0:
                self.x = self.hit_circle_radius + 1

    def update_hit_boxes(self):
        # moves detectors
        self.top_detector = pygame.Rect(self.x - (self.detector_width / 2),
                                        self.y - self.image.get_height() / 2,
                                        self.detector_width,
                                        self.image.get_height() / 2)
        self.bottom_detector = pygame.Rect(self.x - (self.detector_width / 2),
                                           self.y,
                                           self.detector_width,
                                           self.image.get_height() / 2)
        self.left_detector = pygame.Rect(self.x - self.image.get_height() / 2,
                                         self.y - (self.detector_width / 2),
                                         self.image.get_height() / 2,
                                         self.detector_width)
        self.right_detector = pygame.Rect(self.x,
                                          self.y - (self.detector_width / 2),
                                          self.image.get_height() / 2,
                                          self.detector_width)
        self.detectors = [self.top_detector, self.bottom_detector, self.left_detector, self.right_detector]

        # moves hit box
        self.hit_box = pygame.Rect(self.x - (self.image_original_height // 2),
                                   self.y - (self.image_original_height // 2),
                                   self.image_original_height,
                                   self.image_original_height)

    def turn(self, direction):
        if direction == "right":
            self.angle -= self.speed * 1.2
        if direction == "left":
            self.angle += self.speed * 1.2

    def wall_collision(self):
        collisions = []
        for line in self.barrier_lines:
            if line.colliderect(self.right_detector):
                collisions.append("right_collision")
            if line.colliderect(self.left_detector):
                collisions.append("left_collision")
            if line.colliderect(self.top_detector):
                collisions.append("top_collision")
            if line.colliderect(self.bottom_detector):
                collisions.append("bottom_collision")
        return collisions

