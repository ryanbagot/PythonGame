import pygame

#definir la classe projectile du joueur
class Projectile(pygame.sprite.Sprite): 
    
    #definit le constructeur de la classe 
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0
        
    def rotate(self):
        #tourner le projectile
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
        
    def remove(self):
        self.player.all_projectiles.remove(self)
    
    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        
        #verifier si le projectile est en collision avec un monstre 
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            #infliger les dégats  
            monster.damage(self.player.attack)
        
        #verifier si le projectile n'est plus sur l'écran
        if self.rect.x > 1080:
            #supprimer le projectile en dehors de l'ecran
            self.remove()
            print('projectile supprimé')