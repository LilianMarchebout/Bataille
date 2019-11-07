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




##SCRIPT

# Distribution des cartes aux joueurs
def distribution():
    while len(cardP1) < 26:
        # Joueur 1
        cardRandom = randint(1, 13)
        substitute = card[cardRandom]
        substitute[1] += 1
        if substitute[1] > 4:
            substitute[1] -= 1
            distribution()
        cardP1.append(cardRandom)
    while len(cardP2) < 26:
        # Joueur 2
        cardRandom = randint(1, 13)
        substitute = card[cardRandom]
        if substitute[1] > 4:
            substitute[1] -= 1
            distribution()
        cardP2.append(cardRandom)

#Affichage
distribution()
print("liste P1 =")
for boucle in range(len(cardP1)):
    substitue = cardP1[boucle]
    print(boucle , ":" , card[substitue])
print("liste P2 =")
for boucle in range(len(cardP2)):
    substitue = cardP2[boucle]
    print(boucle , ":" , card[substitue])
print("dictionnaire = ")
for boucle in range(len(card)):
    print(card[boucle+1])