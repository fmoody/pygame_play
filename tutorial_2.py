import sys, pygame

# Basic idea, code snippits, and ball.gif borrowed from http://www.pygame.org/docs/tut/intro/intro.html
# and other pygame tutorials from http://www.pygame.org/docs/

pygame.init()

size = width, height = 1680, 1050
#size = width, height = 640, 640
flags = 0

screen = pygame.display.set_mode(size,flags)
screenrect = screen.get_rect()

black = 0, 0, 0

ball = pygame.transform.scale(pygame.image.load("ball.gif").convert_alpha(),[50,50])
ballspeed = [1, 1]
ballspeed_multiplier = 1

balls = [] # Balls is a list of ball rects and directions

paused = True

clock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_f:
                # Speed up the balls
                ballspeed_multiplier *= 2
            elif event.key == pygame.K_s:
                # Slow down the balls
                ballspeed_multiplier *= 0.5
            elif event.key == pygame.K_p:
                paused = not paused
                print("Paused: " + str(paused))
            elif event.key == pygame.K_a:
                # Add a ball
                balls.append([ball.get_rect(), ballspeed.copy()])
            elif event.key == pygame.K_d:
                # Delete a ball
                if len(balls) > 0:
                    balls.pop()
            elif event.key == pygame.K_e:
                # Delete all balls
                balls = []
            elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                sys.exit()
                
    # Move balls
    if not paused:

        original_ball_info = balls.copy()

        for index,current_ball in enumerate(balls):
#            print("Index: " + str(index))
            current_ballspeed = current_ball[1]
            newrect = current_ball[0].move([current_ball[1][0]*ballspeed_multiplier, current_ball[1][1]*ballspeed_multiplier] )

            # Check ball collisions (need to optimize this later)
            remaining_balls_rects = [this_ball[0] for this_ball in original_ball_info]
            collision_list = newrect.collidelistall(remaining_balls_rects)
            if len(collision_list) > 1 :
                collision_value  = [0,0]
                for collision in collision_list:
                    collision_value[0] += original_ball_info[collision][1][0]
                    collision_value[1] += original_ball_info[collision][1][1]

                current_ballspeed[0] = collision_value[0] / len(collision_list)
                current_ballspeed[1] = collision_value[1] / len(collision_list)
            elif screenrect.contains(newrect):             # Check Wall collisions. Update the ball if no collision.
                current_ball[0] = newrect
            else: # Swap the sign of the x/y depending on the wall collided with.
                if newrect.top < screenrect.top or newrect.bottom > screenrect.bottom:
                    current_ballspeed[1] = -current_ballspeed[1]
                if newrect.left < screenrect.left or newrect.right > screenrect.right:
                    current_ballspeed[0] = -current_ballspeed[0]

    # Draw to surface
    screen.fill(black)
    for current_ball in balls:
        screen.blit(ball, current_ball[0])
    pygame.display.flip()
    #pygame.time.wait(10)
    clock.tick(60)
        
