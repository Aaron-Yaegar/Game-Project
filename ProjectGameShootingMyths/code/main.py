from settings import *
from player import Player
from sprite import *
from random import randint

class Game:
    def __init__(self):
        #Setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Alagad: Conquest of Philippines Mythical Creatures")
        self.clock = pygame.time.Clock()
        self.running = True
    
        # #Groups Sprite
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        # #Player Sprite
        self.player = Player ((400,300), self.all_sprites, self.collision_sprites)
        for i in range(6):
            x, y = randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)
            w, h = randint(60,100), randint(50,100)
            CollisionSprite((x,y), (w,h), (self.all_sprites, self.collision_sprites))

    def run(self):
        while self.running:
            #Delta Timer
            dt = self.clock.tick() / 1000  # seconds passed since last frame

            #Event Loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            #Update
            self.all_sprites.update(dt)
            
            # Draw: clear screen then draw all sprites
            self.display_surface.fill('black')
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run() 
