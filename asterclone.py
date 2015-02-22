import sys,pygame

class asterclone:

    size = width, height = 800, 600
    flags = 0

    clock = pygame.time.Clock()

    direction = 0

    turn_speed = 5
    
    def startup(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode(self.size,self.flags)
        self.screenrect = self.screen.get_rect()
    
        self.shuttle = pygame.image.load("shuttle.png").convert_alpha()
        pygame.key.set_repeat(100,100)
    
    def event_loop(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_q or event.key == pygame.K_ESCAPE: sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.direction = (self.direction-self.turn_speed)%360
                    elif event.key == pygame.K_LEFT:
                        self.direction = (self.direction+self.turn_speed)%360
                        
            self.screen.fill([0,0,0])
            angled_shuttle = pygame.transform.rotate(self.shuttle,self.direction)
            angled_shuttlerect = angled_shuttle.get_rect()
            angled_shuttlerect.center = self.screenrect.center
            self.screen.blit(angled_shuttle,angled_shuttlerect)
            
            pygame.display.flip()
            
            self.clock.tick(60)


my_game = asterclone()
my_game.startup()
my_game.event_loop()



