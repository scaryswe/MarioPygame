import pygame, sys

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MarioMiniGame")

WHITE=(255,255,255)
BLACK= (0,0,0)

FPS = 60

marioCharacterImage = pygame.image.load(os.path.join('assets', 'maryo.png'))

def draw_window():
    WIN.fill(WHITE)
    WIN.blit(marioCharacterImage,(300, 100))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run == False
        draw_window

    pygame.quit()
    if __name__ == "__main__":
        main()