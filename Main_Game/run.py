import pygame

pygame.init()
pygame.display.set_caption('Python123')

window = pygame.display.set_mode((1280, 640))
bg = pygame.image.load('background.png')


def redrawGameLoop():
    global walkCount
    window.blit(bg, (0, 0))
    pygame.display.update()


# MainLoop
run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and x > vel:
        x -= vel
    if keys[pygame.K_d] and x < 500 - width - vel:
        x += vel
    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
        else:
            if jumpCount >= 10:
                negative = 1
                if jumpCount < 0:
                    negative = -1
                y -= (jumpCount ** 2) * 0.5 * negative
                jumpCount -= 1

            redrawGameLoop()
