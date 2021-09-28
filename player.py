import pygame


class Player (pygame.sprite.Sprite) :
# créer la classe qui représente le joueur
# sprite permet de lui crée une enveloppe dans le jeu

    
    def __init__ (self, game) :
        super().__init__()
        self.game = game
        self.pseudo = ''
        self.rpseudo = False
        self.health = 500
        self.health2 = 500
        self.max_health = 500
        self.health_bar_length = 200
        self.health_ratio = self.max_health / self.health_bar_length
        self.health_bar_length2 = 200
        self.health_ratio2 = self.max_health / self.health_bar_length2
        self.lvl = 1
        self.xp = 0
        self.next_level = 25
        self.xp_bar_length = 200
        self.xp_ratio = self.next_level / self.xp_bar_length
        self.points = 20
        self.damage = 20
        self.movespeed = 1
        self.prot = 0
        self.prot2 = 100 - self.prot
        self.dps = 1
        self.image = pygame.image.load(r'assets\playernocheald.png')
        # permet de chercher l'image de votre joueur
        self.rect = self.image.get_rect()
        # permet de lui donné une hitbox
        self.rect.x = 100
        self.rect.y = 561
        # permet d'ajuster l'emplacement du personnage au début du jeu
        self.gold = 0
        self.cooldown_health = 200
    

    def update_health_bar (self, surface) :

        pygame.draw.rect(surface, (23, 22, 22), (10, 10, self.health_bar_length, 25))
        pygame.draw.rect(surface, (255, 0, 0), (10, 10, self.health/self.health_ratio, 25))
        pygame.draw.rect(surface, (23, 22, 22), (10, 10, self.health_bar_length, 25), 4)
        # dessiner la bar de vie et le fond de la bar de vie
        
    def update_health_bar_inv (self, surface) :
    
        pygame.draw.rect(surface, (43, 43, 43), (10, 10, self.health_bar_length, 25))
        pygame.draw.rect(surface, (255, 0, 0), (10, 10, self.health/self.health_ratio, 25))
        pygame.draw.rect(surface, (43, 43, 43), (10, 10, self.health_bar_length, 25), 4)
    

    def update_xp_bar (self, surface) :

        pygame.draw.rect(surface, (23, 22, 22), (10, 30, self.xp_bar_length, 25))
        pygame.draw.rect(surface, (255, 239, 0), (10, 30, self.xp/self.xp_ratio, 25))
        pygame.draw.rect(surface, (23, 22, 22), (10, 30, self.xp_bar_length, 25), 4)
        
    def update_xp_bar_inv (self, surface) :
    
        pygame.draw.rect(surface, (43, 43, 43), (10, 30, self.xp_bar_length, 25))
        pygame.draw.rect(surface, (255, 239, 0), (10, 30, self.xp/self.xp_ratio, 25))
        pygame.draw.rect(surface, (43, 43, 43), (10, 30, self.xp_bar_length, 25), 4)


    def get_damage (self, amount) :
        if self.health != 0 :
            self.prot2 = 100 - self.prot
            amount1 = amount * self.prot2
            amount2 = round(amount1 / 100)
            print(amount2)
            self.health -= amount2
            while self.health2 > self.health :
                if self.cooldown_health == 0 :
                    self.health2 -= 1
                    self.cooldown_health = 200
                    if self.health2 < self.health :
                        self.health2 = self.health
                if self.cooldown_health > 0 :
                    self.cooldown_health -= 1
            if self.health < 0 :
                self.health = 0
        if self.health == 0 :
            self.game.game_over()
    

    def move_right (self) :
    # fonctions pour aller vers la droite    
        if not self.game.check_collision (self, self.game.all_monsters) :
        # si [(self, self.game.all_monsters)=(joueur, tout les monstre)] n'entre
        # pas en collision alors c'est bon
            if not self.game.check_collision (self, self.game.all_boss) :
                self.rect.x += self.movespeed
                # code pour aller à droite (rajout de self.movespeed)


    def move_left (self) :
    # fonctions pour aller vers la gauche
        self.rect.x -= self.movespeed
        # code pour aller à gauche (retrait de self.movespeed)