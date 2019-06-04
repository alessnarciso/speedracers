#Speed Racers - game of dodging obstacles with a car to obtain a score
#Python 3.7.3

#libraries
import pygame
import time
import random

#initialize pygame
pygame.init()

#display parameters, 800px wide by 600px tall
display_width = 800
display_height = 600

#colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

#car object
carImg = pygame.image.load('racecar.png')
car_width = 73

#settings for display
gameDisplay = pygame.display.set_mode((display_width,display_height)) 
#game title
pygame.display.set_caption('Speed Racers')
#initialize game clock for time tracking and FPS -- 30 FPS ideal
clock = pygame.time.Clock()

#car function
def car(x,y):
    gameDisplay.blit(carImg, (x,y))

#obstacles function; inputs: x and y starting points, width, height, color
def things(thingx, thingy, thingw, thingh, color):
    #draw object with specifications
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
    
#text objects function
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#counter for score / obstacles dodged
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

#message display function
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',65)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    #sleep and dislay for 5 seconds
    time.sleep(5)
    
#crash event function
def crash():

    #call message display for text
    message_display('Oh no, you crashed!')
    #go back to game loop
    game_loop()
    
#game loop
def game_loop():
    #define car object dimensions
    x =  (display_width * 0.45)
    y = (display_height * 0.8)

    #initialize default x_change to 0 when no key is pressed
    x_change = 0

    #obstacles generated

    #random x loocation generation within display range
    thing_startx = random.randrange(0, display_width)
    #start at top of screen
    thing_starty = -600
    #speed (pixels per second) -- increase for higher difficulty
    thing_speed = 7
    #obstacle size
    thing_width = 100
    thing_height = 100

    #counters
    thingCount = 1
    dodged = 0
    
    gameExit = False
    
    while not gameExit:

        #game exit logic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
    
        #movement logic for car
        #keydown event = if any key being pressed
                
            #left key being pressed x change    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                    
            #right key being pressed x change
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            #if not being pressed, no change in x       
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        #update x variable for object movement
        x += x_change
        gameDisplay.fill(white)

        #define obstalce width and height
        #format: things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed

        #call counter
        things_dodged(dodged)
        
        car(x,y)

        #bounday conditions for car: if car passes side boundaries, crash function
        if x > display_width - car_width or x < 0:
            crash()
            pygame.quit()
            quit()

        #obstacle handling
        if thing_starty > display_height:
            #so block appears off screen
            thing_starty = 0 - thing_height
            #redefine x position to be on screen
            thing_startx = random.randrange(0,display_width)

            #score count / increase speed and obstacle size
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)

        #obstacle crash logic -- for testing on shell, should comment out or will lag
        #if y < thing_starty+thing_height:
        #   print('y crossover')
        #
        #    if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
        #       print('x crossover')
        #       crash()
                
        pygame.display.update()
        clock.tick(60) #run at 60 FPS


game_loop()
pygame.quit()
quit()




    
