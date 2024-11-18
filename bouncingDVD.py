import pygame
import numpy
import typing
import random
import sys

WIDTH: int = 800
HEIGHT: int = 600

SPEED = 3

BLACK: typing.Tuple[int, int, int] = (0, 0, 0)

def setup() -> typing.Tuple[pygame.Surface, pygame.time.Clock, pygame.Surface]:
    pygame.init()
    pygame.display.set_caption("BOUNCING DVD")
    
    screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
    clock: pygame.time.Clock = pygame.time.Clock()
    image: pygame.Surface = pygame.image.load(r"\Users\abina\Desktop\Visual-Programming\Bouncing DVD\dvd.png")
    image = pygame.transform.scale(image, (200, 200))
    
    return screen, clock, image

def changeColor(image: pygame.Surface) -> pygame.Surface:
    color: typing.List[int, int, int] = [random.randint(0, 255) for _ in range(3)]  # Random RGB color
    tint: pygame.Surface = pygame.Surface(image.get_size(), pygame.SRCALPHA)

    tint.fill((*color, 0))
    
    imageCopy: pygame.Surface = image.copy()
    imageCopy.blit(tint, (0, 0), special_flags=pygame.BLEND_RGB_MULT)
        
    return imageCopy
    

def draw(screen: pygame.Surface, clock: pygame.time.Clock, image: pygame.Surface) -> None:
    isRunning: bool = True
    
    xPos: int = random.randrange(1, WIDTH - 200)
    yPos: int = random.randrange(1, HEIGHT - 200)
    xSpeed = SPEED
    ySpeed = SPEED
    
    while (isRunning):
        screen.fill(BLACK)
    
        xPos += xSpeed
        yPos += ySpeed
        
        if (xPos <= 0 or xPos + 200 >= WIDTH):
            xSpeed = -xSpeed
            image = changeColor(image)
        if (yPos <= 0 or yPos + 200 >= HEIGHT):
            ySpeed = -ySpeed
            image = changeColor(image)
            
        screen.blit(image, (xPos, yPos))
        pygame.display.flip()
        clock.tick(60)
        
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                isRunning = False
    
    pygame.quit()
    sys.exit()

def main():
    screen, clock, image = setup()
    draw(screen, clock, image)
    
if __name__ == main():
    main()