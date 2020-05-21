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

perso =  {
    
    "X" : 1000,
    "Y" : 600,
    "taille" : (40,60),
    "vitesse" : 10,

    "walkLeft" : [pygame.image.load('img/1.png'), pygame.image.load('img/2.png'), pygame.image.load('img/3.png'), pygame.image.load('img/4.png'), pygame.image.load('img/5.png'), pygame.image.load('img/6.png'), pygame.image.load('img/2.png'), pygame.image.load('img/3.png'), pygame.image.load('img/4.png'), pygame.image.load('img/5.png'), pygame.image.load('img/6.png'), pygame.image.load('img/2.png'), pygame.image.load('img/3.png'), pygame.image.load('img/4.png'), pygame.image.load('img/5.png'), pygame.image.load('img/6.png'), pygame.image.load('img/2.png'), pygame.image.load('img/3.png'), pygame.image.load('img/4.png'), pygame.image.load('img/5.png'), pygame.image.load('img/6.png'),pygame.image.load('img/1.png'), pygame.image.load('img/2.png'), pygame.image.load('img/3.png'), pygame.image.load('img/4.png'), pygame.image.load('img/5.png'), pygame.image.load('img/6.png'), pygame.image.load('img/2.png'), pygame.image.load('img/3.png'), pygame.image.load('img/4.png'), pygame.image.load('img/5.png'), pygame.image.load('img/6.png'), pygame.image.load('img/2.png'), pygame.image.load('img/3.png'), pygame.image.load('img/4.png'), pygame.image.load('img/5.png'), pygame.image.load('img/6.png'), pygame.image.load('img/2.png'), pygame.image.load('img/3.png'), pygame.image.load('img/4.png'), pygame.image.load('img/5.png'), pygame.image.load('img/6.png')],
    "walkRight" : [pygame.image.load('img/L1.png'), pygame.image.load('img/L2.png'), pygame.image.load('img/L3.png'), pygame.image.load('img/L4.png'), pygame.image.load('img/L5.png'), pygame.image.load('img/L6.png'), pygame.image.load('img/L2.png'), pygame.image.load('img/L3.png'), pygame.image.load('img/L4.png'), pygame.image.load('img/L5.png'), pygame.image.load('img/L6.png'), pygame.image.load('img/L2.png'), pygame.image.load('img/L3.png'), pygame.image.load('img/L4.png'), pygame.image.load('img/L5.png'), pygame.image.load('img/L6.png'), pygame.image.load('img/L2.png'), pygame.image.load('img/L3.png'), pygame.image.load('img/L4.png'), pygame.image.load('img/L5.png'), pygame.image.load('img/L6.png'),pygame.image.load('img/L1.png'), pygame.image.load('img/L2.png'), pygame.image.load('img/L3.png'), pygame.image.load('img/L4.png'), pygame.image.load('img/L5.png'), pygame.image.load('img/L6.png'), pygame.image.load('img/L2.png'), pygame.image.load('img/L3.png'), pygame.image.load('img/L4.png'), pygame.image.load('img/L5.png'), pygame.image.load('img/L6.png'), pygame.image.load('img/L2.png'), pygame.image.load('img/L3.png'), pygame.image.load('img/L4.png'), pygame.image.load('img/L5.png'), pygame.image.load('img/L6.png'), pygame.image.load('img/L2.png'), pygame.image.load('img/L3.png'), pygame.image.load('img/L4.png'), pygame.image.load('img/L5.png'), pygame.image.load('img/L6.png')],
                                                        ##créaion de la liste d'image pour l'annimation du personnage //// bcp de copie pour évité les erreurs d'indéxage 
    "char" : pygame.image.load('img/standing.png')  ,     ##Image du lors que le personnage n'est pas en mouvement 
    "isJump" : False,
    "jumpCount" : 10,
                              ## variable suplémentaire pour le personnage 
    "let" : False,
    "right" : False,
    "walkCount" : 0,

}



init = True,








########################________________ bateau___________#####################################################
navir ={
    
    
    
    
    "NavirW" : 200,
    "NavirH" : 100  ,                               ## coordonées du bateau 
    "x" : 200,
    "y" : 450,


    "navir" :  pygame.image.load('img/NAVIRE.png') , ## image du bateau 


    "vitesse" : 10,

    
}


###################_________________GameOver_____________####################################################

def game0ver ():
    
    message("Perdu!!!")  ##afficher message perdu!!!! grace à la fonction message


##################_________Création d'un mots____________##################################################


def creaTextObjet (texte , police):
    texteSurface = police.render(texte,True,white)
    return texteSurface, texteSurface.get_rect()




#################_______________Création de texte _____________#############################################


def message (texte):
    
    

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
    
    perso["x"]= perso["x"] + 50 
                                                                    ## change les coordonées du perosnnage 
    perso["y"] = perso["y"] + 50                 

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
    
 
 

    char_rect = pygame.draw.rect(win, (255, 255, 255, 255), (int(perso["x"]), int(perso["y"]), 60, 60)) 
                                                                                                       ## création d'un réctangle qui modélise les "hitbox" du perso et du navir
    nav_rect = pygame.draw.rect(win,  (255, 255, 255), (int(navir["x"]), int(navir["y"]), 200, 70))
        
        
 
    print(char_rect.colliderect(nav_rect))
    if char_rect.colliderect(nav_rect):             ## condition si les deux réctangle son en colision alors gameover et font noir 
        win.fill((0, 0, 0))
        game0ver()




    #################__________Mouvement du perosnage et du navir__________######################################




def mvt_pero():


     
   
    
     

    
     win.blit(navir["navir"], (int(navir["x"]) ,int(navir["y"])))       ## afficher le navir et le mettre en mouvement en lui soustrant ça vitesse
     navir["x"] -= navir["vitesse"]
    
    if perso["x"] > 920 :
        perso["x"]= 919                         ## on délimite la zone de jeux 
    if perso["y"] > 1898:
        perso["y"] = 1887
    

  
     if navir["x"] < (-0,5*navir["NavirW"]):                        ## permet de faire passer le navir d'un coté à l'autre coté lorsqu'il arrive à la fin de la fenetre 
        navir["x"] = 1920
        
    
     if perso["walkCount"] + 1 >= 27:                            ## varaible qui permet de se situé dans quelle liste on ce trouve 27 et le nombre d'image pour faire l'annimation
        perso["walkCount"] = 0
        
     if perso["left"]:  
        win.blit(perso["walkLeft"][perso["walkCount"]//3], (int(perso["x"]),int(perso["y"])))         ## indique que lorsque la variable left est true alors aficher les images de la liste walkleft
        perso["walkCount"] += 1                                                           ## incrément de 1 pour changer d'image afin de faire l'annimation
     elif perso["right"]:
        win.blit(perso["walkRight"][perso["walkCount"]//3], (int(perso["x"]),int(perso["y"])))        ## indique que lorsuqe la variable right est true alors afficher les images de la liste walkright
        perso["walkCount"] += 1                                                           ## incrément de 1 pour changer d'image afin de faire l'annimation
     else:
        win.blit(perso["char"], (int(perso["x"]), int(perso["y"])))                         ## si on ne va pas à droite ni à gauche alors on affiche une image appelé char   
        perso["walkCount"] = 0                                                           ## donc on incremente pas la variable walcount car pas de liste une seul image est blit
   



############______________________Projection de dechet_____________________##################################


    













 #############_____________________Fonction principal du jeux_____________####################################




def corps_game():
    global x
    global y
    xp=[]
    yp=[]
    pommes=[]

    




    
    
    
    
    run = True 
    
    while run :
        horloge.tick(60)               ## démarre l'horloge du jeux à 60 
        fps_affiche()                  ## appel la fonction pour les fps 
          
        pygame.time.set_timer(24, 1000)   
        pygame.display.flip()
        
                        ## appel la fonction colision                    
       
        colision()    

        win.blit(bg, (0,0))           ## afficher le fond du jeux 
        
        
        
        
        
           # A toi de changer les objets , de gérer les collisions et le score. Rien de compliqué ici je pense

        aleat=randint (1,100)     #Affichage aléatoire des pommes en fonction de la position du navire
        if aleat < 4:       # entre 0 et 100. Plus on se rapproche de 100, plus il y aura des pommes
            pommes.append(pygame.image.load("img/pomme.png").convert_alpha())  #on crée la pomme ainsi que ses coordonnées
            xp.append(navir["x"])
            yp.append(navir["y"])

        for i in range(len(pommes)):   #On affiche les pommes
             win.blit(pommes[i],(xp[i],yp[i]))

        for i in range(len(pommes)):      #on gère leur déplacement
            yp[i]+= 5
            if yp[i]==1000:               #on les supprime lorsqu'elle sont en bas de l'écran
                del pommes[i] 
                del xp[i]
                del yp[i]
    ##############################################################################################################################
    #             A toi de gérer les collisions certainement ici ou ailleurs....

    #           soit avec la méthode collide ou en testant les coordonnées tout simplement
    ##############################################################################################################################             

 
        
      
       


     
 
        for event in pygame.event.get():         ##comunicaton entre le clavier et le jeux (début)        
            run = False

               
        keys = pygame.key.get_pressed()            

        if keys[pygame.K_a] :
            win.blit(objet, (navir["x"], navir["y"]))
            perso["y"] -= 5

            


        if keys[pygame.K_ESCAPE] : 
            quit()                                 ## echape pour fermer le jeux 

        if keys[pygame.K_UP] and perso["x"] > perso["vitesse"]:
            perso["y"] -= perso["vitesse"]                           ##pour ce diriger faire le haut left et right ne sont pas true parce que pas besoin
            perso["left"] = False 
            perso["right"] = False
        
        if keys[pygame.K_DOWN] and perso["x"] > perso["vitesse"]:
            perso["y"] += perso["vitesse"]                         ## pour ce diriger vers le bas left et right ...........
            perso["left"] = False
            perso["right"] = False
        
        if keys[pygame.K_LEFT] and perso["x"] > perso["vitesse"]: 
            perso["x"] -= perso["vitesse"]
            perso["left"] = True                                ## pour ce diriger vers la droite on change la variable left en true et donc on affichera alors les images de la liste walkleft 
            perso["right"] = False

        elif keys[pygame.K_RIGHT] and perso["x"] < 1980 - perso["vitesse"] :  
            perso["x"] += perso["vitesse"] 
            perso["left"] = False                               ## pour ce diriger vers la gauche on change la variable right
            perso["right"] = True
        
        else: 
            perso["left"] = False
            perso["right"] = False                               ## si dans les deux cas on ce dirige pas vers la gauche ni vers la droite alors on indique en changent les variables left right et walkcount que l'on affiche l'image char standard 
            perso["walkCount"] = 0
        
        if not(perso["isJump"]):
            if keys[pygame.K_SPACE]:
                perso["isJump"] = True
                perso["left"] = False
                perso["right"] = False
                perso["walkCount"] = 0                          
            if perso["y"] <= 500:
                perso["y"]= 499                            ## on parametre le saut 
        elif perso["y"] >= 920 :
                perso["y"] = 919 
        else:
            if perso["jumpCount"] >= -10:
                perso["y"] -= (perso["jumpCount"] * abs(perso["jumpCount"])) * 0.5
                perso["jumpCount"] -= 1
            else: 
                perso["jumpCount"] = 10
                perso["isJump"] = False
        
            
            
       

        mvt_pero()                               ## appélation de la fonction mvt_perso
        
         
    
        pygame.display.update()                  ## mis à jours de l'écran
        
while init :     
    corps_game()
quit()
    
    
