import pygame, sys

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MarioMiniGame")

WHITE=(255,255,255)
BLACK= (0,0,0)
BORDER = pygame.Rect(WIDTH//2 -5, 0, 10, HEIGHT)

FPS = 60
VEL = 5
FIREBALL_VEL = 7
NUM_FIREBALLS = 10
marioHIT = pygame.USEREVENT +1
bowserHIT = pygame.USEREVENT +2

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
        if keys_pressed[pygame.K_LEFT] and bowser.x - VEL > BORDER.x + BORDER.width: #left movement key
            bowser.x-= VEL
        if keys_pressed[pygame.K_RIGHT] and bowser.x + VEL + bowser.width < WIDTH: #right movement key
            bowser.x+= VEL
        if keys_pressed[pygame.K_UP] and bowser.y - VEL > : #Up movement key 
            bowser.y-= VEL
        if keys_pressed[pygame.K_DOWN] and bowser.y + VEL + bowser.height < HEIGHT: #down movement key 
            bowser.y-= VEL

def handle_fireballs(mario_fireballs, bowser_fireballs, mario, bowser):
    for fireball in mario_fireballs:
        fireball.x += FIREBALL_VEL
        if bowser.colliderect(fireball):
            pygame.event.post(pygame.event.Event(bowserHIT))
            mario_fireballs.remove(fireball)
    for fireball in bowser_fireballs:
        fireball.x -= FIREBALL_VEL
        if mario.colliderect(fireball):
            pygame.event.post(pygame.event.Event(marioHIT))
            bowser_fireballs.remove(fireball)


def main():
    #part of function to make them move
    mario = pygame.Rect(100,300)
    bowser = pygame.Rect(700, 300)

    mario_fireballs = []
    bowser_fireballs = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run == False
            if event.type == pygame.KEYDOWN:
                if event.key = pygame.K_LCTRL and len(mario_fireballs) < NUM_FIREBALLS:
                    fireball = pygame.Rect(mario.x + mario.width, mario.y + mario.height//2 - 2, 10, 5)
                    mario_fireballs.append(fireball)

                if event.key = pygame.K_RCTRL and len(bowser_fireballs) < NUM_FIREBALLS:
                    fireball = pygame.Rect(bowser.x, bowser.y + bowser.height//2 - 2, 10, 5)
                    bowser_fireballs.append(fireball)

        keys_pressed = pygame.key.get_pressed()
        mario_movement(keys_pressed, mario)
        bowser_movement(keys_pressed, bowser)
        handle_fireballs(mario_fireballs, bowser_fireballs, mario, bowser)
        draw_window(mario, bowser)

    pygame.quit()

if __name__ == "__main__":
    main()