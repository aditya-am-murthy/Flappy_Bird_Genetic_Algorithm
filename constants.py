import components
import pygame

window_h = 800
window_w = 800

obstacle_gen_rate = 300

window = pygame.display.set_mode((window_w , window_h))

floor = components.Floor(window_w)
obstacles = []