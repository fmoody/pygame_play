import sys, pygame

# Basic idea, code snippits, and ball.gif borrowed from http://www.pygame.org/docs/tut/intro/intro.html
# and other pygame tutorials from http://www.pygame.org/docs/

pygame.init()

size = width, height = 1680, 1050
flags = 0

screen = pygame.display.set_mode(size,flags)
screenrect = screen.get_rect()

black = 0, 0, 0

ball = pygame.image.load("ball.gif").convert_alpha()
ballrect = ball.get_rect()
ballspeed = [1, 1]

paused = True

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_f:
                ballspeed[0] = ballspeed[0]*2
                ballspeed[1] = ballspeed[1]*2
            elif event.key == pygame.K_s:
                ballspeed[0] = ballspeed[0]*0.5
                ballspeed[1] = ballspeed[1]*0.5
            elif event.key == pygame.K_p:
                paused = not paused
            elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                sys.exit()
                
    # Move ball
    if not paused:
        newrect = ballrect.move(ballspeed)
        if screenrect.contains(newrect):
            ballrect = newrect
        else:
            if newrect.top < screenrect.top or newrect.bottom > screenrect.bottom:
                ballspeed[1] = -ballspeed[1]
            if newrect.left < screenrect.left or newrect.right > screenrect.right:
                ballspeed[0] = -ballspeed[0]

    # Draw to surface
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    pygame.time.wait(1)
        
