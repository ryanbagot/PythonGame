import pygame
from player import Player
from monster import Monster

#creation class jeu 
class Game: 
    
    def __init__(self): 
        #si notre jeu commence ou non
        self.is_playing = False
        #générer joueur 
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        
        
    def start (self):
        self.is_playing= True 
        self.spwan_monster()
        self.spwan_monster()
    
    def game_over(self): 
        #remettre le jeu à neuf (retirer les monstres et remettre le joueur à 100 de vie et le jeu en attente)
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.health_max
        self.is_playing= False  
     
    def update(self, screen): 
        #appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)
    
        #actualiser la barre de vie
        self.player.update_health_bar(screen)
    
        #récupérer les projectiles du joueur 
        for projectile in self.player.all_projectiles:
          projectile.move()
          
         #récupérer les monstres
        for monster in self.all_monsters: 
            monster.forward() 
            monster.update_health_bar(screen)
    
         #appliquer l'ensemble des images du groupe de projectiles
        self.player.all_projectiles.draw(screen)
    
        #appliquer l'ensemble des images du groupe de monster
        self.all_monsters.draw(screen)
    
        #verifier si le joueur souhaite aller à gauche ou à droite 
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x>0:
            self.player.move_left()
        
    def check_collision(self, sprite, group): 
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)    
        
    def spwan_monster(self): 
        monster = Monster(self)
        self.all_monsters.add(monster)
 