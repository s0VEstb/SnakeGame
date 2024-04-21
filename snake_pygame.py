import pygame
from random import randrange

RES = 800
Size = 50

pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
image = pygame.image.load('pxfuel-6.jpg').convert()

while True:
    x, y = randrange(0, RES, Size), randrange(0, RES, Size)
    apple = randrange(0, RES, Size), randrange(0, RES, Size)
    dirs = {"W": True, "S": True, "A": True, "D": True}
    length = 1
    score = 0
    snake = [(x, y)]
    dx, dy = 0, 0
    fps = 8

    while True:
        sc.blit(image, (0, 0))
        [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, Size - 2, Size - 2))) for i, j in snake]
        pygame.draw.rect(sc, pygame.Color('red'), (*apple, Size, Size))
        render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
        sc.blit(render_score, (5, 5))
        x += dx * Size
        y += dy * Size
        snake.append((x, y))
        snake = snake[-length:]
        if snake[-1] == apple:
            apple = randrange(0, RES, Size), randrange(0, RES, Size)
            length += 1
            score += 1
            fps += 0.2
        if x < 0 or x > RES - Size or y < 0 or y > RES - Size or len(snake) != len(set(snake)):
            while True:
                render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
                render_end2 = font_end.render('Press C to Restart !', 1, pygame.Color('orange'))
                sc.blit(render_end, (RES // 2 - 200, RES // 3))
                sc.blit(render_end2, (RES // 2 - 300, RES // 2))
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                        break
                else:
                    continue
                break
            break

        pygame.display.flip()
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        key = pygame.key.get_pressed()
        if key[pygame.K_w] and dirs["W"]:
            dx, dy = 0, -1
            dirs = {"W": True, "S": False, "A": True, "D": True}
        if key[pygame.K_s] and dirs["S"]:
            dx, dy = 0, 1
            dirs = {"W": False, "S": True, "A": True, "D": True}
        if key[pygame.K_a] and dirs["A"]:
            dx, dy = -1, 0
            dirs = {"W": True, "S": True, "A": True, "D": False}
        if key[pygame.K_d] and dirs["D"]:
            dx, dy = 1, 0
            dirs = {"W": True, "S": True, "A": False, "D": True}