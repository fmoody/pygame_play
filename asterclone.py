import sys,pygame

class asterclone:

    size = width, height = 800, 600
    flags = 0

    clock = pygame.time.Clock()

    aob = 0
    
    def startup(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode(self.size,self.flags)
        self.screenrect = self.screen.get_rect()
    
        self.shuttle = pygame.image.load("shuttle.png").convert_alpha()
    
    def event_loop(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_q or event.key == pygame.K_ESCAPE: sys.exit()

            self.screen.fill([0,0,0])
            angled_shuttle = pygame.transform.rotate(self.shuttle,self.aob)
            angled_shuttlerect = angled_shuttle.get_rect()
            angled_shuttlerect.center = self.screenrect.center
            self.screen.blit(angled_shuttle,angled_shuttlerect)
            
            pygame.display.flip()
            
            self.aob = (self.aob+1)%360
            
            self.clock.tick(60)


my_game = asterclone()
my_game.startup()
my_game.event_loop()



