import pygame
import pyautogui
from player import Player


class Boss (pygame.sprite.Sprite) :
    
    
    def __init__ (self, game) :
        super().__init__()
        self.game = game
        self.player = Player(self)
        self.health = 1000
        self.max_health = 1000
        self.lvl = 1
        self.lvlprb = 1
        self.damage = 100
        self.movespeed = 0.2
        self.image = pygame.image.load(r'assets\bosssquelette.png')
        self.rect = self.image.get_rect()
        self.size_screen = pyautogui.size()
        if self.size_screen == (1920, 1080) :
            self.rect.x = 1950
            self.rect.y = 643
        else :
            self.rect.x = 1250
            self.rect.y = 373
        self.cool_down_count = 0
        self.health_bar_length = 200
        self.health_ratio = self.max_health / self.health_bar_length
        self.gainexp = 50
        self.gainegold = 25
    
    
    def update_health_bar (self, surface) :
        pygame.draw.rect(surface, (23, 22, 22), (self.rect.x - 8, self.rect.y - 50, self.health_bar_length, 35))
        pygame.draw.rect(surface, (255, 0, 0), (self.rect.x - 8, self.rect.y - 50, self.health/self.health_ratio,35))
        pygame.draw.rect(surface, (23, 22, 22), (self.rect.x - 8, self.rect.y - 50, self.health_bar_length, 35), 4)


    def get_damage (self, amount) :
        self.health -= amount
        if self.health <= 0 :
            self.game.erase_boss()

        
    def cooldown (self) :
        if self.cool_down_count >= 100 :
            self.cool_down_count = 0
        elif self.cool_down_count > 0 :
            self.cool_down_count += 1
        
        
    def forward (self) :
        self.cooldown()  
        if not self.game.check_collision (self, self.game.all_players) :
            self.rect.x -= self.movespeed
        else :
            if self.cool_down_count == 0 :
                self.game.player.get_damage(self.damage)
                self.cool_down_count = 1