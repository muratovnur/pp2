import pygame
import math
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
lr_margin = 50
t_margin = 20
b_margin = 80
padding = 30

size = width, height = (1000, 800)
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))

graph = pygame.Surface([840, 640])
graph.fill((255, 255, 255))

coorSin = []
coorCos = []
n = 6
A = 320

font = pygame.font.Font('freesansbold.ttf', 18)

valsy = ['1.00', '0.75', '0.50', '0.25', '0.00', '-0.25', '-0.50', '-0.75', '-1.00']
valsx = ['-3p', '-5p/2', '-2p', '-3p/2', '-p', '-p/2', '0', 'p/2', 'p', '3p/2', '2p', '5p/2', '3p']
for x in range(width):
    y = int(math.sin(x / 840 * math.pi * n) * A + 320)
    coorSin.append([x, y])

for x in range(width):
    y = int(math.cos(x / 840 * math.pi * n) * A + 320)
    coorCos.append([x, y])

pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(50, 20, 900, 700), 2)
pygame.draw.lines(graph, (255, 0, 0), False, coorSin, 2)
pygame.draw.lines(graph, (0, 0, 255), False, coorCos, 2)
a = 80
b = 50
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
    for i in range(7):
        pygame.draw.line(screen, BLACK, (a, 20), (a, 720))
        a += 140
    a = 0
    for i in range(7):
        pygame.draw.line(graph, BLACK, (a, 0), (a, 700))
        a += 140

    for i in range(9):
        pygame.draw.line(screen, BLACK, (50, b), (950, b))
        b += 80
    b = 0
    for i in range(9):
        pygame.draw.line(graph, BLACK, (0, b), (920, b))
        b += 80

    q = 0
    for n in valsy:
        text = font.render(n, True, BLACK)
        screen.blit(text, (10, 44 + q))
        q += 80
    q = 0
    for n in valsx:
        text = font.render(n, True, BLACK)
        screen.blit(text, (65+q, 720))
        q += 71
    screen.blit(graph, (80, 50))

    pygame.draw.line(screen, BLACK, (lr_margin, t_margin + (height-t_margin-b_margin)/2),
                     (width-lr_margin, t_margin + (height-t_margin-b_margin)/2), 2)
    pygame.draw.line(screen, BLACK, (width/2, t_margin), (width/2, height - b_margin), 2)

    pygame.display.flip()
pygame.quit()
