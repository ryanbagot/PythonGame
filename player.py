import pygame
from projectile import Projectile

#creation joueur
class Player(pygame.sprite.Sprite): 
    
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 100
        self.health_max = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("player.png") 
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
        
    def damage(self, amount): 
        if self.health - amount > amount : 
            self.health -= amount
        else: 
            #si le joueur n'a plus de points de vie
            self.game.game_over()
            
        
    def update_health_bar(self, surface): 
        #dessiner la bar de vie 
        pygame.draw.rect(surface, (60, 63,60), [self.rect.x + 50, self.rect.y + 20, self.health_max, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 5])
        
    def launch_projectile(self):
        #créer une nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectile(self))
        
    def move_right(self):
        #si le joueur n'est pas en collision il peut avancer 
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity
    
    def move_left(self):
        self.rect.x -= self.velocity

 