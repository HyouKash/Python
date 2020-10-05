from random import randint

boucle = True
compteurGame = {"Partie Jouées":0, "Victoires":0, "Défaites":0}

class juste_prix :
    def __init__(self):
        self.nombreAl = (randint(1,100))
        self.nombreAchoisir = 0
    
    def LeJeu(self):
        compteur = 0
        while self.nombreAchoisir != self.nombreAl:
            try:
                self.nombreAchoisir = int(input("D'après-vous, lequel est le bon ? : "))
                if self.nombreAchoisir < 1 or self.nombreAchoisir > 100:
                    print("Entre 1 et 100 s'il vous plait")
                else:
                    if self.nombreAchoisir > self.nombreAl :
                        print("trop grand")
                        compteur += 1
                        if compteur == 5:
                            print("Attention c'est déjà la 5 ième tentative, à la dixième c'est la défaite")
                        elif compteur == 10:
                            print("C'est perdu, dommage !")
                            compteurGame["Partie Jouées"] += 1
                            compteurGame["Défaites"] += 1
                            break;
                    elif self.nombreAchoisir == self.nombreAl :
                        print ("Bien joué, le nombre est bien : " + str(self.nombreAchoisir) + ", tu as trouvé en : " + str(compteur + 1) + " coups")
                        compteurGame["Partie Jouées"] += 1
                        compteurGame["Victoires"] += 1
                    else:
                        print("trop petit")
                        compteur += 1
                        if compteur == 5:
                            print("Attention c'est déjà la 5 ième tentative, à la dixième c'est la défaite")
                        elif compteur == 10:
                            print("C'est perdu, dommage !")
                            compteurGame["Partie Jouées"] += 1
                            compteurGame["Défaites"] += 1
                            break;
            except ValueError:
                print("Ce n'est pas un entier!")
                
while boucle == True:
    Jeux = juste_prix()
    Jeux.LeJeu()
    reponse = str(input('Voulez-vous faire une autre partie ? : '))
    if reponse == "Oui" or reponse == "oui":
        Jeux.LeJeu()
    else:
        boucle = False
        print("Au revoir")
        print("Votre ratio Jouées/Victoire/Défaite est : " + str(compteurGame))