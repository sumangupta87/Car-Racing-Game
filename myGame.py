import pygame,time,random
pygame.init()
display_width=800
display_height=600
black=(0,0,0)
white=(255,255,255)   #(R,G,B)
red=(250,0,0)
blue=(0,0,255)
car_width = 100  #set by photoshop
car_height = 160 #set by photoshop

gameDisplay=pygame.display.set_mode((display_width,display_height))   #create the display
pygame.display.set_caption('Racing game')         #create the caption
clock=pygame.time.Clock()                       #create game clock

carImg = pygame.image.load('C:\\Users\\myCarFinal.png')   #load the car image
#carImg = pygame.transform.scale(carImg,(100,160))  #if car size is huge add this line to reduce the image and fit in the game

def car(x,y):
    gameDisplay.blit(carImg,(x,y))   #blit - drawing something in surface.Here x,y is the starting position of the car

def text_objects(text,font):
    textSurface = font.render(text,True,blue)   #create a surface/True for antialiasing - that is smoothing the texts
    return textSurface, textSurface.get_rect()  #create rectangle around the text surface

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)    #text font and size
    TextSurf, TextRect = text_objects(text, largeText)  #surface and rectangle around the text
    TextRect.center = ((display_width/2),(display_height/2)) #setting position of the text rectangle by giving middle co-ordinates
    gameDisplay.blit(TextSurf, TextRect)  #display the text
    pygame.display.update()   #update the display
    time.sleep(7)
    game_loop()

def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def score_cal(count):
    font = pygame.font.SysFont(None,25)   #setting font for score declaration
    text = font.render("Score: "+str(count),True,black)
    gameDisplay.blit(text, (0,0))
    


def crash():
    soundObj = pygame.mixer.Sound('C:\\Users\\Crash.wav')
    soundObj.play()
    time.sleep(0.5)
    message_display('You Crashed')
    soundObj.stop()

def game_loop():
   
    x=(display_width*0.45)
    y=(display_height*0.8)
    x_change = 0  #changing the car position - initially set to zero

#specifying start position,lenght width speed of rec
    thing_width = 100
    thing_height = 160
    thing_startx = random.randrange(0, display_width-100)
    thing_starty = -600
    thing_speed = 3

    i = 0
    
        

    gameExit = False                                 

    while not gameExit:
        pygame.mixer.music.load('C:\\Users\\Ferrari.wav')  #load the music file
        pygame.mixer.music.play(-1, 0.0)        #play the music file,-1 : play infinitely,0.0 - start from 0s position
        #sound1Obj = pygame.mixer.Sound('C:\\Users\\Ferrari.wav')
        #sound1Obj.play()


        
        for event in pygame.event.get():   #fetch all event in the screen
            if event.type == pygame.QUIT:   #quit game when press X
                pygame.mixer.music.stop()           #stop the music
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:  #if any key is pressed
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change=0
        
        #x=x+x_change            
                
        gameDisplay.fill(white)     #coloring the display in white

        #things(thingx,thingy,thingw,thingh,color)
        things(thing_startx,thing_starty,thing_width,thing_height,red)
        thing_starty+=thing_speed

        things(thing_startx+300,thing_starty,thing_width,thing_height,red)
        thing_starty+=thing_speed

        x=x+x_change

        car(x,y)            #display the car - it should be after previous line
        score_cal(i)        

        if x > display_width - car_width or x<0:   #defining boundary - for right side we need to minus car width as x is top left corner of the car
            gameExit = True
            pygame.mixer.music.stop()
            #sound1Obj.stop()
            crash()

        if thing_starty > display_height:               #if block is out of screen
            thing_starty = 0 - thing_height              #reseting blok y position
            thing_startx = random.randrange(0, display_width-thing_width-300)
            i+=2

        if i > 20:
            thing_speed=5
        elif i>30:
            thing_speed=7
            thing_width+=10
        elif i>40:
            thing_speed=10
        elif i>50:
            thing_speed=15
            thing_width+=40
        elif i>60:
            thing_speed=30
            thing_width+=40
        
            

        if (thing_starty+thing_height)>= y:
            if (thing_startx >=x or (thing_startx+thing_width) >=x) and thing_startx <= (x+car_width):
                pygame.mixer.music.stop()       #stop music
                #sound1Obj.stop()
                crash()

            elif (thing_startx+300 >=x or (thing_startx+300+thing_width) >=x) and (thing_startx+300) <= (x+car_width):
                pygame.mixer.music.stop()       #stop music
                #sound1Obj.stop()
                crash()

        pygame.display.update()   #update the display
        clock.tick(60)            #how fast and smooth it will move

game_loop()

pygame.quit()
quit()

    
