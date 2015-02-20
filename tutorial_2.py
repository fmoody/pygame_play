import sys, pygame

# Basic idea, code snippits, and ball.gif borrowed from http://www.pygame.org/docs/tut/intro/intro.html
# and other pygame tutorials from http://www.pygame.org/docs/

pygame.init()

#size = width, height = 1680, 1050
size = width, height = 640, 480
flags = 0

screen = pygame.display.set_mode(size,flags)
screenrect = screen.get_rect()

black = 0, 0, 0

ball = pygame.transform.scale(pygame.image.load("ball.gif").convert_alpha(),[10,10])
ballspeed = [2, 1]

balls = [] # Balls is a list of ball rects and directions

paused = True

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_f:
                # Speed up the balls
                ballspeed[0] = ballspeed[0]*2
                ballspeed[1] = ballspeed[1]*2
            elif event.key == pygame.K_s:
                # Slow down the balls
                ballspeed[0] = ballspeed[0]*0.5
                ballspeed[1] = ballspeed[1]*0.5
            elif event.key == pygame.K_p:
                paused = not paused
            elif event.key == pygame.K_a:
                # Add a ball
                balls.append([ball.get_rect(), [1,1]])
            elif event.key == pygame.K_d:
                # Delete a ball
                if len(balls) > 0:
                    balls.pop()
            elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                sys.exit()
                
    # Move balls
    if not paused:
        for current_ball in balls:
            current_balldirection = current_ball[1]
            newrect = current_ball[0].move([current_ball[1][0]*ballspeed[0], current_ball[1][1]*ballspeed[1]] )

            # Check Wall collisions
            if screenrect.contains(newrect):
                current_ball[0] = newrect
            else:
                if newrect.top < screenrect.top or newrect.bottom > screenrect.bottom:
                    current_balldirection[1] = -current_balldirection[1]
                if newrect.left < screenrect.left or newrect.right > screenrect.right:
                    current_balldirection[0] = -current_balldirection[0]

    # Draw to surface
    screen.fill(black)
    for current_ball in balls:
        screen.blit(ball, current_ball[0])
    pygame.display.flip()
    pygame.time.wait(1)
        
