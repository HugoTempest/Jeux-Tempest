import pygame
import random
from player import Player
from sword import Sword
from monster import Monster
from boss import Boss


class Game () :
    # créer la classe qui représente le jeu


    def __init__ (self) :
        self.is_playing = False
        # définir si le jeu a commencé ou non
        self.all_players = pygame.sprite.Group()
        # créer un groupe de joueur pour gérer les collisions
        self.player = Player(self)
        # génerer le joueur
        self.monster = Monster(self)
        self.boss = Boss(self)
        self.all_players.add(self.player)
        # ajouter self.player (le joueur) dans le groupe all_players
        self.all_monsters = pygame.sprite.Group()
        # créer un groupe de monstre
        self.all_boss = pygame.sprite.Group()
        self.pressed = {}
        # permet de laissé enfoncé la touche
        self.sword = Sword(self, self.player)
        # génerer l'épée
        self.font = pygame.font.Font('assets\Staatliches-Regular.ttf', 25)
        self.font2 = pygame.font.Font('assets\Staatliches-Regular.ttf', 30)
        self.health_text = self.font.render(f"Damage : {self.player.damage}", 1, (255, 255, 255))
        self.xp_text = self.font.render(f"Level : {self.player.lvl}", 1, (255, 255, 255))
        self.movespeed_text = self.font.render(f"Move Speed : {self.player.movespeed}", 1, (255, 255, 255))
        self.prot_text = self.font.render(f"Resistance : {self.player.prot}", 1, (255, 255, 255))
        self.dps_text = self.font.render(f"Dps : {self.player.dps}", 1, (255, 255, 255))
        self.point_text = self.font.render(f"Points : {self.player.points}", 1, (255, 255, 255))
        self.gold_text = self.font.render(f"Gold : {self.player.gold}", 1, (255, 255, 255))
        # affiche stats
        self.health2_text = self.font2.render("+", 1, (255, 255, 255))
        self.movespeed2_text = self.font2.render("+", 1, (255, 255, 255))
        self.prot2_text = self.font2.render("+", 1, (255, 255, 255))
        self.dps2_text = self.font2.render("+", 1, (255, 255, 255))
        # affiche ajouts a stats
        self.ar = pygame.image.load(r'assets\+.png')
        self.health2_text_rect = self.ar.get_rect()
        self.health2_text_rect.x = 194
        self.health2_text_rect.y = 88
        self.movespeed2_text_rect = self.ar.get_rect()
        self.movespeed2_text_rect.x = 194
        self.movespeed2_text_rect.y = 118
        self.dps2_text_rect = self.ar.get_rect()
        self.dps2_text_rect.x = 194
        self.dps2_text_rect.y = 139
        self.prot2_text_rect = self.ar.get_rect()
        self.prot2_text_rect.x = 194
        self.prot2_text_rect.y = 178
        # affiche + stats
        self.pauseimg = pygame.image.load(r'assets\pause.png')
        self.pauseimg_rect = self.pauseimg.get_rect()
        self.pauseimg_rect2 = pygame.transform.scale(self.pauseimg, (0, 0))
        self.pausing = False
        self.font3 = pygame.font.Font('assets\Staatliches-Regular.ttf', 50)
        self.continu_e_text = self.font3.render(f"CONTINUE", 1, (255, 255, 255))
        self.continu_e_text_rect = self.continu_e_text.get_rect()
        self.continu_e_text2 = self.font3.render(f"  CONTINUE  ", 1, (255, 255, 255))
        self.continu_e_text_rect2 = self.continu_e_text2.get_rect()
        # continue et pause images
        self.inventair = False
        self.invoc_boss = 0
        self.boss_appeard = False
        self.size_jeux_1g = False
        
    
    def start (self) :
        self.is_playing = True
        if self.size_jeux_1g == True :
            self.player.rect.x = 100
            self.player.rect.y = 832
            self.sword.rect.x = 115
            self.sword.rect.y = 832
            self.spawn_monster()
        else :
            self.player.rect.x = 100
            self.player.rect.y = 561
            self.sword.rect.x = 115
            self.sword.rect.y = 561
            self.spawn_monster()
        # permet de lancé le code spawn_monster au début du jeu


    def add_xp (self, xps) :
        self.player.xp += xps
    

    def add_health (self, points) :
        self.player.health += points
        self.player.health = self.player.max_health
        
    
    def add_gold (self, gold) :
        self.player.gold += gold
    
    
    def add_boss (self) :
        self.invoc_boss += 1
        if self.invoc_boss >= 5 :
            self.invoc_boss = 0
            self.boss_appeard = True
            self.all_monsters = pygame.sprite.Group()
            self.boss.lvl = random.randrange(1, 10)
            while self.boss.lvl >= self.boss.lvlprb :
                self.boss.max_health = round(self.boss.max_health * 1.12)
                self.boss.gainexp = round(self.boss.gainexp * 1.12)
                self.boss.damage = round(self.boss.damage * 1.06)
                self.boss.gainegold = round(self.boss.gainegold * 1.12)
                self.boss.movespeed = random.randrange(1, 4)
                self.boss.lvlprb += 1
            self.spawn_boss()
            print(self.boss.lvl, self.boss.max_health, self.boss.gainegold, self.boss.gainexp, self.boss.movespeed, self.boss.damage)
            
    
    def erase_boss (self) :
        self.boss_appeard = False
        self.all_boss = pygame.sprite.Group()
        self.add_gold(self.boss.gainegold)
        self.add_xp(self.boss.gainexp)
        self.boss.max_health = 1000
        self.boss.damage = 100
        self.boss.gainegold = 25
        self.boss.gainexp = 50
        self.boss.movespeed = 0.2
        self.boss.lvl = 1
        self.boss.lvlprb = 1
        self.spawn_monster()

    
    def health_max (self) :
        if self.player.health > self.player.max_health :
            self.player.health = self.player.max_health
            
            
    def pseudotxt (self, screen) :
        self.gamepseudo = 'Enter your name'
        self.fontpseudo = pygame.font.Font('assets\Staatliches-Regular.ttf', 30)
        self.msg_text = self.fontpseudo.render(f"{self.gamepseudo}", 1, (255, 255, 255))
        screen.blit(self.msg_text, (525, 300))

    
    def game_over (self) :
        self.all_monsters = pygame.sprite.Group()
        self.all_boss = pygame.sprite.Group()
        self.player.max_health = 500
        self.player.health = self.player.max_health
        self.player.health2 = self.player.max_health
        self.is_playing = False
        self.player.damage = 20
        self.player.lvl = 1
        self.player.xp = 0
        self.player.next_level = 25
        self.player.points = 0
        self.player.dps = 1
        self.player.prot = 0
        self.player.movespeed = 1
        self.player.gold = 0
        self.boss_appeard = False


    def ajspointsdamage (self) :
        if self.player.points >= 1 :
                self.player.damage += 10
                self.player.points -= 1
    def ajspointsmovespeed (self) :
        if self.player.points >= 1 :
                self.sword.movespeed += 0.5
                self.player.movespeed += 0.5
                self.player.points -= 1
    def ajspointsdps (self) :
        if self.player.dps < 10 :
            if self.player.points >= 1 :
                    self.player.dps += 0.5
                    self.sword.dps -= 2.5
                    self.player.points -= 1
    def ajspointsprot (self) :
        if self.player.points >= 1 :
                self.player.prot += 0.5
                self.player.points -= 1
    
    
    def stats (self, screen) :
        if self.size_jeux_1g == True :
            self.font = pygame.font.Font('assets\Staatliches-Regular.ttf', 45)
            self.font2 = pygame.font.Font('assets\Staatliches-Regular.ttf', 50)
        else :
            self.font = pygame.font.Font('assets\Staatliches-Regular.ttf', 25)
            self.font2 = pygame.font.Font('assets\Staatliches-Regular.ttf', 30)
        self.health_text = self.font.render(f"Damage : {self.player.damage}", 1, (255, 255, 255))
        self.xp_text = self.font.render(f"Level : {self.player.lvl}", 1, (255, 255, 255))
        self.movespeed_text = self.font.render(f"Move Speed : {self.player.movespeed}", 1, (255, 255, 255))
        self.prot_text = self.font.render(f"Resistance : {self.player.prot}", 1, (255, 255, 255))
        self.dps_text = self.font.render(f"Dps : {self.player.dps}", 1, (255, 255, 255))
        self.point_text = self.font.render(f"Points : {self.player.points}", 1, (255, 255, 255))
        self.gold_text = self.font.render(f"Gold : {self.player.gold}", 1, (255, 255, 255))
        # affiche stats
        self.health2_text = self.font2.render("+", 1, (255, 255, 255))
        self.movespeed2_text = self.font2.render("+", 1, (255, 255, 255))
        self.prot2_text = self.font2.render("+", 1, (255, 255, 255))
        self.dps2_text = self.font2.render("+", 1, (255, 255, 255))
        # affiche ajouts a stats
        if self.size_jeux_1g == True :
            pygame.draw.rect(screen, (23, 22, 22), (10, 50, 320, 300))
            pygame.draw.rect(screen, (23, 22, 22), (10, 50, 320, 300), 4)
            # carré noir/gris
            screen.blit(self.xp_text, (15, 55))
            screen.blit(self.health_text, (15, 95))
            screen.blit(self.movespeed_text, (15, 135))
            screen.blit(self.prot_text, (15, 175))
            screen.blit(self.dps_text, (15, 215))
            screen.blit(self.point_text, (15, 255))
            screen.blit(self.gold_text, (15, 295))
            # affichage des informations sur l'écrans
            screen.blit(self.health2_text, (295, 93.5))
            screen.blit(self.movespeed2_text, (295, 132.5))
            screen.blit(self.prot2_text, (295, 173.5))
            screen.blit(self.dps2_text, (295, 212.5))
            # affichage du + pour l'ajouts des points sur l'écrans
            self.health2_text_rect = self.ar.get_rect()
            self.health2_text_rect.x = 194
            self.health2_text_rect.y = 88
            self.movespeed2_text_rect = self.ar.get_rect()
            self.movespeed2_text_rect.x = 194
            self.movespeed2_text_rect.y = 113
            self.dps2_text_rect = self.ar.get_rect()
            self.dps2_text_rect.x = 194
            self.dps2_text_rect.y = 163
            self.prot2_text_rect = self.ar.get_rect()
            self.prot2_text_rect.x = 194
            self.prot2_text_rect.y = 138
        else :
            pygame.draw.rect(screen, (23, 22, 22), (10, 50, 200, 185))
            pygame.draw.rect(screen, (23, 22, 22), (10, 50, 200, 185), 4)
            # carré noir/gris
            screen.blit(self.xp_text, (15, 55))
            screen.blit(self.health_text, (15, 80))
            screen.blit(self.movespeed_text, (15, 105))
            screen.blit(self.prot_text, (15, 130))
            screen.blit(self.dps_text, (15, 155))
            screen.blit(self.point_text, (15, 180))
            screen.blit(self.gold_text, (15, 205))
            # affichage des informations sur l'écrans
            screen.blit(self.health2_text, (195, 77.5))
            screen.blit(self.movespeed2_text, (195, 102.5))
            screen.blit(self.prot2_text, (195, 127.5))
            screen.blit(self.dps2_text, (195, 152.5))
            # affichage du + pour l'ajouts des points sur l'écrans
            self.health2_text_rect = self.ar.get_rect()
            self.health2_text_rect.x = 194
            self.health2_text_rect.y = 88
            self.movespeed2_text_rect = self.ar.get_rect()
            self.movespeed2_text_rect.x = 194
            self.movespeed2_text_rect.y = 113
            self.dps2_text_rect = self.ar.get_rect()
            self.dps2_text_rect.x = 194
            self.dps2_text_rect.y = 163
            self.prot2_text_rect = self.ar.get_rect()
            self.prot2_text_rect.x = 194
            self.prot2_text_rect.y = 138
        
    
    def cooldown_sword (self) :
        self.sword.cooldown2()
        self.sword.move()
        
        
    def stats_inv (self, screen) :
        if self.size_jeux_1g == True :
            self.font = pygame.font.Font('assets\Staatliches-Regular.ttf', 45)
            self.font2 = pygame.font.Font('assets\Staatliches-Regular.ttf', 50)
        else :
            self.font = pygame.font.Font('assets\Staatliches-Regular.ttf', 25)
            self.font2 = pygame.font.Font('assets\Staatliches-Regular.ttf', 30)
        self.font4 = pygame.font.Font('assets\Oswald-Regular.ttf', 18)
        self.health_text = self.font.render(f"Damage : {self.player.damage}", 1, (255, 255, 255))
        self.xp_text = self.font.render(f"Level : {self.player.lvl}", 1, (255, 255, 255))
        self.movespeed_text = self.font.render(f"Move Speed : {self.player.movespeed}", 1, (255, 255, 255))
        self.prot_text = self.font.render(f"Resistance : {self.player.prot}", 1, (255, 255, 255))
        self.dps_text = self.font.render(f"Dps : {self.player.dps}", 1, (255, 255, 255))
        self.point_text = self.font.render(f"Points : {self.player.points}", 1, (255, 255, 255))
        self.gold_text = self.font.render(f"Gold : {self.player.gold}", 1, (255, 255, 255))
        self.health_text_info = self.font4.render(f"{self.player.health}/{self.player.max_health}", 1, (255, 255, 255))
        self.xp_text_info = self.font4.render(f"{self.player.xp}/{self.player.next_level}", 1, (255, 255, 255))
        # affiche stats
        self.health2_text = self.font2.render("+", 1, (255, 255, 255))
        self.movespeed2_text = self.font2.render("+", 1, (255, 255, 255))
        self.prot2_text = self.font2.render("+", 1, (255, 255, 255))
        self.dps2_text = self.font2.render("+", 1, (255, 255, 255))
        # affiche ajouts a stats
        pygame.draw.rect(screen, (43, 43, 43), (10, 50, 200, 185))
        pygame.draw.rect(screen, (43, 43, 43), (10, 50, 200, 185), 4)
        # carré noir/gris
        screen.blit(self.xp_text, (15, 55))
        screen.blit(self.health_text, (15, 80))
        screen.blit(self.movespeed_text, (15, 105))
        screen.blit(self.prot_text, (15, 130))
        screen.blit(self.dps_text, (15, 155))
        screen.blit(self.point_text, (15, 180))
        screen.blit(self.gold_text, (15, 205))
        # affichage des informations sur l'écrans
        screen.blit(self.health2_text, (195, 77.5))
        screen.blit(self.movespeed2_text, (195, 102.5))
        screen.blit(self.prot2_text, (195, 127.5))
        screen.blit(self.dps2_text, (195, 152.5))
        # affichage du + pour l'ajouts des points sur l'écrans
        self.health2_text_rect = self.ar.get_rect()
        self.health2_text_rect.x = 194
        self.health2_text_rect.y = 88
        self.movespeed2_text_rect = self.ar.get_rect()
        self.movespeed2_text_rect.x = 194
        self.movespeed2_text_rect.y = 113
        self.dps2_text_rect = self.ar.get_rect()
        self.dps2_text_rect.x = 194
        self.dps2_text_rect.y = 163
        self.prot2_text_rect = self.ar.get_rect()
        self.prot2_text_rect.x = 194
        self.prot2_text_rect.y = 138
        # coordonné des +
        screen.blit(self.health_text_info, (210, 6))
        screen.blit(self.xp_text_info, (210, 25))
        self.pseudoname = self.font3.render(f"{self.player.pseudo}", 1, (255, 255, 255))
        screen.blit(self.pseudoname, (300, 15))
    

    def update (self, screen) :
        
        
        screen.blit(self.player.image, self.player.rect)
        # permet d'afficher dans le jeu mon joueur, rect peut être ramplacer
        # par des coordonnées ex; (player.image, (0, 0)) / player. permet de chercher
        # player dans la classe Player


        screen.blit(self.sword.image, self.sword.rect)
        # permet d'afficher dans le jeu mon épée


        for monster in self.all_monsters :
        # permet de générer cet fonction pendant que le jeu est en cour
            monster.forward()
            monster.update_health_bar(screen)
            
            
        for boss in self.all_boss :
            boss.forward()
            boss.update_health_bar(screen)
            

        self.all_monsters.draw(screen)
        
        
        self.all_boss.draw(screen)


        self.player.update_health_bar(screen)
        self.player.update_xp_bar(screen)
        self.monster.health_bar_length = 100
        self.monster.health_ratio = self.monster.max_health / self.monster.health_bar_length
        self.player.health_bar_length = 200
        self.player.health_ratio = self.player.max_health / self.player.health_bar_length
        self.player.xp_bar_length = 200
        self.player.xp_ratio = self.player.next_level / self.player.xp_bar_length
        self.boss.health_bar_length = 200
        self.boss.health_ratio = self.boss.max_health / self.boss.health_bar_length
        self.player.pseudo = self.gamepseudo


        while self.player.xp >= self.player.next_level:
            self.player.lvl += 1
            self.player.xp = self.player.xp - self.player.next_level
            self.player.next_level = round(self.player.next_level * 1.4)
            self.player.points += 1
            self.player.health = round(self.player.health * 1.07)
            self.player.max_health = self.player.max_health + 75
            self.player.damage = self.player.damage + 1
            print(self.player.health, self.player.max_health, self.player.damage, self.player.lvl)
            self.player.health = self.player.health + round(self.player.max_health / 1.4)
            self.health_max()


        if self.size_jeux_1g == True :
        
        
            if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < 1875 :
            # on regarde si la touche presser est la droite
            # on regarde si les coordonnées du joueur sont inférieurs à 1900 pour l'arréter
            # sur les bourdures / game.player.rect.width est pour ajouté tout les pixel de
            #l'image player


                self.sword.move_right()
                # permet de relier l'événement de sword.py


                self.player.move_right()
                # permet de relier l'événement de player.py


                self.sword.move()
                    

            elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0 :
            # on regarde si la touche presser est la gauche
            # on regarde si les coordonnées du joueur sont supérieur à 0 pour l'arréter
            # sur les bourdures


                self.sword.move_left()
                # permet de relier l'événement de sword.py


                self.player.move_left()
                # permet de relier l'événement de player.py


                self.sword.move()
        else :
            
            
            if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < 1300 :
            # on regarde si la touche presser est la droite
            # on regarde si les coordonnées du joueur sont inférieurs à 1300 pour l'arréter
            # sur les bourdures / game.player.rect.width est pour ajouté tout les pixel de
            #l'image player


                self.sword.move_right()
                # permet de relier l'événement de sword.py


                self.player.move_right()
                # permet de relier l'événement de player.py


                self.sword.move()
            
            
            elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0 :
            # on regarde si la touche presser est la gauche
            # on regarde si les coordonnées du joueur sont supérieur à 0 pour l'arréter
            # sur les bourdures


                self.sword.move_left()
                # permet de relier l'événement de sword.py


                self.player.move_left()
                # permet de relier l'événement de player.py


                self.sword.move()
            

    def paused (self, screen) :
        self.font3 = pygame.font.Font('assets\Staatliches-Regular.ttf', 50)
        self.continu_e_text = self.font3.render(f"CONTINUE", 1, (255, 255, 255))
        self.continu_e_text_rect = self.continu_e_text.get_rect()
        self.continu_e_text_rect.x = screen.get_width() / 2.40
        self.continu_e_text_rect.y = 200
        self.continu_e_text2 = self.font3.render(f"  CONTINUE  ", 1, (255, 255, 255))
        self.continu_e_text_rect2 = self.continu_e_text2.get_rect()
        self.continu_e_text_rect2.x = 525
        self.continu_e_text_rect2.y = 200
        # bouttons reprendre
        self.restart_text = self.font3.render(f"RESTART", 1, (255, 255, 255))
        self.restart_text_rect = self.restart_text.get_rect()
        self.restart_text_rect.x = (screen.get_width() / 2.40) + 7.5
        self.restart_text_rect.y = 300
        self.restart_text2 = self.font3.render(f"  CONTINUE  ", 1, (255, 255, 255))
        self.restart_text_rect2 = self.restart_text2.get_rect()
        self.restart_text_rect2.x = 525
        self.restart_text_rect2.y = 300
        # bouttons recommencé
        self.quit_text = self.font3.render(f"QUIT", 1, (255, 255, 255))
        self.quit_text_rect = self.quit_text.get_rect()
        self.quit_text_rect.x = (screen.get_width() / 2.40) + 7.5
        self.quit_text_rect.y = 400
        self.quit_text2 = self.font3.render(f"  CONTINUE  ", 1, (255, 255, 255))
        self.quit_text_rect2 = self.quit_text2.get_rect()
        self.quit_text_rect2.x = 525
        self.quit_text_rect2.y = 400
        # bouttons quitter
        if self.pausing == True :
            screen.blit(self.pauseimg, self.pauseimg_rect)
            screen.blit(self.continu_e_text, self.continu_e_text_rect)
            pygame.draw.rect(screen, (255, 255, 255), self.continu_e_text_rect2, 4)
            screen.blit(self.restart_text, self.restart_text_rect)
            pygame.draw.rect(screen, (255, 255, 255), self.restart_text_rect2, 4)
            screen.blit(self.quit_text, self.quit_text_rect)
            pygame.draw.rect(screen, (255, 255, 255), self.quit_text_rect2, 4)
        if self.pausing == False :
            screen.blit(self.pauseimg_rect2, (0, 0))
    
    
    def inventaire (self, screen) :
        self.player.health_bar_length = 200
        self.player.health_ratio = self.player.max_health / self.player.health_bar_length
        self.player.xp_bar_length = 200
        self.player.xp_ratio = self.player.next_level / self.player.xp_bar_length
        if self.inventair == True :
            if self.size_jeux_1g == True :
                pygame.draw.rect(screen, (43, 43, 43), (10, 10, 1880, 980))
                pygame.draw.rect(screen, (43, 43, 43), (10, 10, 1880, 980), 4)
                self.player.update_health_bar_inv(screen)
                self.player.update_xp_bar_inv(screen)
            else : 
                pygame.draw.rect(screen, (43, 43, 43), (10, 10, 1280, 680))
                pygame.draw.rect(screen, (43, 43, 43), (10, 10, 1280, 680), 4)
                self.player.update_health_bar_inv(screen)
                self.player.update_xp_bar_inv(screen)
            


    def check_collision (self, sprite, group) :
    # pour regardé si il y a une collision
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


    def spawn_monster (self) :
        monster = Monster(self)
        self.monster.lvl = random.randrange(1, 10)
        self.all_monsters.add(monster)
        # ajouter monster dans le groupe all_monsters
        
        
    def spawn_boss (self) :
        boss = Boss(self)
        self.boss.lvl = random.randrange(1, 10)
        self.all_boss.add(boss)
    
    
    def cheat (self) :
        self.player.max_health = 999999
        self.player.damage = 999999
        self.player.prot = 200
        self.player.movespeed = 20
        self.player.dps = 999
        self.sword.dps = 2
        self.sword.movespeed = 20