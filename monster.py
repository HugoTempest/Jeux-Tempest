import pygame
import random
import pyautogui
from player import Player


class Monster (pygame.sprite.Sprite) :
# créer la classe qui représente le monstre


    def __init__ (self, game) :
        super().__init__()
        self.game = game
        self.player = Player(self)
        self.health = 100
        self.max_health = 100
        self.health_bar_length = 100
        self.health_ratio = self.max_health / self.health_bar_length
        self.lvl = random.randrange(1, 10)
        self.damage = 30
        self.image = pygame.image.load(r'assets\monstresquelette.png')
        self.rect = self.image.get_rect()
        self.size_screen = pyautogui.size()
        if self.size_screen == (1920, 1080) :
            self.rect.x = 1900
            self.rect.y = 760
        else :
            self.rect.x = 1200
            self.rect.y = 490
        self.movespeed = 0.5
        self.gainexp = 10
        self.gainegold = 5
        self.lvlprb = 1
        self.cool_down_count = 0
        while self.lvl >= self.lvlprb :
            self.lvlprb += 1
    

    def get_damage (self, amount) :
        self.health -= amount
        if self.health <= 0 :
            self.lvl = random.randrange(1, 10)
            print(self.lvlprb)
            self.lvlprb = 1
            self.damage = 30
            self.gainexp = 10
            self.max_health = 100
            self.gainegold = 5
            while self.lvl >= self.lvlprb :
                self.max_health = round(self.max_health * 1.12)
                self.gainexp = round(self.gainexp * 1.12)
                self.damage = round(self.damage * 1.06)
                self.gainegold = round(self.gainegold * 1.12)
                self.movespeed = random.randrange(1, 4)
                self.lvlprb += 1
            self.game.add_xp(self.gainexp)
            self.game.add_health(20)
            self.game.add_gold(self.gainegold)
            self.game.add_boss()
            if self.game.size_jeux_1g == True :
                self.rect.x = 1900
            else :
                self.rect.x = 1300
            self.health = self.max_health
            self.health_bar_length = 100
            self.health_ratio = self.max_health / self.health_bar_length
            #print("Lvl : ", self.lvl,"/ Max Health : ", self.max_health,"/ Speed : ", self.movespeed,"/ Damage : ", self.damage, "/ Xp : ", self.gainexp, "/ Gold : ", self.gainegold)
  

    def update_health_bar (self, surface) :
        pygame.draw.rect(surface, (23, 22, 22), (self.rect.x - 4, self.rect.y - 30, self.health_bar_length, 25))
        pygame.draw.rect(surface, (255, 0, 0), (self.rect.x - 4, self.rect.y - 30, self.health/self.health_ratio,25))
        pygame.draw.rect(surface, (23, 22, 22), (self.rect.x - 4, self.rect.y - 30, self.health_bar_length, 25), 4)
        # dessiner la bar de vie et le fond de la bar de vie
    

    def cooldown (self) :
        if self.cool_down_count >= 100:
            self.cool_down_count = 0
        elif self.cool_down_count > 0:
            self.cool_down_count += 1


    def forward (self) :
        self.cooldown()       
        if not self.game.check_collision (self, self.game.all_players) :
            self.rect.x -= self.movespeed
        else :
            if self.cool_down_count == 0 :          
                self.game.player.get_damage(self.damage)
                self.cool_down_count = 1