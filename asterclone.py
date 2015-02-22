import sys,math,pygame

class Ship:
    def __init__(self, position):
        self.x=position[0]
        self.y=position[1]
        self.dx = 0
        self.dy = 0
        self.direction = 90
        self.acceleration = 1
        self.turn_speed = 5
        self.ship_image = pygame.transform.rotate(pygame.image.load("shuttle.png").convert_alpha(),270)

    def draw(self,surface):
        self.x += self.dx
        self.y += self.dy
        if self.x > 800: self.x = 0
        elif self.x < 0: self.x = 800
        if self.y > 600: self.y = 0
        elif self.y < 0: self.y = 600
        angled_shuttle = pygame.transform.rotate(self.ship_image,self.direction)
        angled_shuttlerect = angled_shuttle.get_rect()
        angled_shuttlerect.x = self.x
        angled_shuttlerect.y = self.y
        surface.blit(angled_shuttle,angled_shuttlerect)

    def rotate_right(self):
        self.direction = (self.direction-self.turn_speed)%360

    def rotate_left(self):
        self.direction = (self.direction+self.turn_speed)%360

    def accelerate(self):
        self.dx += self.acceleration*math.cos(math.radians(self.direction))
        self.dy += -1*self.acceleration*math.sin(math.radians(self.direction))
        
class asterclone:

    def startup(self):
        pygame.init()
        
        self.size = 800, 600
        self.flags = 0

        self.screen = pygame.display.set_mode(self.size,self.flags)
        self.screenrect = self.screen.get_rect()

        self.player_ship = Ship(self.screenrect.center)

        self.clock = pygame.time.Clock()
        
        pygame.key.set_repeat(50,50)
    
    def event_loop(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_q or event.key == pygame.K_ESCAPE: sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.player_ship.rotate_right()
                    elif event.key == pygame.K_LEFT:
                        self.player_ship.rotate_left()
                    elif event.key == pygame.K_UP:
                        self.player_ship.accelerate()
                    # elif event.key == pygame.K_DOWN:
                        # We don't have a special ability yet.
                        
            self.screen.fill([0,0,0])

            self.player_ship.draw(self.screen)
            
            pygame.display.flip()
            
            self.clock.tick(60)


my_game = asterclone()
my_game.startup()
my_game.event_loop()



