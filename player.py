import random
import pygame
import perceptron

import constants

class Player:
    def __init__(self):
        self.x, self.y = 50, 400
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
        self.color = random.randint(0, 150), random.randint(0, 150), random.randint(0, 150)
        self.vel = 0
        self.isJump = False
        self.isAlive = True
        self.lifespan = 0
        
        self.decision = None
        self.vision = [0.5, 1, 0.5]
        self.inputs = 3
        self.fitness = 0
        self.perceptron = perceptron.Perceptron(self.inputs)
        self.perceptron.generate_net()

    def create(self, window):
        pygame.draw.rect(window, self.color, self.rect)


    #collision functions
    def hit_ground(self, ground):
        return pygame.Rect.colliderect(self.rect, ground)
    def hit_sky(self):
        return bool(self.rect.y<10)
    def hit_obstacle(self):
        if len(constants.obstacles):
            return pygame.Rect.colliderect(self.rect, constants.obstacles[-1].top_rect) or pygame.Rect.colliderect(self.rect, constants.obstacles[-1].bottom_rect)
    
    def update(self, ground):
        if not (self.hit_ground(ground) or self.hit_obstacle()):
            self.vel += 0.25
            self.rect.y += self.vel
            if self.vel > 5:
                self.vel = 5
            self.lifespan += 1
        else:
            self.isAlive, self.isJump = False, False
            self.vel = 0

    def jump(self):
        if not self.isJump and not self.hit_sky():
            self.isJump = True
            self.vel = -5
        if self.vel >= 1.7:
            self.isJump = False #jump cooldown
    
    @staticmethod
    def closest_pipe():
        for i in reversed(range(len(constants.obstacles))):
            if not constants.obstacles[i].passed:
                return constants.obstacles[i]

    def look(self):
        if constants.obstacles:
            #to the top of the opening
            self.vision[0] = max(0, self.rect.center[1] - self.closest_pipe().top_rect.bottom)/constants.window_h
            pygame.draw.line(constants.window, self.color, self.rect.center, (self.rect.center[0], constants.obstacles[-1].top_rect.bottom))

            #to the bottom of the opening
            self.vision[2] = max(0, self.rect.center[1] - self.closest_pipe().bottom_rect.top)/constants.window_h
            pygame.draw.line(constants.window, self.color, self.rect.center, (self.rect.center[0], constants.obstacles[-1].bottom_rect.top))

            #to the middle of the opening
            self.vision[1] = max(0, self.closest_pipe().x - self.rect.center[0])/constants.window_w
            pygame.draw.line(constants.window, self.color, self.rect.center, (constants.obstacles[-1].x, self.rect.center[1]))

    def decide(self):
        self.decision = self.perceptron.feed_forward(self.vision)
        if self.decision > 0.73:
            self.jump()

    def calculate_fitness(self):
        self.fitness = self.lifespan

    def clone(self):
        clone = Player()
        clone.fitness = self.fitness
        clone.perceptron = self.perceptron.clone()
        clone.perceptron.generate_net()
        return clone

    