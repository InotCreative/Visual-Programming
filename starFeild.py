import pygame
import random
import sys
import numpy
import typing

WIDTH: int = 800
HEIGHT: int = 600
BLACK: typing.Tuple[int, int, int] = (0, 0, 0)
WHITE: typing.Tuple[int, int, int] = (255, 255, 255)
numberOfStars: int = 1000
starSpeed: float = 3
lineLengthMultiplier: float = 3  # This controls how long the line will be

class Star:
    def __init__(self):
        self.x: int = random.randrange(-WIDTH, WIDTH)
        self.y: int = random.randrange(-HEIGHT, HEIGHT)
        self.z: int = random.randrange(1, WIDTH) 
        self.previousZ: int = self.z
        self.previousX: int = self.x
        self.previousY: int = self.y
    
    def update(self) -> None:
        self.z = self.z - starSpeed
        
        if self.z < 1:
            self.z = WIDTH // 2
            self.x: int = random.randrange(-WIDTH, WIDTH)
            self.y: int = random.randrange(-HEIGHT, HEIGHT)
            self.previousZ = self.z 
            self.previousX = self.x
            self.previousY = self.y
    
    def show(self, screen) -> None:
        normX: float = self.x / self.z
        normY: float = self.y / self.z
        
        newStarX: int = int(numpy.interp(normX, [-1, 1], [0, WIDTH]))
        newStarY: int = int(numpy.interp(normY, [-1, 1], [0, HEIGHT]))
        
        sizeOfStar: int = int(numpy.interp(self.z, [0, WIDTH], [4, 0]))

        pygame.draw.circle(screen, WHITE, (newStarX, newStarY), sizeOfStar)
        
        # Draw line from the previous position to the current position
        lineX: int = int(numpy.interp((self.previousX / self.previousZ), [-1, 1], [0, WIDTH]))
        lineY: int = int(numpy.interp((self.previousY / self.previousZ), [-1, 1], [0, HEIGHT]))
        
        # Calculate direction vector from the previous to the current star position
        deltaX = newStarX - lineX
        deltaY = newStarY - lineY
        
        # Scale the direction vector to make the line longer
        lineX2 = int(lineX - deltaX * lineLengthMultiplier)  # Multiply by a factor to extend the line
        lineY2 = int(lineY - deltaY * lineLengthMultiplier)
        
        # Draw the extended line
        pygame.draw.line(screen, WHITE, (lineX2, lineY2), (newStarX, newStarY))
        
        self.previousX = self.x
        self.previousY = self.y
        self.previousZ = self.z

def setup():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Starfield Simulation")

    arrayOfStars: typing.List[Star] = []
    
    for i in range(numberOfStars):
        arrayOfStars.append(Star())    
    
    clock = pygame.time.Clock()
    return screen, arrayOfStars, clock

def draw(screen, arrayOfStars, clock):
    global starSpeed
    running: bool = True
    
    while running:
        screen.fill(BLACK)
        
        mouseX, _ = pygame.mouse.get_pos()
        
        # Adjust star speed based on the mouse position
        starSpeed = 0.1 + numpy.interp(mouseX, [0, 800], [2, 10])
                     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        for star in arrayOfStars:
            star.show(screen)       
            star.update() 
        
        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()
    sys.exit()

def main():
    screen, arrayOfStars, clock = setup()
    draw(screen, arrayOfStars, clock)

if __name__ == "__main__":
    main()
