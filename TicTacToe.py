###############################
#           PACKAGES
###############################
import numpy as np
###############################


def gagner(tableau, num_joueur):
    ligne = 0
    colonne = 0

    if(num_joueur == 0):
        signe = "X"
    else:
        signe = "O"

    ###############################
    # l'un d'eux à 3 c'est gagné
    trouve_ligne = 0
    trouve_colonne = 0
    trouve_diago_principale = 0
    trouve_diago_secondaire = 0
    ###############################

    # lignes
    for ligne in range(0, 3):
        trouve_ligne = 0
        for colonne in range(0, 3):
            if(tableau[ligne][colonne] == signe):
                trouve_ligne += 1
                if(trouve_ligne == 3):
                    print("trouvé ligne")
                    return True

    # colonnes
    for colonne in range(0, 3):
        trouve_colonne = 0
        for ligne in range(0, 3):
            if(tableau[ligne][colonne] == signe):
                trouve_colonne += 1
                if(trouve_colonne == 3):
                    print("trouvé colonne")
                    return True

    # diagonale principal
    for ligne in range(0, 3):
        if(tableau[ligne][ligne] == signe):
            trouve_diago_principale += 1
            if(trouve_diago_principale == 3):
                print("trouvé diago principale")
                return True

    # diagonale secondaire
    # ligne     i       colonne(ligne+i)
    # 0         2       2
    # 1         0       1
    # 2         -2      0

    i = 2
    for ligne in range(0, 3):
        if(tableau[ligne][ligne+i] == signe):
            trouve_diago_secondaire += 1
            if(trouve_diago_secondaire == 3):
                print("trouvé diago secondaire")
                return True
        i = -2

    return False


def lancer_jeu():
    tableau = np.array([
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."]
    ])

    # pour un meilleur visuel
    joueur1 = str(input("Donnez le nom du premier joueur : "))
    joueur2 = str(input("Donnez le nom du deuxième joueur : "))

    resultat = False  # pour le test de gagner
    rempli = False  # pour tester ex aequo, le tableau est totalement rempli mais personne n'a gagné
    tour = 1  # traçage du jeu
    num_joueur = 0  # joueur 0 et joueur 1 pour le test de gagner

    while resultat == False and rempli == False:

        # choisis par le joueur
        ligne = 0
        colonne = 0

        print("tour : ", tour)

        ###################################
        # prendre le nom du joueur courant
        if(num_joueur == 0):
            joueur_courant = joueur1
        else:
            joueur_courant = joueur2

        print("joueur : ", joueur_courant)
        ###################################

        # prendre le choix du joueur
        # on prend entre 1 et 3 pour un bon visuel, le joueur ne va pas se casser la tête à comprendre qu'il faut commencer de 0
        # il faut aussi vérifier qu'il a entré une valeur valide
        ligne = int(input("choisissez la ligne (1,2,3) : "))
        while(ligne <= 0 and ligne > 3 and ligne != None):
            ligne = int(input("non, choisissez la ligne (1,2,3) : "))

        colonne = int(input("choisissez la colonne (1,2,3) : "))
        while(colonne <= 0 and colonne > 3 and colonne != None):
            colonne = int(input("non, choisissez la colonne (1,2,3) : "))

        # pour rendre dans le bon indice pour le programme (0,1,2) au lieu de (1,2,3)
        ligne -= 1
        colonne -= 1

        # il a choisis une case non vide
        if(tableau[ligne][colonne] != "."):
            print("Cette case est déjà prise !!!!!!!!")
        else:
            # poser le signe du joueur
            if(num_joueur == 0):
                tableau[ligne, colonne] = "X"
            else:
                tableau[ligne, colonne] = "O"

            # afficher le tableau et vérifier s'il a gagné
            print(tableau)
            resultat = gagner(tableau, num_joueur)

            # le joueur courant a gagné
            if(resultat == True):
                print("Bravo ", joueur_courant)

            # passer au prochain joueur, prochain tour
            else:
                # on teste rempli après ex aequo au cas où la dernière case à remplir fait gagner l'un des joueurs

                #######################################################################################
                nb_case = 0  # nombre de cases remplis, si ç atteint 9 c'est que le tableau est rempli
                for l in range(0, 3):
                    for c in range(0, 3):
                        if (tableau[l, c] != "."):
                            nb_case += 1
                if(nb_case == 9):
                    rempli = True
                #######################################################################################

                tour += 1
                if(num_joueur == 0):
                    num_joueur = 1
                else:
                    num_joueur = 0

    # ex aequo
    if(resultat == False):
        print("personne n'a gagné, tentez votre chance une nouvelle fois !")


lancer_jeu()
