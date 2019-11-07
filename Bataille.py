##IMPORTATION

from random import randint




##VARIABLE

card = {1: ["Deux", 0], 2: ["Trois", 0]} # Dictionnaire associant un nombre à une carte (numéro de la carte : [nom de la carte, nombre de carte prise])


# Liste des cartes des joueurs
cardP1 = [] # Joueur 1
cardP2 = [] # Joueur 2

cardNumber = 52 # Nombre de cartes dans le paquet de jeu


##FONCTION




##SCRIPT

# Attribution des cartes aux joueurs
while len(cardP1) < 26 and len(cardP2) < 26:
    # Joueur 1
    cardRandom = randint(1, 13)
    substitute = card[cardRandom]
    substitute[1] += 1
    while substitute[1] > 4:
        cardRandom = randint(1, 13)
        substitute = card[cardRandom]
        substitute[1] -= 1
    cardP1.append(cardRandom)
    # Joueur 2
    cardRandom = randint(1, 13)
    substitute = card[cardRandom]
    while substitute[1] > 4:
        cardRandom = randint(1, 13)
        substitute = card[cardRandom]
        substitute[1] -= 1
    cardP2.append(cardRandom)
