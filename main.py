import pygame, sys

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MarioMiniGame")

WHITE=(255,255,255)
BLACK= (0,0,0)

FPS = 60
VEL = 5
#Need to get this to load in, then resize, then move, then work on collision
marioCharacterImage = pygame.image.load(os.path.join('assets', 'maryo.png'))
mario = pygame.transform.scale(marioCharacterImage, (55, 45))

bowserCharacterImage= pygame.image.load(os.path.join('assets', 'bowser.png')
bowser = pygame.transform.scale(bowserCharacterImage, (55, 45))

def draw_window():
    WIN.fill(WHITE)
    WIN.blit(marioCharacterImage,(mario.x, mario.y))
    WIN.blit(bowserCharacterImage, (bowser.x, bowser.y))
    pygame.display.update()

def mario_movement(keys_pressed, mario):
        if keys_pressed[pygame.K_a]: #left movement key
            mario.x-= VEL
        if keys_pressed[pygame.K_d]: #right movement key
            mario.x+= VEL
        if keys_pressed[pygame.K_w]: #Up movement key 
            mario.y-= VEL
        if keys_pressed[pygame.K_s]: #down movement key 
            mario.y-= VEL

def main():
    #part of function to make mario move
    mario = pygame.Rect(100,300)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run == False

        keys_pressed = pygame.key.get_pressed()

        draw_window

    pygame.quit()
    if __name__ == "__main__":
        main()