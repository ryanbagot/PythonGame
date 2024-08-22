from game import Game
import math
from projectile import Projectile
import pygame

pygame.init()

#génrer la fenêtre 
pygame.display.set_caption("Comet Fall")
screen = pygame.display.set_mode((1080,720))

#importer image pour background
background = pygame.image.load("bg.jpg") 

#importer la bannière 
banner = pygame.image.load('banner.png')
banner = pygame.transform.scale(banner, (500,500))
banner_rect = banner.get_rect()
banner_rect.centerx = screen.get_width() // 2
banner_rect.centery = screen.get_height() // 2
banner_rect.x = math.ceil((screen.get_width()/4)+2)

#importer le bouton play
play_button = pygame.image.load('button.png')
play_button = pygame.transform.scale(play_button, (400,150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil((screen.get_width()/3.33)+2)
play_button_rect.y = math.ceil(screen.get_height()/1.5133)

#charger jeu
game = Game()

running = True

#boucle tant que la condition est vraie
while running: 
    
    #appliquer l'arriere plan
    screen.blit(background, (0, -200))
    
    #vérifier si le jeu a commencé 
    if game.is_playing:
        #déclencher les instructions de la partie
        game.update(screen)
    #vérifier si le jeu n'a pas commencé 
    else: 
        #ajouter un ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)
        
    
    #position joueur    
    print(game.player.rect.x)
            
    #mettre à jour l'ecran
    pygame.display.flip()
    
    #si le joueur ferme la fenêtre
    for event in pygame.event.get(): 
        #l'évènement fermeture de fenêtre
        if event.type == pygame.QUIT: 
            running = False
            pygame.quit()
            print('fermeture du jeu')
        #detecter su un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN: 
            game.pressed[event.key] = True
            
            #detecter si la touche espace est enclenchée pour lancer un projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
                
        elif event.type == pygame.KEYUP: 
            game.pressed[event.key] = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            #vérifier si la souris est en collision avec le bouton jouer 
            if play_button_rect.collidepoint(event.pos): 
                #mettre le jeu en mode lancé
                game.start()
            