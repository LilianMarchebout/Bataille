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
    while len(cardP1) < cardNumber/2 and len(cardP2) < cardNumber/2:
        # Joueur 1
        cardRandom = randint(1, 13)
        substitute = card[cardRandom]
        substitute[1] += 1
        if substitute[1] > 4:
            substitute[1] -= 1
            distribution()
        else:
            cardP1.append(cardRandom)
        # Joueur 2
        cardRandom = randint(1, 13)
        substitute = card[cardRandom]
        substitute[1] += 1
        if substitute[1] > 4:
            substitute[1] -= 1
            distribution()
        else:
            cardP2.append(cardRandom)


def round():
    cardPlayP1 = cardP1[0]
    cardPlayP2 = cardP2[0]
    if cardPlayP1 > cardPlayP2: #Joueur 1 gagne la manche
        # Met à la fin du paquet du joueur la carte jouée
        cardP1.remove(cardPlayP1)
        cardP1.append(cardPlayP1)
        # Ajoute la carte gagné et la supprimme à l'adversaire
        cardP2.remove(cardPlayP2)
        cardP1.append(cardPlayP2)
    if cardPlayP1 < cardPlayP2: #Joueur 2 gagne la manche
        # Met à la fin du paquet du joueur la carte jouée
        cardP2.remove(cardPlayP2)
        cardP2.append(cardPlayP2)
        # Ajoute la carte gagné et la supprimme à l'adversaire
        cardP1.remove(cardPlayP1)
        cardP2.append(cardPlayP1)



##SCRIPT
distribution()