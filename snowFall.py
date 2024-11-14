import pygame
import typing
import random
import sys
import numpy

BLACK: typing.Tuple[int, int, int] = (0, 0, 0)
WHITE: typing.Tuple[int, int, int] = (255, 255, 255)

NUMBER_OF_SNOW_FLAKES = 900

HEIGHT: int = 600
WIDTH: int = 800

class SnowFlakes:
    def __init__(self):
        self.xPos: int = random.randrange(0, WIDTH)
        self.yPos: int = random.randrange(0, HEIGHT)
        self.size: int = random.randint(2, 6)
        self.snowFallSpeed: int = random.randrange(0, WIDTH)
        self.snowFallSpeed: int = int(numpy.interp(self.snowFallSpeed, [0, WIDTH], [4, 10]))
    
    def update(self):
        self.yPos += self.snowFallSpeed
        
        if (self.yPos > HEIGHT):
            self.yPos = random.randint(-50, -10)
            self.xPos = random.randrange(0, WIDTH)
            
    def show(self, screen):
        pygame.draw.circle(screen, WHITE, (self.xPos, self.yPos), self.size)

def setup():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snowfall")
    
    clock = pygame.time.Clock()
    arrayOfSnowflakes: typing.List[SnowFlakes] = [SnowFlakes() for _ in range(NUMBER_OF_SNOW_FLAKES)]
    
    return screen, clock, arrayOfSnowflakes

def draw(screen: pygame.Surface, clock, arrayOfSnowflakes: typing.List[SnowFlakes]):
    isRunning: bool = True
    
    while (isRunning):
        screen.fill(BLACK)
        
        for snowFlakes in arrayOfSnowflakes:
            snowFlakes.show(screen)
            snowFlakes.update()
        
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                isRunning = False
                
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

def main():
    screen, clock, arrayOfSnowflakes = setup()
    draw(screen, clock, arrayOfSnowflakes)

if __name__ == "__main__":
    main()