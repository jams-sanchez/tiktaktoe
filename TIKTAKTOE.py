# joueurs
joueur_1= "X"
joueur_2= "O"
symbole = ""

# tableau
board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
ligne1 = board[0]
ligne2 = board[1]
ligne3 = board[2]

# Affiche la grille
def grille():
    print()
    print("|".join(ligne1))
    print("|".join(ligne2))
    print("|".join(ligne3))
    print()

# Efface le tableau d'une partie terminée
def efface():
    global ligne1
    global ligne2
    global ligne3
    global board
    board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    ligne1 = board[0]
    ligne2 = board[1]
    ligne3 = board[2]
    grille()
    changement_joueur()

# Rejouer au jeu 
def relancer_partie():
    global tour
    print()
    print("Voulez-vous rejouer ? ")
    rejouer = int(input("[1] Oui ou [2] Non "))
    if rejouer == 2:
        print()
        print("Aurevoir !")
        print()
    # Si le joueur souhaite jouer
    elif rejouer == 1:
        efface()
    # Erreur si le joueur entre une lettre non demandé
    else:
        print("Erreur! Entrez [1] Oui ou [2] Non")
        print()
        return relancer_partie()

# Vérifie si un joueur a une ligne gagnante OU si la partie est égalité
def verifie():
    # Joueur 1 - vérification horizontale
    if board[0] == ["X", "X", "X"] \
    or board[1] == ["X", "X", "X"] \
    or board[2] == ["X", "X", "X"]:
        print("HOORAY!")
        print("Joueur 1 gagne !")
        return True
    # Joueur 1 - vérification verticale
    elif board[0][0] == joueur_1 and board[1][0] == joueur_1 and board[2][0] == joueur_1 \
    or board[0][1] == joueur_1 and board[1][1] == joueur_1 and board[2][1] == joueur_1 \
    or board[0][2] == joueur_1 and board[1][2] == joueur_1 and board[2][2] == joueur_1:
        print("HOORAY!")
        print("Joueur 1 gagne !")
        return True
    # Joueur 1 - vérification diagonale
    elif board[0][0] == joueur_1 and board[1][1] == joueur_1 and board[2][2] == joueur_1 \
    or board[0][2] == joueur_1 and board[1][1] == joueur_1 and board[2][0] == joueur_1:
        print("HOORAY!")
        print("Joueur 1 gagne !")
        return True
    # Joueur 2 - vérification horizontale
    if board[0] == ["O", "O", "O"] \
    or board[1] == ["O", "O", "O"] \
    or board[2] == ["O", "O", "O"]:
        print("HOORAY!")
        print("Joueur 2 gagne !")
        return True
    # Joueur 2 - vérification verticale
    elif board[0][0] == joueur_2 and board[1][0] == joueur_2 and board[2][0] == joueur_2 \
    or board[0][1] == joueur_2 and board[1][1] == joueur_2 and board[2][1] == joueur_2 \
    or board[0][2] == joueur_2 and board[1][2] == joueur_2 and board[2][2] == joueur_2:
        print("HOORAY!")
        print("Joueur 2 gagne !")
        return True
    # Joueur 2 - vérification diagonale
    elif board[0][0] == joueur_2 and board[1][1] == joueur_2 and board[2][2] == joueur_2 \
    or board[0][2] == joueur_2 and board[1][1] == joueur_2 and board[2][0] == joueur_2:
        print("HOORAY!")
        print("Joueur 2 gagne !")
        return True
    # Vérification d'une égalité
    elif tour == 10:
        print("C'est une égalite !")
        print()
        return True
    else:
        return False

# Changement de joueur entre les tours
def changement_joueur():
    global tour
    global joueur_1
    global joueur_2
    global symbole
    tour = 1
    while verifie() != True and tour <= 10:
        if tour % 2 == 1:
            symbole = joueur_1
            print("Joueur 1, c'est à ton tour de jouer!")
        else:
            symbole = joueur_2
            print("Joueur 2, c'est à ton tour de jouer!")
        actions()
        tour += 1
    relancer_partie()
    
                                   
# Défini l'action des joueurs ET vérifie si les informations demandées
def actions():
    # Erreur qui apparait si les éléments demandés ne sont pas respecté
    while True:
        action_1 = int(input("Sur quelle ligne voulez-vous jouer ? (1,2,3) : "))
        if action_1 > 3 or action_1 == 0:
            print()
            print("1- Erreur, entrez un numéro 1, 2 ou 3")
            print()
        else:
            break
    while True:
        action_2 = int(input("Dans quelle colonne ? (1,2,3) : "))
        if action_2 > 3 or action_2 == 0:
            print()
            print("2- Erreur, entrez un numéro 1, 2 ou 3")
            print()
        else:
            break
    # Détermine une action en ligne 1 
    # ET une erreur si l'emplacement est déjà occupé par l'adversaire
    if action_1 == 1:
        if ligne1[action_2 - 1] == "_":
            ligne1[action_2 - 1] = symbole
        else:
            print()
            print("OOPS! Il semblerait que cet emplacement soit déjà occupé.")
            print("Essaie-en un autre :)")
            print()   
            return actions()           
    # Détermine une action en ligne 2 
    # ET une erreur si l'emplacement est déjà occupé par l'adversaire
    elif action_1 == 2:
        if ligne2[action_2 - 1] == "_":
            ligne2[action_2 - 1] = symbole
        else:
            print()
            print("OOPS! Il semblerait que cet emplacement soit déjà occupé.")
            print("Essaie-en un autre :)")
            print()
            return actions()
    # Détermine une action en ligne 3 
    # ET une erreur si l'emplacement est déjà occupé par l'adversaire
    elif action_1 == 3:
        if ligne3[action_2 - 1] == "_":
            ligne3[action_2 - 1] = symbole
        else:
            print()
            print("OOPS! Il semblerait que cet emplacement soit déjà occupé.")
            print("Essaie-en un autre :)")
            print()
            return actions()
    # Imprime le rendu du tableau au fur a mesure des actions des joueurs
    grille()

# Lancement du jeu Tik Tak Toe
def lancement_jeu():
    print("Voulez vous commencer la partie ?")
    print()
    adversaire = int(input("[1] Oui ou [2] Non : "))
    # Si le joueur choisi de jouer
    if adversaire == 1:
        grille()
        changement_joueur()
    # Si le joueur ne veut pas jouer
    elif adversaire == 2:
        print()
        print("Aurevoir")
        print()
    # Affiche une erreur si le numéro entré n'est pas celui demandé
    else:
        print("! ERREUR !")
        print("Saisissez 1 ou 2")
        print()
        print("[1] Pour jouer contre une IA")
        print("[2] pour jouer contre un adversaire réel")
        print()
        return lancement_jeu()
        
# Pré-lancement du jeu - Message d'Accueil
def pre_lancement():
    print()
    print("Bienvenue dans Tik Tak Toe ! ")
    print("Un monde de grilles et de symboles")
    print()
    lancement_jeu()

# Appel au lancement du jeu dans le terminal
pre_lancement()