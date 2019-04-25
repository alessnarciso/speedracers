#first game in python: Speed Racers - game of dodging obstacles with a car to obtain a score

#libraries
import pygame

#initialize pygame
pygame.init()

#display parameters, 800px wide by 600px tall
display_width = 800
display_height = 600

#settings for display
gameDisplay = pygame.display.set_mode((display_width,display_height)) 

#game title
pygame.display.set_caption('Speed Racers')

#colors
black = (0,0,0)
white = (255,255,255)

#initialize game clock for time tracking and FPS -- 30 FPS ideal
clock = pygame.time.Clock()

#game crash logic, set to initially false
crashed = False

#initialize default x_change to 0 when no key is pressed
x_change = 0

#car object
carImg = pygame.image.load('racecar.png')
def car(x,y):
    gameDisplay.blit(carImg, (x,y))

#define car object dimensions
x =  (display_width * 0.45)
y = (display_height * 0.8)

#game loop
while not crashed:

    #set crashed to true if crash happens
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        #movement logic for car
        # keydown event if any key being pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

    #update x variable for object movement
    x += x_change
    
    gameDisplay.fill(white)
    car(x,y)

    pygame.display.update()
    clock.tick(60) #run at 60 FPS

pygame.quit()
quit()




    
