import pygame
import time


class Sword (pygame.sprite.Sprite) :
# créer la classe qui représente l'épée
# sprite permet de lui crée une enveloppe dans le jeu
    
    
    def __init__ (self, game, player) :
        super().__init__()
        self.game = game
        self.player = player
        self.image = pygame.image.load(r'assets\sword.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 561
        self.movespeed = 1
        self.dps = 75
        self.cool_down_count = 0

    
    def cooldown (self) :
        if self.cool_down_count >= self.dps :
            self.cool_down_count = 0
        elif self.cool_down_count > 0:
            self.cool_down_count += 1
            
    def cooldown2 (self) :
        self.cooldown()
    

    def move (self) :
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters) :
            if self.cool_down_count == 0 :
                monster.get_damage (self.player.damage)
                self.cool_down_count = 1
        for boss in self.player.game.check_collision(self, self.player.game.all_boss) :
            if self.cool_down_count == 0 :
                boss.get_damage (self.player.damage)
                self.cool_down_count = 1


    def move_right (self) :
    # fonctions pour aller vers la droite    
        if not self.player.game.check_collision (self.player, self.player.game.all_monsters) :
        # si [(self, self.game.all_monsters)=(joueur, tout les monstre)] n'entre
        # pas en collision alors c'est bon
            if not self.player.game.check_collision (self.player, self.player.game.all_boss) :
                self.rect.x += self.movespeed
                # code pour aller à droite (rajout de self.movespeed)


    def move_left (self) :
    # fonctions pour aller vers la gauche
        self.rect.x -= self.movespeed
        # code pour aller à gauche (retrait de self.movespeed)