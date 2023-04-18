import pygame
pygame.init()  
pygame.display.set_caption("sprite sheet")  # sets the window title
screen = pygame.display.set_mode((1600, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3

a=0
d=1
w = 2
s = 3

#MAP: 1 is grass, 2 is brick
map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2 ,2 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

wood = pygame.image.load('wood.png')
brick = pygame.image.load('brick.png') #load your spritesheet
dirt = pygame.image.load('dirt.png') #load your spritesheet
Link = pygame.image.load('link.png') #load your spritesheet
Link.set_colorkey((255, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)
Cat = pygame.image.load('link.png')
Cat.set_colorkey((255, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)

#player variables
xpos = 400 #xpos of player
ypos = 400 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
xpos2 = 400 #xpos of player2
ypos2 = 400 #ypos of player2
vx2 = 0 #x velocity of player2
vy2 = 0 #y velocity of player2
offset = 0
offset2 = 0
keys = [False, False, False, False] #this list holds whether each key has been pressed
keys2 = [False, False, False, False]
isOnGround = False
isOnGround2 = False #this variable stops gravity from pulling you down more when on a platform
moving = False
moving2 = False

#animation variables variables
frameWidth = 32
frameHeight = 48
RowNum = 0 #for left animation, this will need to change for other animations
frameNum = 0
ticker = 0
direction = DOWN

frameWidth2 = 32
frameHeight2 = 48
RowNum2 = 0 #for left animation, this will need to change for other animations
frameNum2 = 0
ticker2 = 0
direction2 = DOWN

while not gameover:
    clock.tick(60) #FPS
   
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
     
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=True
            elif event.key == pygame.K_UP:
                keys[UP]=True
            elif event.key == pygame.K_a:
                keys2[LEFT]=True
            elif event.key == pygame.K_d:
                keys2[RIGHT]=True
            elif event.key == pygame.K_w:
                keys2[UP]=True
        

        #PLAYER 2 INPUT
        elif event.type == pygame.KEYUP: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=False
            elif event.key == pygame.K_UP:
                keys[UP]=False
            elif event.key == pygame.K_a:
                keys2[LEFT]=False
            elif event.key == pygame.K_d:
                keys2[RIGHT]=False
            elif event.key == pygame.K_w:
                keys2[UP]=False
         

    #LEFT MOVEMENT
    if keys[LEFT]==True:
        if xpos > 400:
            vx = -5
        elif offset<0:
            offset+=5
            vx =0
        else:
            vx = -5
        RowNum = 0
        direction = LEFT
        moving = True
       
    #RIGHT MOVEMENT
    elif keys[RIGHT] == True:
        if xpos<400:
            vx=5
        elif offset>-1700:
            offset-=5
            vx = 0

        else:
            vx = 5
        RowNum = 1
        direction = RIGHT
        moving = True
    #turn off velocity
    else:
        vx = 0
        moving = False
       
        #JUMPING
    if keys[UP] == True and isOnGround == True: #only jump when on the ground
        vy = -8
        RowNum = 2
        isOnGround = False
        direction = UP
        moving = True
   
   
       
    xpos+=vx #update player xpos
    ypos+=vy
    print(vx, vy)

    #PLAYER 2 MOVEMENT
     #LEFT MOVEMENT
    if keys2[a]==True:
        if xpos2 > 400:
            vx2 = -3
        #elif offset2<0:
            #offset2+=3
            #vx2 =0
        else:
            vx2 = -3
            RowNum2 = 0
            direction2 = LEFT
            moving2 = True
       
    #RIGHT MOVEMENT
    elif keys2[d] == True:
        if xpos2<400:
            vx2=3
        #elif offset2>-1700:
            #offset2-=3
            #vx2 = 0
        else:
            vx2 = 3
            RowNum2 = 1
            direction2 = RIGHT
            moving2 = True
    #turn off velocity
    else:
        vx2 = 0
        moving2 = False
       
        #JUMPING
    if keys2[w] == True and isOnGround2 == True:#only jump when on the ground
        vy2 = -8
        RowNum2 = 2
        isOnGround2 = False
        direction2 = UP
        moving2 = True
   
   
       
    xpos2+=vx2 #update player xpos
    ypos2+=vy2
    print(vx2, vy2)
   
    #COLLISION
   
    #collision with feetsies
    if map[int((ypos+frameHeight)/50)][int((xpos-offset+frameWidth/2)/50)]==1 or map[int((ypos+frameHeight)/50)][int((xpos-offset+frameWidth/2)/50)]==2 or map[int((ypos+frameHeight)/50)][int((xpos-offset+frameWidth/3)/50)]==3:
        isOnGround = True
        vy=0
       
    else:
        isOnGround = False
       
    #bump your head, ouch!
    if map[int((ypos)/50)][int((xpos-offset+frameWidth/2)/50)]==1 or map[int((ypos)/50)][int((xpos-offset+frameWidth/2)/50)]==2 or map[int((ypos)/50)][int((xpos-offset+frameWidth/3)/50)]==3:
        vy=0
       
    #left collision (it's extra long because we check both head and feets(well, knees) for left collision
    if (map[int((ypos+frameHeight-10)/50)][int((xpos-offset-10)/50)]==1 or map[int((ypos)/50)][int((xpos-offset-10)/50)]==1 or map[int((ypos+frameHeight-10)/50)][int((xpos-offset-10)/50)]==2 or map[int((ypos)/50)][int((xpos-offset-10)/50)]==2 or map[int((ypos+frameHeight-10)/50)][int((xpos-offset-10)/50)]==3 or map[int((ypos)/50)][int((xpos-offset-10)/50)]==3 ) and direction == LEFT:
        xpos+=3
       
    #right collision needed here
    if (map[int((ypos+frameHeight-10)/50)][int((xpos-offset+frameWidth+5)/50)]==1 or map[int((ypos)/50)][int((xpos-offset+frameWidth+5)/50)]==1 or map[int((ypos+frameHeight-10)/50)][int((xpos-offset+frameWidth+5)/50)]==2 or map[int((ypos)/50)][int((xpos-offset+frameWidth+5)/50)]==2 or map[int((ypos+frameHeight-10)/50)][int((xpos-offset+frameWidth+5)/50)]==3 or map[int((ypos)/50)][int((xpos-offset+frameWidth+5)/50)]==3) and direction == RIGHT:
        xpos-=3    
    #stop moving if you hit edge of screen (will be removed for scrolling)
    if xpos+frameWidth > 1700:
        xpos-=3
    if xpos<0:
        xpos+=3

   
    #stop falling if on bottom of game screen
    if ypos > 800-frameHeight:
        isOnGround = True
        vy = 0
        ypos = 800-frameHeight
   
    #gravity
    if isOnGround == False:
        vy+=.2 #notice this grows over time, aka ACCELERATION









    #COLLISION2
   
    #collision with feetsies
    if map[int((ypos2+frameHeight2)/50)][int((xpos2-offset2+frameWidth2/2)/50)]==1 or map[int((ypos2+frameHeight2)/50)][int((xpos2-offset2+frameWidth2/2)/50)]==2 or map[int((ypos2+frameHeight2)/50)][int((xpos2-offset2+frameWidth2/3)/50)]==3:
        isOnGround2 = True
        vy2=0
       
    else:
        isOnGround2 = False
       
    #bump your head, ouch!
    if map[int((ypos2)/50)][int((xpos2-offset2+frameWidth2/2)/50)]==1 or map[int((ypos2)/50)][int((xpos2-offset2+frameWidth2/2)/50)]==2 or map[int((ypos2)/50)][int((xpos2-offset2+frameWidth2/3)/50)]==3:
        vy2=0
       
    #left collision (it's extra long because we check both head and feets(well, knees) for left collision
    if (map[int((ypos2+frameHeight2-10)/50)][int((xpos2-offset2-10)/50)]==1 or map[int((ypos2)/50)][int((xpos2-offset2-10)/50)]==1 or map[int((ypos2+frameHeight2-10)/50)][int((xpos2-offset2-10)/50)]==2 or map[int((ypos2)/50)][int((xpos2-offset2-10)/50)]==2 or map[int((ypos2+frameHeight2-10)/50)][int((xpos2-offset2-10)/50)]==3 or map[int((ypos2)/50)][int((xpos2-offset2-10)/50)]==3 ) and direction2 == LEFT:
        xpos2+=3
       
    #right collision needed here
    if (map[int((ypos2+frameHeight2-10)/50)][int((xpos2+frameWidth2+5)/50)]==1 or map[int((ypos2)/50)][int((xpos2+frameWidth2+5)/50)]==1 or map[int((ypos2+frameHeight2-10)/50)][int((xpos2+frameWidth2+5)/50)]==2 or map[int((ypos2)/50)][int((xpos2+frameWidth2+5)/50)]==2 or map[int((ypos2+frameHeight2-10)/50)][int((xpos2+frameWidth2+5)/50)]==3 or map[int((ypos2)/50)][int((xpos2+frameWidth2+5)/50)]==3) and direction2 == RIGHT:
        xpos2-=3    
    #stop moving if you hit edge of screen (will be removed for scrolling)
    if xpos2+frameWidth2 > 1700:
        xpos2-=3
    if xpos2<0:
        xpos2+=3

   
    #stop falling if on bottom of game screen
    if ypos2 > 800-frameHeight2:
        isOnGround2 = True
        vy2 = 0
        ypos2 = 800-frameHeight2
   
    #gravity
    if isOnGround2 == False:
        vy2+=.2 #notice this grows over time, aka ACCELERATION
   

       
    #ANIMATION-------------------------------------------------------------------
       
    # Update Animation Information

    if moving == True: #animate when moving
        ticker+=1
        if ticker%10==0: #only change frames every 10 ticks
          frameNum+=1
        if frameNum>7:
           frameNum = 0

    if moving2 == True: #animate when moving
        ticker2+=1
        if ticker2%10==0: #only change frames every 10 ticks
          frameNum2+=1
        if frameNum2>7:
           frameNum2 = 0
 
    # RENDER--------------------------------------------------------------------------------
    # Once we've figured out what frame we're on and where we are, time to render.
           
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
   
    #draw map
    for i in range (16):
        for j in range(66):
            if map[i][j]==1:
                screen.blit(dirt, (j*50+offset, i*50), (0, 0, 50, 50))
            if map[i][j]==2:
                screen.blit(brick, (j*50+offset, i*50), (0, 0, 50, 50))
            if map[i][j]==3:
                screen.blit(wood, (j*50+offset, i*50), (0, 0, 50, 50))
       
    print(offset)
    screen.blit(Link, (xpos, ypos), (frameWidth*frameNum, RowNum*frameHeight, frameWidth, frameHeight))
    screen.blit(Cat, (xpos2, ypos2), (frameWidth2*frameNum2, RowNum2*frameHeight2, frameWidth2, frameHeight2))
    pygame.display.flip()#this actually puts the pixel on the screen
   
#end game loop------------------------------------------------------------------------------
pygame.quit()
