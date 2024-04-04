import components
import constants
import population
from sys import exit
import pygame

pygame.init()
clock = pygame.time.Clock()
population = population.Population(100)

def gen_obstacles():
    constants.obstacles.insert(0, components.Obstacles(constants.window_w))

def quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def main():
    spawn_now = 10
    while True:
        quit()
        constants.window.fill((200, 200, 200))

        constants.floor.create(constants.window)

        if spawn_now <= 0:
            gen_obstacles()
            spawn_now = constants.obstacle_gen_rate
        spawn_now-=1

        for obs in constants.obstacles:
            obs.create(constants.window)
            obs.move()
            if obs.deleteNow:
                constants.obstacles.remove(obs)
        if not population.exinct():
            population.update_live_players()
        else: 
            constants.obstacles.clear()
            population.natural_selection()

        clock.tick(60)
        pygame.display.flip()

main()