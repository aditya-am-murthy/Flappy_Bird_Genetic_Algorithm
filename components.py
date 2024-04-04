import pygame
import random

class Floor:
    floor_level = 700

    def __init__(self, window_w):
        self.x, self.y = 0, Floor.floor_level
        self.rect = pygame.Rect(self.x, self.y, window_w, 3)

    def create(self, window):
        pygame.draw.rect(window, (200, 100, 100), self.rect)

class Obstacles:
    width = 20
    opening = 70

    def __init__(self, window_w):
        self.x = window_w
        self.bottom_height = random.randint(10, 600)
        self.top_height = Floor.floor_level - self.bottom_height - self.opening
        self.bottom_rect = pygame.Rect(0, 0, 0, 0)
        self.top_rect = pygame.Rect(0, 0, 0, 0)
        self.passed = False
        self.deleteNow = False

    def create(self, window):
        self.bottom_rect = pygame.Rect(self.x, Floor.floor_level-self.bottom_height, self.width, self.bottom_height)
        pygame.draw.rect(window, (50, 50, 50), self.bottom_rect)

        self.top_rect = pygame.Rect(self.x, 0, self.width, self.top_height)
        pygame.draw.rect(window, (50, 50, 50), self.top_rect)

    def move(self):
        self.x -= 1
        if self.x + Obstacles.width <=50:
            self.passed = True
        if self.x <= -self.width:
            self.deleteNow = True
            