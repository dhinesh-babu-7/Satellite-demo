import math
import pygame

pygame.init()

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

cx = WIDTH // 2
cy = HEIGHT // 2

radius = 150

angle = 0

running = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    angle += 0.02
    
    x = cx + radius * math.cos(angle)
    y = cy + radius * math.sin(angle)
    
    screen.fill((0, 0, 0))
    
    pygame.draw.circle(screen, (50, 50, 50), (cx, cy), 80)
    pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 10)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()