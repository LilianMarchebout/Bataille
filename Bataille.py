##IMPORTATION

from random import randint




##VARIABLE

# Dictionnaire associant un nombre à une carte (numéro de la carte : [nom de la carte, nombre de carte prise])
card = {1: ["Deux", 0], 
2: ["Trois", 0], 
3: ["Quatre", 0], 
4: ["Cinq", 0], 
5: ["Six", 0], 
6: ["Sept", 0], 
7: ["Huit", 0], 
8: ["Neuf", 0], 
9: ["Dix", 0], 
10: ["Valet", 0], 
11: ["Dame", 0], 
12: ["Roi", 0], 
13: ["As", 0]} 


# Liste des cartes des joueurs
cardP1 = [] # Joueur 1
cardP2 = [] # Joueur 2

cardNumber = 52 # Nombre de cartes dans le paquet de jeu




##FONCTION
def distribution():
    """
    Distribution des cartes aux joueurs
    """
    while len(cardP1) < cardNumber/2:
        # Joueur 1
        cardRandom = randint(1, 13)
        substitute = card[cardRandom]
        substitute[1] += 1
        if substitute[1] > 4:
            substitute[1] -= 1
            distribution()
        else:
            cardP1.append(cardRandom)
    while len(cardP2) < cardNumber/2:
        # Joueur 2
        cardRandom = randint(1, 13)
        substitute = card[cardRandom]
        substitute[1] += 1
        if substitute[1] > 4:
            substitute[1] -= 1
            distribution()
        else:
            cardP2.append(cardRandom)




##SCRIPT
distribution()