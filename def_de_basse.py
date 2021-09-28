from math import trunc
import pygame
import time
import sys
import pyautogui
from game import Game
from player import Player
pygame.init()


# generer la fenetre du jeu


pygame.display.set_caption("RPG Tempest")
# définir le nom du jeu et/ou l'icone


size_screen = pyautogui.size()

if size_screen == (1920, 1080) :
    screen = pygame.display.set_mode((1900, 1000))
    size_jeux_1 = True
else :    
    screen = pygame.display.set_mode((1300, 700))
    # définir la taille de la fenetre (et autre)
    # screen est une variable qui permet de récuperer la dimension de la fenetre
    size_jeux_2 = True


background = pygame.image.load(r'assets\bg.png')
# importer l'arrière plan du jeu


if size_jeux_1 == True :
    resized_background = pygame.transform.scale (background, (1900, 1000))
    # redimensionner l'arrière plan par rapport à la taille de la fenetre
else :
    resized_background = pygame.transform.scale (background, (1300, 700))


banner = pygame.image.load(r'assets\Bannière.png')

if size_jeux_1 == True :
    resized_banner = pygame.transform.scale (banner, (1900, 1000))
else :
    resized_banner = pygame.transform.scale (banner, (1300, 800))
resized_banner2 = pygame.transform.scale (banner, (1, 1))


resized_banner_rect = resized_banner.get_rect()


font = pygame.font.Font('assets\Staatliches-Regular.ttf', 40)
bienvenue_text = font.render("Click to play", 1, (255, 255, 255))
bienvenue_text_rect = bienvenue_text.get_rect()
bienvenue_text_rect.x = screen.get_width() / 2.40
bienvenue_text_rect.y = screen.get_height() / 1.75


game = Game()
# charger le jeu / la classe Game
player = Player(game)


running = True
# variable qui permet d'informé le système si le jeu est lancé

if size_jeux_1 == True :
    game.size_jeux_1g = True
    pseudo = ''
    maxname = 0
    font = pygame.font.Font('assets\Staatliches-Regular.ttf', 50)
    fontpseudo = pygame.font.Font('assets\Staatliches-Regular.ttf', 50)
    pseudo_enter_text = fontpseudo.render(f"Enter a pseudo", 1, (255, 255, 255))
else :
    pseudo = ''
    maxname = 0
    font = pygame.font.Font('assets\Staatliches-Regular.ttf', 30)
    fontpseudo = pygame.font.Font('assets\Staatliches-Regular.ttf', 30)
    pseudo_enter_text = fontpseudo.render(f"Enter a pseudo", 1, (255, 255, 255))


while running :
# boucle tant que la condition running est vrai (true)


    if game.is_playing :
        # vérifier si notre jeu a commencé
        screen.blit(resized_background, (0, 0))
        # définir l'arrière plan
        game.update(screen)
        game.stats(screen)
        game.cooldown_sword()
        maxname = 0
        player.pseudo = pseudo
        if player.pseudo == "cheat" :
            game.cheat()
    elif player.rpseudo == True :
        player.pseudo = pseudo
        game.gamepseudo = pseudo
        resized_banner_rect = resized_banner2.get_rect()
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 1920, 1080))
        if size_jeux_1 == True :
            pygame.draw.rect(screen, (255, 255, 255), (795, 433, 380, 45), 4)
        else :
            pygame.draw.rect(screen, (255, 255, 255), (445, 320, 350, 45), 4)
        if maxname > 0 :
            pseudo_enter_text = fontpseudo.render(f"", 1, (255, 255, 255))
        elif maxname <= 0 :
            pseudo_enter_text = fontpseudo.render(f"Enter your name", 1, (255, 255, 255))
        if size_jeux_1 == True :
            screen.blit(pseudo_enter_text, (800, 425))
            fkname = font.render(f"{pseudo}", 1, (255, 255, 255))
            screen.blit(fkname, (800, 425))
        else :
            screen.blit(pseudo_enter_text, (450, 325))
            fkname = font.render(f"{pseudo}", 1, (255, 255, 255))
            screen.blit(fkname, (450, 325))
       
    elif game.pausing == True :
        if event.type == pygame.MOUSEBUTTONDOWN :
            if game.continu_e_text_rect2.collidepoint (event.pos) :
                game.pausing = False
                game.is_playing = True
            if game.restart_text_rect2.collidepoint (event.pos) :
                game.game_over()
                pseudo = ''
                game.pausing = False
            if game.quit_text_rect2.collidepoint (event.pos) :
                game.pausing = False
                running = False
                pygame.quit()
    elif game.inventair == True :
        game.stats_inv(screen)
        if event.type == pygame.MOUSEBUTTONDOWN :
            # on regarde si l'événement est la pression d'un boutton de souris

        
            if game.health2_text_rect.collidepoint (event.pos) :
                game.ajspointsdamage()
                time.sleep(1)
            if game.movespeed2_text_rect.collidepoint (event.pos) :
                game.ajspointsmovespeed()
                time.sleep(1)
            if game.dps2_text_rect.collidepoint (event.pos) :
                game.ajspointsdps()
                time.sleep(1)
            if game.prot2_text_rect.collidepoint (event.pos) :
                game.ajspointsprot()
                time.sleep(1)
                
    else :
        screen.blit(resized_banner, (0, -100))
        screen.blit(bienvenue_text, bienvenue_text_rect)
        resized_banner_rect = resized_banner.get_rect()


    pygame.display.flip()
    # mettre a jour l'écran pour pouvoir voir l'arrière plan
    

    for event in pygame.event.get () :
    # récuperer les événements de pygame, tous
        
        if event.type == pygame.QUIT :
        # on regarde si l'événement est pygame.QUIT
            
            running = False
            # si l'événements est vrai alors changé running en False
            
            pygame.quit()
            # pour fermé la fenetre
            
            print("Fermeture du jeu")
            # pour vérifier si sa fonctionne en l'affichant dans la console


        elif event.type == pygame.KEYDOWN :
        # on regarde si l'événement est pygame.KEYDOWN


            game.pressed[event.key] = True
            # lui dire que la touche est active
            if player.rpseudo == True :
                if event.key == pygame.K_RETURN :
                    game.start()
                    player.rpseudo = False
                    game.is_playing = True
                    print(pseudo)
                    player.pseudo = pseudo
                    game.gamepseudo = pseudo
                    print(player.pseudo)
                elif event.key == pygame.K_BACKSPACE :
                    pseudo = pseudo[:-1]
                    if maxname > 0 :
                        maxname -= 1
                else :
                    if maxname <= 15 :
                        pseudo += event.unicode
                        player.pseudo = pseudo
                        game.gamepseudo = pseudo
                        maxname += 1
                        game.pseudotxt(screen)
                        print(event.unicode)
            elif event.key == pygame.K_ESCAPE :
                if game.inventair == False :
                    game.is_playing = False
                    game.pausing = True
                    game.paused(screen)
                elif game.inventair == True :
                    game.is_playing = True
                    game.inventair = False
            elif event.key == pygame.K_e :
                if player.rpseudo == False :
                    if game.pausing == False :
                        game.is_playing = not game.is_playing
                        game.inventair = not game.inventair
                        game.inventaire(screen)
        if game.pausing == True :
            continue
        if game.inventair == True :
            continue
        if player.pseudo == True :
            continue
                       

        elif event.type == pygame.KEYUP :
        # on regarde si l'événement est pygame.KEYUP


            game.pressed[event.key] = False
            # lui dire que la touche n'est pas active
       
        
        if event.type == pygame.MOUSEBUTTONDOWN :
        # on regarde si l'événement est la pression d'un boutton de souris

        
            if game.health2_text_rect.collidepoint (event.pos) :
                game.ajspointsdamage()
            if game.movespeed2_text_rect.collidepoint (event.pos) :
                game.ajspointsmovespeed()
            if game.dps2_text_rect.collidepoint (event.pos) :
                game.ajspointsdps()
            if game.prot2_text_rect.collidepoint (event.pos) :
                game.ajspointsprot()
            if game.continu_e_text_rect2.collidepoint (event.pos) :
                if game.pausing == True :
                    game.pausing = False
        

            if resized_banner_rect.collidepoint (event.pos) :
            # si il rentre en collision avec resized_banner_rect
                player.rpseudo = True
                game.is_playing = False