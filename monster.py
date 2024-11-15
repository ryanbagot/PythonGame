import pygame
import random

#créer une classe monstre 
class Monster(pygame.sprite.Sprite): 
    
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.03
        self.image= pygame.image.load('mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0,300)
        self.rect.y = 540
        self.velocity = random.uniform(0.1,0.8)
        
    def damage(self, amount):
        #infliger les dégats
        self.health -= amount
        
        #vérifier si le nouveau nombre de points de vies du monstre 
        if self.health <= 0: 
            #reaparaaitre un monstre 
            self.rect.x = 1000 + random.randint(0,300)
            self.velocity = random.randint(1,3)
            self.health = self.max_health
            
    def update_health_bar(self, surface): 
        #dessiner la bar de vie 
        pygame.draw.rect(surface, (60, 63,60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])
        
    def forward(self):
        #si il n'ya pas de collision il peut avancer 
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        #si le joueur est en collision avec le monstre
        else: 
            #infliger les dégats (au joueur)
            self.game.player.damage(self.attack)
            