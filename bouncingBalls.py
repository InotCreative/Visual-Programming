import pygame
import random
import typing
import sys

WIDTH: int = 800
HEIGHT: int = 600
SPEED: int = 7
NUMBER_OF_BALLS: int = 300

class Balls:
    def __init__(self):
        self.radius: int = random.randint(7, 25)
        self.xPos: int = random.randint(self.radius, WIDTH - self.radius)
        self.yPos: int = random.randint(self.radius, HEIGHT - self.radius)
        self.xSpeed: int = SPEED
        self.ySpeed: int = SPEED
        self.color: typing.Tuple[int, int, int] = tuple(random.randint(0, 255) for _ in range(3))
        self.opacity: int = random.randint(100, 255)
    
    def showBalls(self, screen: pygame.Surface) -> None:        
        pygame.draw.circle(screen, self.color, (self.xPos, self.yPos), self.radius, 0)


def setup() -> typing.Tuple[pygame.Surface, pygame.time.Clock, typing.List[Balls]]:
    pygame.init()
    
    pygame.display.set_caption("BOUNCING BALLS")
    screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
    clock: pygame.time.Clock = pygame.time.Clock()
    
    arraysOfBalls: typing.List[Balls] = [Balls() for _ in range(NUMBER_OF_BALLS)]
    
    return screen, clock, arraysOfBalls

def draw(screen: pygame.Surface, clock: pygame.time.Clock, arrayOfBalls: typing.List[Balls]):
    isRunning: bool = True
    
    while (isRunning):
        screen.fill((255, 255, 255))
        
        for balls in arrayOfBalls:
            balls.showBalls(screen)
            
            if (balls.xPos <= balls.radius or balls.xPos >= WIDTH - balls.radius):
                balls.xSpeed = -balls.xSpeed
            if (balls.yPos <= balls.radius or balls.yPos >= HEIGHT - balls.radius):
                balls.ySpeed = -balls.ySpeed
            
            balls.xPos += balls.xSpeed
            balls.yPos += balls.ySpeed

        clock.tick(60)

        pygame.display.flip()
                
        
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                isRunning = False
    
    pygame.quit()
    sys.exit()

def main():
    screen, clock, arrayOfBalls = setup()
    draw(screen, clock, arrayOfBalls)

if __name__ == "__main__":
    main()