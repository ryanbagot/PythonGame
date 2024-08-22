#créer la classe Player 
class Player:
    #caractéristique joueur indiqué dans les () de la classe, on peut créer une fonction avec les caractéristiques 
    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None
#fonctions de la class pour les caractéristiques
    def get_pseudo(self):
        return self.pseudo
    def get_health(self):
        return self.health
    def get_attack_value(self):
        return self.attack
    def damage(self, damage):
        self.health = self.health - damage
    def attack_player(self, target_player): 
        target_player.damage(self.attack)

#si le joueur a une arme 
        if self.has_weapon():
            #ajoute les dégats de l'arme au point d'attaque du joueur 
            damage = damage + self.weapon.get_damage_amount()
        
        target_player.damage(damage)

#méthode pour changer l'arme du joueur 
    def set_weapon(self, weapon):
        self.weapon = weapon

#méthode pour savoir si le joueur a une arme 
    def has_weapon(self):
        return self.weapon is not None 
    
            
#Créer la classe Warrior 
class Warrior(Player):
    #caractéristique joueur indiqué dans les () de la classe, on peut créer une fonction avec les caractéristiques 
    def __init__(self, pseudo, health, attack):
        super().__init__(pseudo, health, attack)
        self.armor = 3
    def damage(self, damage):
        if self.armor > 0:
            self.armor = self.armor - 1
            damage = 0 
            super().damage(damage)
    def attack_player(self, target_player): 
        target_player.damage(self.attack)
    def blade(self): 
        self.armor = 3
        print("l'armure est rechargé")
    def get_armor_point(self): 
        return self.armor
    
warrior = Warrior("DarkWarrior", 30, 4)
print("Bienvenue au guerrier", warrior.get_pseudo(), "Point de vie:", warrior.get_health(), "Point d'attaque:", warrior.get_attack_value(), "Point d'armure:", warrior.get_armor_point())
warrior.damage(4)
print("Vie:", warrior.get_health(), "armure:", warrior.get_armor_point())

