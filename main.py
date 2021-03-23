import pygame, sys

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MarioMiniGame")

WHITE=(255,255,255)
BLACK= (0,0,0)
BORDER = pygame.Rect(WIDTH/2 -5, 0, 10, HEIGHT)

FPS = 60
VEL = 5
#Need to get this to load in, then resize, then move, then work on collision
marioCharacterImage = pygame.image.load(os.path.join('assets', 'maryo.png'))
mario = pygame.transform.scale(marioCharacterImage, (55, 45))

bowserCharacterImage= pygame.image.load(os.path.join('assets', 'bowser.png'))
bowser = pygame.transform.scale(bowserCharacterImage, (55, 45))

def draw_window(mario, bowser):
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, BORDER)
    WIN.blit(marioCharacterImage,(mario.x, mario.y))
    WIN.blit(bowserCharacterImage, (bowser.x, bowser.y))
    pygame.display.update()
#Next two functions are for movement and borders
def mario_movement(keys_pressed, mario):
        if keys_pressed[pygame.K_a] and mario.x - VEL > 0: #left movement key
            mario.x-= VEL
        if keys_pressed[pygame.K_d] and mario.x + VEL + mario.width < BORDER.x: #right movement key
            mario.x+= VEL
        if keys_pressed[pygame.K_w] and mario.y - VEL > : #Up movement key 
            mario.y-= VEL
        if keys_pressed[pygame.K_s] and mario.y + VEL + mario.height < HEIGHT: #down movement key 
            mario.y-= VEL

def bowser_movement(keys_pressed, bowser):
        if keys_pressed[pygame.K_LEFT]: #left movement key
            bowser.x-= VEL
        if keys_pressed[pygame.K_RIGHT]: #right movement key
            bowser.x+= VEL
        if keys_pressed[pygame.K_UP]: #Up movement key 
            bowser.y-= VEL
        if keys_pressed[pygame.K_DOWN]: #down movement key 
            bowser.y-= VEL

def main():
    #part of function to make them move
    mario = pygame.Rect(100,300)
    bowser = pygame.Rect(700, 300)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run == False

        keys_pressed = pygame.key.get_pressed()
        mario_movement(keys_pressed, mario)
        bowser_movement(keys_pressed, bowser)
        draw_window(mario, bowser)

    pygame.quit()

if __name__ == "__main__":
    main()