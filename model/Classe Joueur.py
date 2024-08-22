from model.player import Player
from model.weapon import Weapon       

knife = Weapon("Couteau", 3)

player1 = Player('Badboyriri',20, 3)
player2 = Player('Badgirlroro',20, 5)

player1.attack_player(player2)
print(player1.get_pseudo(), "attaque", player2.get_pseudo())
print("Bienvenue au joueur", player1.get_pseudo(), "Point de vie", player1.get_health(), "Attaque", player1.get_attack_value())
print("Bienvenue au joueur", player2.get_pseudo(), "Point de vie", player2.get_health(), "Attaque", player2.get_attack_value())
