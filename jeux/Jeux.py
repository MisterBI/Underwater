import pygame
import time
from random import*
pygame.init()

##############__________Autre paramètre, temps , couleur , dimension fenetre _____________###################################
t = (255,255,255,.4)
blue = (113,122,255)
white =(255,255,255) 
horloge = pygame.time.Clock()

win = pygame.display.set_mode((1920,980))  ##fentre de dimension 1920:980
pygame.display.set_caption("Underwater ")  ## nom de la fentre 

icon = pygame.image.load('img/plastic.png')  ## icone et nom  de la fênetre
pygame.display.set_icon(icon)                ##icone de notre jeux en haut de la fentre 
bg = pygame.image.load('img/background.jpg') ##fond de notre jeux 

x=400
y=600





#######################______________Personnage_____________########################################
## image pour l'animation du perosnnage (Enormément d'image en double normal pour évité une erreur d'indexage)


x_perso = 400
y_perso = 1000
persoW = 40                       ##coordonées et vitesse du personne 
persoH = 60
vitesse = 10


walkLeft= [pygame.image.load('img/1.png'), pygame.image.load('img/2.png'), pygame.image.load('img/3.png'), pygame.image.load('img/4.png'), pygame.image.load('img/5.png'), pygame.image.load('img/6.png'), pygame.image.load('img/2.png'), pygame.image.load('img/3.png'), pygame.image.load('img/4.png'), pygame.image.load('img/5.png'), pygame.image.load('img/6.png'), pygame.image.load('img/2.png'), pygame.image.load('img/3.png'), pygame.image.load('img/4.png'), pygame.image.load('img/5.png'), pygame.image.load('img/6.png'), pygame.image.load('img/2.png'), pygame.image.load('img/3.png'), pygame.image.load('img/4.png'), pygame.image.load('img/5.png'), pygame.image.load('img/6.png'),pygame.image.load('img/1.png'), pygame.image.load('img/2.png'), pygame.image.load('img/3.png'), pygame.image.load('img/4.png'), pygame.image.load('img/5.png'), pygame.image.load('img/6.png'), pygame.image.load('img/2.png'), pygame.image.load('img/3.png'), pygame.image.load('img/4.png'), pygame.image.load('img/5.png'), pygame.image.load('img/6.png'), pygame.image.load('img/2.png'), pygame.image.load('img/3.png'), pygame.image.load('img/4.png'), pygame.image.load('img/5.png'), pygame.image.load('img/6.png'), pygame.image.load('img/2.png'), pygame.image.load('img/3.png'), pygame.image.load('img/4.png'), pygame.image.load('img/5.png'), pygame.image.load('img/6.png')]
walkRight = [pygame.image.load('img/L1.png'), pygame.image.load('img/L2.png'), pygame.image.load('img/L3.png'), pygame.image.load('img/L4.png'), pygame.image.load('img/L5.png'), pygame.image.load('img/L6.png'), pygame.image.load('img/L2.png'), pygame.image.load('img/L3.png'), pygame.image.load('img/L4.png'), pygame.image.load('img/L5.png'), pygame.image.load('img/L6.png'), pygame.image.load('img/L2.png'), pygame.image.load('img/L3.png'), pygame.image.load('img/L4.png'), pygame.image.load('img/L5.png'), pygame.image.load('img/L6.png'), pygame.image.load('img/L2.png'), pygame.image.load('img/L3.png'), pygame.image.load('img/L4.png'), pygame.image.load('img/L5.png'), pygame.image.load('img/L6.png'),pygame.image.load('img/L1.png'), pygame.image.load('img/L2.png'), pygame.image.load('img/L3.png'), pygame.image.load('img/L4.png'), pygame.image.load('img/L5.png'), pygame.image.load('img/L6.png'), pygame.image.load('img/L2.png'), pygame.image.load('img/L3.png'), pygame.image.load('img/L4.png'), pygame.image.load('img/L5.png'), pygame.image.load('img/L6.png'), pygame.image.load('img/L2.png'), pygame.image.load('img/L3.png'), pygame.image.load('img/L4.png'), pygame.image.load('img/L5.png'), pygame.image.load('img/L6.png'), pygame.image.load('img/L2.png'), pygame.image.load('img/L3.png'), pygame.image.load('img/L4.png'), pygame.image.load('img/L5.png'), pygame.image.load('img/L6.png')]
                                                   ##créaion de la liste d'image pour l'annimation du personnage //// bcp de copie pour évité les erreurs d'indéxage 
char = pygame.image.load('img/standing.png')       ##Image du lors que le personnage n'est pas en mouvement 





isJump = False
jumpCount = 10
                              ## variable suplémentaire pour le personnage 
left = False
right = False
walkCount = 0


########################________________ bateau___________#####################################################
NavirW = 200
NavirH = 100                                 ## coordonées du bateau 
x_navir = 200
y_navir = 450


navir = pygame.image.load('img/NAVIRE.png')  ## image du bateau 




init = True



###################_________________GameOver_____________####################################################

def game0ver ():
    
    message("Perdu!!!")  ##afficher message perdu!!!! grace à la fonction message


##################_________Création d'un mots____________##################################################


def creaTextObjet (texte , police):
    texteSurface = police.render(texte,True,white)
    return texteSurface, texteSurface.get_rect()




#################_______________Création de texte _____________#############################################


def message (texte):
    
    global x_perso                            
                                            ## global les coordonées du personnage pour lui changé ça possition une fois en colision avec le bateau pour éviter de rester en gameover
    global y_perso

    GTexte = pygame.font.Font('font/Second.ttf',150)
    Ptexte = pygame.font.Font('font/Second.ttf ', 100)                        ## parametrage de la police font et taille du texte
    RetournerMenu = pygame.font.Font ('font/Second.ttf ',150)


    GtexteSurf,GTexteRect = creaTextObjet (texte, GTexte)               ## création d'un rectangle qui acceuil la zone de texte 
    GTexteRect.center = int(1920/2) , (int(980/2)-50)                   ## positionnement du texte 
    win.blit(GtexteSurf, GTexteRect)                                    ## affiche 
    PtexteSurf,PtexteRect = creaTextObjet("Roujé dans 5 secondes",Ptexte)   ##  <<
    PtexteRect.center = int(1920 / 2) , (int(980 / 2) + 50)                 ##  <<
    win.blit ( PtexteSurf, PtexteRect )                                     ##  <<
    RetourMenuSurf,RetourMenuRect = creaTextObjet('Home',RetournerMenu)     ##  <<
    RetournerMenu= 1920 / 2 , ((980 /3) + 50)                               ##  <<
    win.blit ( RetourMenuSurf, RetourMenuRect )                             ##  <<
    
    pygame.display.update()                                             ## mise à jour de l'affichaque 
    
    x_perso = x_perso + 50 
                                                                    ## change les coordonées du perosnnage 
    y_perso = y_perso + 50                 

    time.sleep(5)                                                   ## attendre 5seconde pour rejouer
    corps_game()                                                    ## appel la fonction corps_game pour relancer 

###############________________Création des fps__________________###########################################


def fps_affiche ():

    Seconde_txt = pygame.font.SysFont('font/Second.ttf', 35)

    FPStexteSurf,FPStexteRect = creaTextObjet('FPS: {:.2f}'.format(horloge.get_fps()),Seconde_txt) ## création d'un texte afficher les 2 premiers nombre apres la virgule
    FPStexteRect.topleft = (1780,920)                                                              ## emplacement du texte
    win.blit(FPStexteSurf,FPStexteRect)                                                            ## affichage du texte (fps)


    
##############_______________Fonciton gère toutes les colisions_____________####################################



def colision () : 
    
    global x_perso
    global y_perso            ## globalisation des variable qu'on à besoin 
    global x_navir 
    global y_navir 

    char_rect = pygame.draw.rect(win, (255, 255, 255, 255), (int(x_perso), int(y_perso), 60, 60)) 
                                                                                                       ## création d'un réctangle qui modélise les "hitbox" du perso et du navir
    nav_rect = pygame.draw.rect(win,  (255, 255, 255), (int(x_navir), int(y_navir), 200, 70))
        
        
 
    print(char_rect.colliderect(nav_rect))
    if char_rect.colliderect(nav_rect):             ## condition si les deux réctangle son en colision alors gameover et font noir 
        win.fill((0, 0, 0))
        game0ver()




    #################__________Mouvement du perosnage et du navir__________######################################




def mvt_pero():


     global NavirW
     global x_navir
     global y_navir                         ## globalisation des variable qui nous faut 
     global walkCount
     global x_perso
     global y_perso
    
     

    
     win.blit(navir, (int(x_navir) ,int(y_navir)))       ## afficher le navir et le mettre en mouvement en lui soustrant ça vitesse
     x_navir -= vitesse
    
    

  
     if x_navir < (-0.5*NavirW):                        ## permet de faire passer le navir d'un coté à l'autre coté lorsqu'il arrive à la fin de la fenetre 
        x_navir = 1920
        
    
     if walkCount + 1 >= 27:                            ## varaible qui permet de se situé dans quelle liste on ce trouve 27 et le nombre d'image pour faire l'annimation
        walkCount = 0
        
     if left:  
        win.blit(walkLeft[walkCount//3], (int(x_perso),int(y_perso)))         ## indique que lorsque la variable left est true alors aficher les images de la liste walkleft
        walkCount += 1                                                           ## incrément de 1 pour changer d'image afin de faire l'annimation
     elif right:
        win.blit(walkRight[walkCount//3], (int(x_perso),int(y_perso)))        ## indique que lorsuqe la variable right est true alors afficher les images de la liste walkright
        walkCount += 1                                                           ## incrément de 1 pour changer d'image afin de faire l'annimation
     else:
        win.blit(char, (int(x_perso), int(y_perso)))                         ## si on ne va pas à droite ni à gauche alors on affiche une image appelé char   
        walkCount = 0                                                           ## donc on incremente pas la variable walcount car pas de liste une seul image est blit
   



############______________________Projection de dechet_____________________##################################

def projectif ():

    global x_navir 
    global y_navir 

    x_objet = 1000
    y_objet = 400
    objet = pygame.image.load("img/Pomme.png")
    win.blit(objet, (x_objet, y_objet))
    













 #############_____________________Fonction principal du jeux_____________####################################




def corps_game():
    global x
    global y
    global X
    global Y
    global y_perso
    global x_perso
    global persoH
    global persoW
    global x_navir
    global y_navir
    global NavirH
    global NavirW
    global vitesse 
    global left                                       ## globalisation de toutes les variables qu'ont à besoin 
    global right
    global jump
    global walkcount
    global jumpCount
    global isJump
    global nav_hit_box
    global char_hit_box
    global char 
    global navir
    global nav_rect
    global char_rect
    global dechet
    global vitesse 
    global dechetX
    global dechetY
    x_objet = x_navir 
    y_objet = 450




    
    
    
    
    run = True 
    
    while run :
        horloge.tick(60)               ## démarre l'horloge du jeux à 60 
        fps_affiche()                  ## appel la fonction pour les fps 
          
        pygame.time.set_timer(24, 1000)   
        pygame.display.flip()
        
                        ## appel la fonction colision                    
       
        colision()    

        win.blit(bg, (0,0))           ## afficher le fond du jeux 
        
        projectif()
        
            
        
      
       

        if y_perso >= 920:
            y_perso= 919                         ## on délimite la zone de jeux 
        if x_perso > 1889:
            x_perso = 1887
     
 
        for event in pygame.event.get():         ##comunicaton entre le clavier et le jeux (début)        
            run = False

               
        keys = pygame.key.get_pressed()            

        if keys[pygame.K_a] :
            win.blit(objet, (x_navir, y_objet))
            y_objet -= 5

            


        if keys[pygame.K_ESCAPE] : 
            quit()                                 ## echape pour fermer le jeux 

        if keys[pygame.K_UP] and x_perso > vitesse:
            y_perso-= vitesse                           ##pour ce diriger faire le haut left et right ne sont pas true parce que pas besoin
            left = False 
            right = False
        
        if keys[pygame.K_DOWN] and x_perso > vitesse:
            y_perso += vitesse                         ## pour ce diriger vers le bas left et right ...........
            left = False
            right = False
        
        if keys[pygame.K_LEFT] and x_perso > vitesse: 
            x_perso -= vitesse
            left = True                                ## pour ce diriger vers la droite on change la variable left en true et donc on affichera alors les images de la liste walkleft 
            right = False

        elif keys[pygame.K_RIGHT] and x_perso < 1980 - vitesse :  
            x_perso += vitesse
            left = False                               ## pour ce diriger vers la gauche on change la variable right
            right = True
        
        else: 
            left = False
            right = False                               ## si dans les deux cas on ce dirige pas vers la gauche ni vers la droite alors on indique en changent les variables left right et walkcount que l'on affiche l'image char standard 
            walkCount = 0
        
        if not(isJump):
            if keys[pygame.K_SPACE]:
                isJump = True
                left = False
                right = False
                walkCount = 0                          
            if y_perso <= 500:
                y_perso = 499                            ## on parametre le saut 
        elif y_perso >= 920 :
                y_perso = 919 
        else:
            if jumpCount >= -10:
                y_perso -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1
            else: 
                jumpCount = 10
                isJump = False
        
            
            
       

        mvt_pero()                               ## appélation de la fonction mvt_perso
        
         
    
        pygame.display.update()                  ## mis à jours de l'écran
        
while init:     
    corps_game()
quit()
    
    
